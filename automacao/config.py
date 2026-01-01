import os

# =============================================================================
# 1. DIRETÓRIOS E CAMINHOS
# =============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model")

if not os.path.exists(MODEL_PATH):
    print(f"[AVISO CRÍTICO] Pasta do modelo não encontrada em: {MODEL_PATH}")

# =============================================================================
# 2. CONFIGURAÇÕES DE ÁUDIO
# =============================================================================
SAMPLE_RATE = 16000
BLOCK_SIZE = 8000
CHANNELS = 1

# (A seção VOCABULÁRIO foi removida pois agora usamos o modo Livre)

# =============================================================================
# 3. INTERFACE GRÁFICA (UI / UX)
# =============================================================================
UI_COR_GRADE = "#00FF00"      # Verde Neon
UI_COR_TEXTO = "#FFFFFF"      # Branco
UI_COR_FUNDO = "#101010"      # Fundo das legendas
UI_COR_DESTAQUE = "#00BFFF"   # Azul
UI_COR_INATIVO = "#808080"    # Cinza

# Transparência
UI_CHROMA_KEY = "black"       # Cor que fica invisível
UI_OPACIDADE = 0.8            # 0.0 a 1.0

# Fontes
UI_FONTE_LEGENDA = ("Segoe UI", 16, "bold")
UI_FONTE_GRADE = ("Arial", 24, "bold")

# =============================================================================
# 4. MAPEAMENTOS LÓGICOS (MUITO IMPORTANTE MANTER)
# =============================================================================
# Isso ainda é usado pelo processador para saber que "um" = 1
MAPA_NUMEROS = {
    "um": 1, "dois": 2, "três": 3,
    "quatro": 4, "cinco": 5, "seis": 6,
    "sete": 7, "oito": 8, "nove": 9
}

# Configurações de Mouse
SCROLL_SPEED = 300
MOUSE_DURATION = 0.1