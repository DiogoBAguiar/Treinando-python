from typing import Final

class Eventos:
    """
    CONTRATO DE API DO SISTEMA (Event-Driven Architecture).
    
    Esta classe define todos os canais de comunicação (tópicos) do barramento.
    Abaixo de cada constante está a definição do PAYLOAD (dados) esperado.
    """

    # =========================================================================
    # 1. EVENTOS DE ENTRADA (Sensores)
    # =========================================================================
    
    # Disparado quando o motor STT (Vosk) detecta uma frase completa.
    # Payload: {"texto": str}
    # Exemplo: {"texto": "abrir o navegador"}
    VOZ_RECONHECIDA: Final[str] = "evt_voz_reconhecida"

    # Disparado quando o motor de NLU identifica uma intenção clara (Fase 2 do projeto).
    # Payload: {"intencao": str, "confianca": float, "entidades": dict}
    INTENCAO_DETECTADA: Final[str] = "evt_intencao_detectada"

    # =========================================================================
    # 2. EVENTOS DE COMANDO (Atuadores)
    # =========================================================================
    
    # Ordem para o sistema de áudio falar algo (TTS).
    # Payload: {"texto": str, "prioridade": str (opcional)}
    # Exemplo: {"texto": "Abrindo Spotify"}
    CMD_FALAR: Final[str] = "cmd_falar"

    # Ordem para controle do mouse.
    # Payload: {"tipo": str, ...args}
    #   - tipo="clique" | "duplo" | "direita"
    #   - tipo="mover_setor", "setor": int (1-9)
    #   - tipo="rolar", "direcao": "cima"|"baixo"
    CMD_MOUSE: Final[str] = "cmd_mouse"

    # Ordem para controle de teclado.
    # Payload: {"acao": str, "dados": str}
    #   - acao="escrever", "dados": "texto para digitar"
    #   - acao="atalho", "dados": "ctrl+c"
    CMD_TECLADO: Final[str] = "cmd_teclado"

    # Ordem para gestão de janelas e processos.
    # Payload: {"acao": str, "nome": str}
    #   - acao="abrir", "nome": "chrome"
    #   - acao="fechar", "nome": "notepad"
    CMD_APP: Final[str] = "cmd_app"

    # Ordem global de sistema (Ciclo de Vida).
    # Payload: {"acao": str}
    #   - acao="desligar"
    CMD_SISTEMA: Final[str] = "cmd_sistema"

    # =========================================================================
    # 3. EVENTOS DE INTERFACE (Feedback Visual)
    # =========================================================================
    
    # Atualiza o texto da legenda flutuante (HUD).
    # Payload: {"texto": str, "tipo": str (opcional: "info"|"erro"|"sucesso")}
    UI_ATUALIZAR_STATUS: Final[str] = "ui_status"

    # Controla a exibição da grade do mouse.
    # Payload: {"estado": str} -> "mostrar" | "ocultar"
    UI_ATUALIZAR_GRADE: Final[str] = "ui_grade"

    # =========================================================================
    # 4. OBSERVABILIDADE (Logs e Debug)
    # =========================================================================
    
    # Evento genérico para logs centralizados.
    # Payload: {"nivel": str, "msg": str, "origem": str}
    LOG_SISTEMA: Final[str] = "log_sistema"