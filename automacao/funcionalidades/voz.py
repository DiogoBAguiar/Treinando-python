import os
import pygame
import edge_tts
import asyncio
import threading
import logging
import winsound # <--- NOVO: Biblioteca nativa do Windows para sons de sistema
from core.event_bus import bus, Evento
from core.definitions import Eventos

# Configuração da Voz (Português Brasil)
VOZ_ESCOLHIDA = "pt-BR-AntonioNeural"

class Speaker:
    def __init__(self):
        """
        Módulo de Voz (TTS - Text to Speech).
        Arquitetura: Event-Driven (Ouve CMD_FALAR no barramento).
        """
        try:
            # Inicializa o mixer de áudio
            pygame.mixer.init()
            
            # Cria pasta temporária
            self.temp_dir = "temp_audio"
            if not os.path.exists(self.temp_dir):
                os.makedirs(self.temp_dir)
            
            # --- INSCRIÇÃO NO BARRAMENTO ---
            # Ouve qualquer pedido de fala vindo do sistema
            bus.inscrever(Eventos.CMD_FALAR, self.processar_evento)
            
            logging.info(f"Serviço de Voz iniciado ({VOZ_ESCOLHIDA}).")
            
        except Exception as e:
            logging.error(f"Erro ao iniciar sistema de som: {e}")

    def processar_evento(self, evento):
        """
        Recebe o evento do barramento: {"texto": "Olá mundo"}
        """
        texto = evento.dados.get("texto")
        if texto:
            self.falar(texto)

    def falar(self, texto):
        """
        Inicia a thread para baixar e tocar o áudio sem travar o sistema.
        """
        logging.info(f"Jarvis diz: {texto}")
        
        # Thread dedicada para I/O de rede e disco
        t = threading.Thread(target=self._thread_wrapper, args=(texto,))
        t.start()

    def _thread_wrapper(self, texto):
        """
        Wrapper para rodar código assíncrono (Edge-TTS) dentro de uma thread síncrona.
        """
        try:
            asyncio.run(self._gerar_e_tocar(texto))
        except Exception as e:
            logging.error(f"Erro na síntese de voz: {e}")
            # --- FALLBACK DE EMERGÊNCIA ---
            # Se a voz falhar (ex: sem internet), faz um Beep para o usuário saber.
            try:
                # Frequência 400Hz (Grave), Duração 400ms
                winsound.Beep(400, 400) 
            except:
                pass

    async def _gerar_e_tocar(self, texto):
        """
        Lógica pesada: Conecta na Azure -> Baixa MP3 -> Toca no Pygame.
        """
        arquivo_mp3 = os.path.join(self.temp_dir, "fala_temp.mp3")
        
        try:
            # 1. Gera o arquivo de áudio (Edge TTS)
            # Pode falhar aqui se estiver sem internet
            comunicate = edge_tts.Communicate(texto, VOZ_ESCOLHIDA)
            await comunicate.save(arquivo_mp3)
            
            # 2. Reproduz o áudio
            if os.path.exists(arquivo_mp3):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                
                pygame.mixer.music.load(arquivo_mp3)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                
                pygame.mixer.music.unload()
                
        except PermissionError:
            logging.warning("Conflito de arquivo de áudio (fala muito rápida).")
        except Exception as e:
            # Relança o erro para cair no except do _thread_wrapper e tocar o Beep
            raise e