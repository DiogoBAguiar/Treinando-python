import os
import sys
import json
import queue
import logging
import sounddevice as sd
import vosk
from typing import Optional

# Imports de Configuração
from config import MODEL_PATH, SAMPLE_RATE, BLOCK_SIZE, CHANNELS

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class MotorDeAudio:
    """
    Motor de Reconhecimento de Fala (STT - Speech to Text).
    Responsável por capturar o áudio do microfone em tempo real e transcrever
    usando o modelo offline VOSK.
    """
    def __init__(self):
        # Fila thread-safe para passar dados do callback (C) para o Python
        self._q_audio: queue.Queue[bytes] = queue.Queue()
        self._rodando: bool = False
        self._rec: Optional[vosk.KaldiRecognizer] = None
        
        self._inicializar_vosk()

    def _inicializar_vosk(self) -> None:
        """Carrega o modelo VOSK na memória com validação de caminho."""
        if not os.path.exists(MODEL_PATH):
            msg = f"CRÍTICO: Modelo Vosk não encontrado em: {MODEL_PATH}"
            logging.critical(msg)
            # Publica erro para quem estiver ouvindo (ex: Interface/Logs)
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "CRITICAL", "msg": msg, "origem": "Engine"}))
            return

        logging.info(f"Carregando modelo Vosk de: {MODEL_PATH} ...")
        try:
            model = vosk.Model(MODEL_PATH)
            # Inicializa o reconhecedor
            self._rec = vosk.KaldiRecognizer(model, SAMPLE_RATE)
            self._rec.SetWords(False) # Otimização: Não precisamos de timestamp por palavra
            logging.info("Motor Vosk carregado com sucesso.")
        except Exception as e:
            logging.critical(f"Falha fatal ao instanciar Vosk: {e}", exc_info=True)
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "CRITICAL", "msg": f"Erro Vosk: {e}", "origem": "Engine"}))
            sys.exit(1) # Erro irrecuperável, o programa não funciona sem ouvidos.

    def _callback_microfone(self, indata, frames, time, status) -> None:
        """
        Callback executado pelo SoundDevice em uma Thread separada (nível de sistema).
        AVISO: Não execute operações pesadas aqui. Apenas coloque dados na fila.
        """
        if status:
            logging.warning(f"Status do áudio (SoundDevice): {status}")
        self._q_audio.put(bytes(indata))

    def iniciar(self) -> None:
        """
        Inicia o loop principal de escuta. 
        Este método é BLOQUEANTE e deve rodar numa Thread separada no main.py.
        """
        if not self._rec:
            logging.error("Tentativa de iniciar motor sem modelo carregado.")
            return

        self._rodando = True
        logging.info("Abrindo stream de áudio...")
        
        bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "INFO", "msg": "Microfone Ativo", "origem": "Engine"}))

        try:
            # Context Manager garante que o microfone feche se houver erro
            with sd.RawInputStream(
                samplerate=SAMPLE_RATE, 
                blocksize=BLOCK_SIZE, 
                device=None, 
                dtype='int16',
                channels=CHANNELS, 
                callback=self._callback_microfone
            ):
                logging.info("Ouvindo...")
                
                while self._rodando:
                    # Pega dados da fila com timeout.
                    # O timeout permite que o loop verifique 'self._rodando' periodicamente,
                    # permitindo que a thread encerre suavemente.
                    try:
                        data = self._q_audio.get(timeout=1.0)
                    except queue.Empty:
                        continue

                    # Processamento Vosk (CPU Bound)
                    if self._rec.AcceptWaveform(data):
                        resultado = json.loads(self._rec.Result())
                        texto = resultado.get("text", "")
                        
                        if texto:
                            self._processar_texto_reconhecido(texto)

        except Exception as e:
            logging.error(f"Erro no stream de áudio: {e}", exc_info=True)
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "ERROR", "msg": f"Erro Mic: {e}", "origem": "Engine"}))
            
        finally:
            self._rodando = False
            logging.info("Stream de áudio encerrado.")

    def _processar_texto_reconhecido(self, texto: str) -> None:
        """Publica o texto reconhecido no barramento para consumo do sistema."""
        logging.info(f"Reconhecido: '{texto}'")
        
        # 1. Atualiza Interface (Feedback Visual Rápido)
        bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": f"🗣️ {texto}"}))
        
        # 2. Envia para o Cérebro (Lógica de Decisão)
        bus.publicar(Evento(Eventos.VOZ_RECONHECIDA, {"texto": texto}))

    def parar(self) -> None:
        """Sinaliza para o loop de áudio encerrar na próxima iteração."""
        logging.info("Solicitando parada do Motor de Áudio...")
        self._rodando = False