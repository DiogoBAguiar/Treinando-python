import tkinter as tk
import logging
from config import (
    UI_COR_GRADE, UI_COR_TEXTO, UI_COR_FUNDO, 
    UI_FONTE_LEGENDA, UI_FONTE_GRADE, UI_CHROMA_KEY, 
    UI_OPACIDADE, UI_COR_DESTAQUE, UI_COR_INATIVO
)
from core.event_bus import bus, Evento
from core.definitions import Eventos

class VoiceOverlay(tk.Tk):
    def __init__(self):
        """
        Interface Gráfica (HUD).
        Arquitetura: Event-Driven (Ouve eventos UI_* no barramento).
        """
        super().__init__()
        
        # --- CONFIGURAÇÃO DA JANELA (TRANSPARÊNCIA) ---
        self.overrideredirect(True) # Remove bordas
        self.largura = self.winfo_screenwidth()
        self.altura = self.winfo_screenheight()
        self.geometry(f"{self.largura}x{self.altura}+0+0")
        
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-alpha", UI_OPACIDADE)
        
        # Define a cor de fundo como transparente
        self.configure(bg=UI_CHROMA_KEY)
        self.wm_attributes("-transparentcolor", UI_CHROMA_KEY)

        # --- ELEMENTOS VISUAIS ---
        self.canvas = tk.Canvas(self, width=self.largura, height=self.altura, 
                                bg=UI_CHROMA_KEY, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.lbl_status = tk.Label(self, text="Inicializando...", font=UI_FONTE_LEGENDA,
                                   fg=UI_COR_TEXTO, bg=UI_COR_FUNDO, padx=10, pady=5)
        self.lbl_status.place(x=20, y=20)

        # --- INSCRIÇÃO NO BARRAMENTO ---
        # Ouvimos eventos de status, grade e sistema
        bus.inscrever(Eventos.UI_ATUALIZAR_STATUS, self.on_update_status)
        bus.inscrever(Eventos.UI_ATUALIZAR_GRADE, self.on_update_grade)
        bus.inscrever(Eventos.CMD_SISTEMA, self.on_system_cmd)
        
        logging.info("Interface Gráfica inscrita no barramento.")

    # =========================================================================
    # HANDLERS DE EVENTOS (Thread-Safe)
    # =========================================================================

    def on_update_status(self, evento):
        """Recebe o evento em qualquer thread e agenda atualização na Main Thread."""
        texto = evento.dados.get("texto")
        if texto:
            # self.after(0, ...) garante que o Tkinter execute isso na thread principal
            self.after(0, lambda: self._atualizar_legenda_ui(texto))

    def on_update_grade(self, evento):
        estado = evento.dados.get("estado")
        if estado == "mostrar":
            self.after(0, self._desenhar_grade_ui)
        elif estado == "ocultar":
            self.after(0, self._limpar_grade_ui)

    def on_system_cmd(self, evento):
        acao = evento.dados.get("acao")
        if acao == "desligar" or acao == "fechar":
            self.after(0, self.encerrar_programa)

    # =========================================================================
    # MÉTODOS DE DESENHO (Rodam na Main Thread)
    # =========================================================================

    def _atualizar_legenda_ui(self, texto):
        color = UI_COR_TEXTO
        
        # Muda a cor se for status de sistema
        if "Dormindo" in texto: color = UI_COR_INATIVO
        elif "Ativo" in texto: color = UI_COR_DESTAQUE
            
        self.lbl_status.config(text=texto, fg=color)
        
        # Timer para limpar feedback rápido
        if hasattr(self, '_timer_id'):
            self.after_cancel(self._timer_id)
        
        # Se for mensagem de reconhecimento, volta para "Ouvindo" depois de 3s
        if "🗣️" in texto:
            self._timer_id = self.after(3000, lambda: self.lbl_status.config(text="Ouvindo...", fg=UI_COR_TEXTO))

    def _desenhar_grade_ui(self):
        self._limpar_grade_ui()
        w = self.largura
        h = self.altura
        
        # Linhas
        self.canvas.create_line(w/3, 0, w/3, h, fill=UI_COR_GRADE, width=2, tags="grade")
        self.canvas.create_line(2*w/3, 0, 2*w/3, h, fill=UI_COR_GRADE, width=2, tags="grade")
        self.canvas.create_line(0, h/3, w, h/3, fill=UI_COR_GRADE, width=2, tags="grade")
        self.canvas.create_line(0, 2*h/3, w, 2*h/3, fill=UI_COR_GRADE, width=2, tags="grade")
        
        # Números
        posicoes = {
            "7": (w/6, h/6), "8": (w/2, h/6), "9": (5*w/6, h/6),
            "4": (w/6, h/2), "5": (w/2, h/2), "6": (5*w/6, h/2),
            "1": (w/6, 5*h/6), "2": (w/2, 5*h/6), "3": (5*w/6, 5*h/6)
        }
        for num, (x, y) in posicoes.items():
            self.canvas.create_oval(x-25, y-25, x+25, y+25, fill=UI_COR_FUNDO, outline=UI_COR_GRADE, tags="grade")
            self.canvas.create_text(x, y, text=num, font=UI_FONTE_GRADE, fill=UI_COR_TEXTO, tags="grade")

    def _limpar_grade_ui(self):
        self.canvas.delete("grade")

    def encerrar_programa(self):
        logging.info("Interface encerrando...")
        self.destroy()