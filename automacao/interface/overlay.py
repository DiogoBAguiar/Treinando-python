import tkinter as tk
import logging
from typing import Optional

# Imports de Configuração
from config import (
    UI_COR_GRADE, UI_COR_TEXTO, UI_COR_FUNDO, 
    UI_FONTE_LEGENDA, UI_FONTE_GRADE, UI_CHROMA_KEY, 
    UI_OPACIDADE, UI_COR_DESTAQUE, UI_COR_INATIVO
)

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class VoiceOverlay(tk.Tk):
    """
    Interface Gráfica Transparente (HUD).
    Exibe legendas e a grade de controle do mouse.
    Arquitetura: Event-Driven e Thread-Safe.
    """
    def __init__(self):
        super().__init__()
        
        # --- CONFIGURAÇÃO DA JANELA (TRANSPARÊNCIA E POSIÇÃO) ---
        self.overrideredirect(True) # Remove barra de título e bordas
        
        # Ocupa toda a tela
        self.largura = self.winfo_screenwidth()
        self.altura = self.winfo_screenheight()
        self.geometry(f"{self.largura}x{self.altura}+0+0")
        
        # Mantém sempre no topo
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-alpha", UI_OPACIDADE)
        
        # Define a cor de fundo como transparente (Chroma Key)
        # Tudo que for pintado com UI_CHROMA_KEY ficará invisível
        self.configure(bg=UI_CHROMA_KEY)
        self.wm_attributes("-transparentcolor", UI_CHROMA_KEY)

        # --- ELEMENTOS VISUAIS ---
        # Canvas é onde desenhamos a grade
        self.canvas = tk.Canvas(self, width=self.largura, height=self.altura, 
                                bg=UI_CHROMA_KEY, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Legenda de Status (Canto Superior Esquerdo)
        self.lbl_status = tk.Label(self, text="Inicializando...", font=UI_FONTE_LEGENDA,
                                   fg=UI_COR_TEXTO, bg=UI_COR_FUNDO, padx=10, pady=5)
        self.lbl_status.place(x=20, y=20)
        
        # Timer para limpar legendas automaticamente
        self._timer_id: Optional[str] = None

        # --- INSCRIÇÃO NO BARRAMENTO ---
        bus.inscrever(Eventos.UI_ATUALIZAR_STATUS, self._on_update_status)
        bus.inscrever(Eventos.UI_ATUALIZAR_GRADE, self._on_update_grade)
        bus.inscrever(Eventos.CMD_SISTEMA, self._on_system_cmd)
        
        logging.info("Interface Gráfica iniciada e inscrita no barramento.")

    # =========================================================================
    # HANDLERS DE EVENTOS (Thread-Safe)
    # O Tkinter NÃO é thread-safe. Se chamarmos self.lbl.config() de outra thread,
    # o programa crasha. Usamos self.after(0, func) para agendar a execução na Main Thread.
    # =========================================================================

    def _on_update_status(self, evento: Evento) -> None:
        texto = evento.dados.get("texto")
        if texto:
            self.after(0, lambda: self._atualizar_legenda_ui(str(texto)))

    def _on_update_grade(self, evento: Evento) -> None:
        estado = evento.dados.get("estado")
        if estado == "mostrar":
            self.after(0, self._desenhar_grade_ui)
        elif estado == "ocultar":
            self.after(0, self._limpar_grade_ui)

    def _on_system_cmd(self, evento: Evento) -> None:
        acao = evento.dados.get("acao")
        if acao in ["desligar", "fechar"]:
            self.after(0, self._encerrar_programa)

    # =========================================================================
    # MÉTODOS DE DESENHO (Executados na Main Thread)
    # =========================================================================

    def _atualizar_legenda_ui(self, texto: str) -> None:
        """Atualiza o texto e a cor da legenda."""
        cor = UI_COR_TEXTO
        
        # Lógica de Cores baseada no contexto
        if "Dormindo" in texto: 
            cor = UI_COR_INATIVO
        elif "Ativo" in texto or "Online" in texto: 
            cor = UI_COR_DESTAQUE
        elif "🗣️" in texto: # Ícone de fala (Input do usuário)
            cor = "#FFFF00" # Amarelo para destaque do que foi ouvido
            
        self.lbl_status.config(text=texto, fg=cor)
        
        # Gerenciamento do Timer para limpar a mensagem
        if self._timer_id:
            self.after_cancel(self._timer_id)
        
        # Se for uma frase reconhecida, volta para o status padrão após 4 segundos
        if "🗣️" in texto:
            self._timer_id = self.after(4000, lambda: self.lbl_status.config(text="Ouvindo...", fg=UI_COR_TEXTO))

    def _desenhar_grade_ui(self) -> None:
        """Desenha a grade 3x3 na tela."""
        self._limpar_grade_ui() # Garante que não desenhamos por cima
        w = self.largura
        h = self.altura
        
        # Configurações visuais
        TAG = "grade"
        LARGURA_LINHA = 2
        
        # Linhas Verticais
        self.canvas.create_line(w/3, 0, w/3, h, fill=UI_COR_GRADE, width=LARGURA_LINHA, tags=TAG)
        self.canvas.create_line(2*w/3, 0, 2*w/3, h, fill=UI_COR_GRADE, width=LARGURA_LINHA, tags=TAG)
        
        # Linhas Horizontais
        self.canvas.create_line(0, h/3, w, h/3, fill=UI_COR_GRADE, width=LARGURA_LINHA, tags=TAG)
        self.canvas.create_line(0, 2*h/3, w, 2*h/3, fill=UI_COR_GRADE, width=LARGURA_LINHA, tags=TAG)
        
        # Números nos centros
        posicoes = {
            "7": (w/6, h/6),   "8": (w/2, h/6),   "9": (5*w/6, h/6),
            "4": (w/6, h/2),   "5": (w/2, h/2),   "6": (5*w/6, h/2),
            "1": (w/6, 5*h/6), "2": (w/2, 5*h/6), "3": (5*w/6, 5*h/6)
        }
        
        for num, (x, y) in posicoes.items():
            # Círculo de fundo para o número ficar legível
            raio = 30
            self.canvas.create_oval(x-raio, y-raio, x+raio, y+raio, 
                                    fill=UI_COR_FUNDO, outline=UI_COR_GRADE, width=2, tags=TAG)
            self.canvas.create_text(x, y, text=num, font=UI_FONTE_GRADE, fill=UI_COR_TEXTO, tags=TAG)

    def _limpar_grade_ui(self) -> None:
        """Remove todos os elementos da grade."""
        self.canvas.delete("grade")

    def _encerrar_programa(self) -> None:
        logging.info("Interface encerrando...")
        self.destroy()