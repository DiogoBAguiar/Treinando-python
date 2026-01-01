import tkinter as tk
import threading
import queue
import sys
import os
import json
import pyautogui
import sounddevice as sd
import vosk

# --- CONFIGURAÇÕES ---
SAMPLE_RATE = 16000
MODEL_PATH = "model"
COR_GRADE = "#00FF00"  # Verde Hacker (Alta visibilidade)
COR_TEXTO = "white"
COR_FUNDO_LEGENDA = "black"

# Vocabulário restrito para máxima velocidade e pouca RAM
VOCABULARIO = '["clicar", "duplo", "direita", "rolar", "cima", "baixo", "parar", "dormir", "acordar", "fechar", "grade", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "zerar"]'

# Fila de comunicação entre a Voz (Thread) e a Tela (Tkinter)
fila_comandos = queue.Queue()
fila_status = queue.Queue()

class VoiceOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuração da Janela Transparente (Ocupa toda a tela)
        self.overrideredirect(True) # Remove barra de título
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.wm_attributes("-topmost", True) # Sempre no topo
        self.wm_attributes("-transparentcolor", "black") # Define preto como invisível
        self.configure(bg="black")
        
        self.grade_visivel = False
        self.sistema_ativo = True # Se False, está em modo "Dormir"
        
        # Canvas para desenhar linhas e números
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg="black", highlightthickness=0)
        self.canvas.pack()
        
        # Label de Status (Feedback do que foi ouvido)
        self.lbl_status = tk.Label(self, text="Inicializando...", font=("Arial", 14, "bold"), fg="white", bg="#202020")
        self.lbl_status.place(x=10, y=10)
        
        # Loop de verificação da fila
        self.after(100, self.checar_fila)

    def desenhar_grade(self):
        """Desenha a grade 3x3 na tela"""
        self.canvas.delete("grade") # Limpa grade anterior
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        
        # Linhas Verticais
        self.canvas.create_line(w/3, 0, w/3, h, fill=COR_GRADE, width=2, tags="grade")
        self.canvas.create_line(2*w/3, 0, 2*w/3, h, fill=COR_GRADE, width=2, tags="grade")
        
        # Linhas Horizontais
        self.canvas.create_line(0, h/3, w, h/3, fill=COR_GRADE, width=2, tags="grade")
        self.canvas.create_line(0, 2*h/3, w, 2*h/3, fill=COR_GRADE, width=2, tags="grade")
        
        # Números
        numeros = {
            "7": (w/6, h/6),   "8": (w/2, h/6),   "9": (5*w/6, h/6),
            "4": (w/6, h/2),   "5": (w/2, h/2),   "6": (5*w/6, h/2),
            "1": (w/6, 5*h/6), "2": (w/2, 5*h/6), "3": (5*w/6, 5*h/6)
        }
        
        for num, pos in numeros.items():
            # Círculo de fundo
            self.canvas.create_oval(pos[0]-25, pos[1]-25, pos[0]+25, pos[1]+25, fill="blue", outline=COR_GRADE, tags="grade")
            # Número
            self.canvas.create_text(pos[0], pos[1], text=num, font=("Arial", 24, "bold"), fill="white", tags="grade")
            
        self.grade_visivel = True

    def ocultar_grade(self):
        self.canvas.delete("grade")
        self.grade_visivel = False

    def atualizar_status(self, texto, cor="white"):
        self.lbl_status.config(text=texto, fg=cor)
        # Limpa o texto após 3 segundos
        self.after(3000, lambda: self.lbl_status.config(text="Ouvindo..."))

    def checar_fila(self):
        """Verifica se a thread de áudio mandou algum comando"""
        try:
            while True:
                tipo, valor = fila_comandos.get_nowait()
                
                if tipo == "STATUS":
                    self.atualizar_status(valor)
                
                elif tipo == "CMD_GRADE":
                    if valor == "mostrar": self.desenhar_grade()
                    elif valor == "ocultar": self.ocultar_grade()
                
                elif tipo == "CMD_SISTEMA":
                    if valor == "dormir":
                        self.sistema_ativo = False
                        self.atualizar_status("💤 Dormindo (Diga 'Acordar')", "gray")
                    elif valor == "acordar":
                        self.sistema_ativo = True
                        self.atualizar_status("🟢 Ativo", "green")
                    elif valor == "fechar":
                        self.destroy()
                        sys.exit()

                # Só executa comandos de mouse se o sistema estiver ACORDADO
                elif tipo == "EXEC" and self.sistema_ativo:
                    funcao, arg = valor
                    if arg: funcao(arg)
                    else: funcao()
                    
        except queue.Empty:
            pass
        
        self.after(50, self.checar_fila)


