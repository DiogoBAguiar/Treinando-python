import os
import sys
import json
import queue
import logging
import sounddevice as sd
import vosk

# Imports de Configuração
from config import MODEL_PATH, SAMPLE_RATE, BLOCK_SIZE, CHANNELS

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class MotorDeAudio:
    def __init__(self):
        """
        Responsável apenas por:
        1. Capturar áudio do microfone.
        2. Transcrever áudio para texto (Vosk).
        3. Publicar o evento VOZ_RECONHECIDA no Barramento.
        """
        self.q_audio = queue.Queue()
        self.rodando = False

        # Validação do Modelo
        if not os.path.exists(MODEL_PATH):
            logging.critical(f"Modelo não encontrado em: {MODEL_PATH}")
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"msg": "CRÍTICO: Modelo Vosk não encontrado!"}))
            return

        logging.info("Carregando modelo Vosk...")
        try:
            # Carrega o modelo
            self.model = vosk.Model(MODEL_PATH)
            
            # Inicializa o reconhecedor em MODO LIVRE (Sem vocabulário restrito)
            self.rec = vosk.KaldiRecognizer(self.model, SAMPLE_RATE)
            self.rec.SetWords(False) # Não precisamos timestamp de cada palavra
            
            logging.info("Motor de Áudio pronto para ouvir.")
            
        except Exception as e:
            logging.error(f"Erro fatal ao carregar Vosk: {e}")
            sys.exit(1)

    def _callback_microfone(self, indata, frames, time, status):
        """
        Chamado pelo sounddevice toda vez que o buffer do microfone enche.
        """
        if status:
            logging.warning(f"Status do áudio: {status}")
        self.q_audio.put(bytes(indata))

    def iniciar(self):
        """
        Loop principal de escuta.
        """
        self.rodando = True
        
        logging.info("Abrindo stream de áudio...")
        
        # Notifica o sistema que o ouvido abriu
        bus.publicar(Evento(Eventos.LOG_SISTEMA, {"msg": "Microfone Aberto"}))
        
        try:
            with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, device=None,
                                   dtype='int16', channels=CHANNELS, callback=self._callback_microfone):
                
                logging.info("Ouvindo...")
                
                while self.rodando:
                    # Pega o áudio bruto da fila
                    data = self.q_audio.get()
                    
                    # O Vosk processa o pedaço de áudio
                    if self.rec.AcceptWaveform(data):
                        resultado = json.loads(self.rec.Result())
                        texto = resultado.get("text", "")
                        
                        if texto:
                            logging.info(f"Reconhecido: '{texto}'")
                            
                            # --- O PULO DO GATO (EVENT DRIVEN) ---
                            # 1. Publica para a Interface atualizar a legenda
                            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": f"🗣️ {texto}"}))
                            
                            # 2. Publica para o Cérebro processar
                            bus.publicar(Evento(Eventos.VOZ_RECONHECIDA, {"texto": texto}))

        except Exception as e:
            logging.error(f"Erro no loop de áudio: {e}")
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"msg": f"Erro Áudio: {e}"}))