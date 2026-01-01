# core/definitions.py

class Eventos:
    """
    Lista oficial de todos os eventos que podem ocorrer no sistema.
    Isso serve como contrato entre os módulos.
    """
    # Eventos de Entrada (Sensores)
    VOZ_RECONHECIDA = "evt_voz_reconhecida"  # Payload: {"texto": "abrir chrome"}
    
    # Eventos de Intenção (O que o usuário quer fazer)
    INTENCAO_DETECTADA = "evt_intencao_detectada" # Payload: {"acao": "abrir", "alvo": "chrome"}
    
    # Eventos de Ação (Execução)
    CMD_MOUSE = "cmd_mouse"       # Payload: {"tipo": "clique", "x": 0, "y": 0}
    CMD_TECLADO = "cmd_teclado"   # Payload: {"teclas": ["ctrl", "c"]}
    CMD_APP = "cmd_app"           # Payload: {"acao": "abrir", "nome": "chrome"}
    CMD_SISTEMA = "cmd_sistema"   # Payload: {"acao": "desligar"}
    
    # Eventos de Interface (Feedback)
    UI_ATUALIZAR_STATUS = "ui_status" # Payload: {"texto": "Ouvindo...", "cor": "green"}
    UI_ATUALIZAR_GRADE = "ui_grade"   # Payload: {"estado": "mostrar"}
    
    # Eventos de Log/Debug
    LOG_SISTEMA = "log_sistema"       # Payload: {"nivel": "INFO", "msg": "..."}