# --- LÓGICA DE ÁUDIO (RODA EM THREAD SEPARADA) ---
def motor_de_audio():
    if not os.path.exists(MODEL_PATH):
        print("MODELO NÃO ENCONTRADO")
        return

    model = vosk.Model(MODEL_PATH)
    rec = vosk.KaldiRecognizer(model, SAMPLE_RATE, VOCABULARIO)
    
    q_audio = queue.Queue()
    
    def audio_callback(indata, frames, time, status):
        q_audio.put(bytes(indata))

    w_scr, h_scr = pyautogui.size()

    # Mapa numérico para coordenadas (Grade Teclado Numérico)
    # 7 8 9
    # 4 5 6
    # 1 2 3
    mapa_grade = {
        "um": (w_scr/6, 5*h_scr/6),    "dois": (w_scr/2, 5*h_scr/6),   "três": (5*w_scr/6, 5*h_scr/6),
        "quatro": (w_scr/6, h_scr/2),  "cinco": (w_scr/2, h_scr/2),    "seis": (5*w_scr/6, h_scr/2),
        "sete": (w_scr/6, h_scr/6),    "oito": (w_scr/2, h_scr/6),     "nove": (5*w_scr/6, h_scr/6)
    }

    print("Motor de áudio iniciado.")
    fila_comandos.put(("STATUS", "Pronto! Diga 'Grade'"))

    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, device=None, dtype='int16', channels=1, callback=audio_callback):
        while True:
            data = q_audio.get()
            if rec.AcceptWaveform(data):
                resultado = json.loads(rec.Result())
                texto = resultado.get("text", "")
                
                if not texto: continue
                
                # Feedback na tela
                fila_comandos.put(("STATUS", f"Ouvido: {texto}"))
                
                # --- COMANDOS DE CONTROLE ---
                if "dormir" in texto:
                    fila_comandos.put(("CMD_SISTEMA", "dormir"))
                    continue # Pula o resto
                
                if "acordar" in texto:
                    fila_comandos.put(("CMD_SISTEMA", "acordar"))
                    continue

                if "fechar" in texto:
                    fila_comandos.put(("CMD_SISTEMA", "fechar"))
                    break

                # --- COMANDOS DE AÇÃO ---
                if "grade" in texto:
                    fila_comandos.put(("CMD_GRADE", "mostrar"))
                
                elif "zerar" in texto: # Comando para limpar a tela
                    fila_comandos.put(("CMD_GRADE", "ocultar"))

                elif "clicar" in texto:
                    fila_comandos.put(("EXEC", (pyautogui.click, None)))
                
                elif "duplo" in texto:
                    fila_comandos.put(("EXEC", (pyautogui.doubleClick, None)))
                
                elif "direita" in texto:
                    fila_comandos.put(("EXEC", (pyautogui.rightClick, None)))
                
                elif "rolar" in texto and "baixo" in texto:
                    fila_comandos.put(("EXEC", (pyautogui.scroll, -300)))
                
                elif "rolar" in texto and "cima" in texto:
                    fila_comandos.put(("EXEC", (pyautogui.scroll, 300)))

                # --- NAVEGAÇÃO POR NÚMEROS ---
                else:
                    for num_extenso, coords in mapa_grade.items():
                        if num_extenso in texto:
                            # Move o mouse
                            fila_comandos.put(("EXEC", (pyautogui.moveTo, coords)))
                            # Opcional: Ocultar a grade após mover?
                            # fila_comandos.put(("CMD_GRADE", "ocultar"))
                            break

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    # Inicia a thread de áudio
    t_audio = threading.Thread(target=motor_de_audio, daemon=True)
    t_audio.start()
    
    # Inicia a interface gráfica (Bloqueia o código aqui, deve ser o último)
    app = VoiceOverlay()
    app.mainloop()