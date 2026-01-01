import sys
import threading
import logging
import ctypes 

# Configuração de Log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logging.info("--- INICIANDO JARVIS (EVENT DRIVEN) ---")

# Imports da Arquitetura
from core.event_bus import bus
from core.engine import MotorDeAudio
from core.processor import Processador
from interface.overlay import VoiceOverlay

# --- CORREÇÃO AQUI ---
# Importamos as CLASSES, não só os módulos
from funcionalidades.mouse_grid import ControladorMouse
from funcionalidades.teclado import ControladorTeclado
from funcionalidades.aplicativos import ControladorApps
from funcionalidades.voz import Speaker

def configurar_alta_resolucao():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

def main():
    configurar_alta_resolucao()

    # 1. INICIALIZAÇÃO DOS SERVIÇOS (Ligar os rádios)
    # Ao criar a instância, o __init__ roda e se inscreve no barramento.
    logging.info("Iniciando serviços periféricos...")
    servico_mouse = ControladorMouse()
    servico_teclado = ControladorTeclado()
    servico_apps = ControladorApps()
    servico_voz = Speaker()

    # 2. Inicializa o Cérebro (Lógica)
    logging.info("Iniciando Processador Central...")
    cerebro = Processador()

    # 3. Inicializa o Ouvido (Motor Vosk)
    logging.info("Iniciando Motor de Áudio...")
    motor = MotorDeAudio()
    thread_audio = threading.Thread(target=motor.iniciar, daemon=True)
    thread_audio.start()

    # 4. Inicializa a Interface (Main Loop)
    logging.info("Carregando Interface...")
    app = VoiceOverlay()
    
    try:
        logging.info("Sistema Online. Pode falar.")
        app.mainloop()
    except KeyboardInterrupt:
        logging.info("Interrupção manual.")

if __name__ == "__main__":
    main()