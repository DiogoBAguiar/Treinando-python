import pyautogui
import pyperclip
import time
import logging

class ControladorTeclado:
    def __init__(self):
        """
        Gerencia a interação com o teclado.
        """
        # Pausa menor para teclado, pois queremos digitar rápido
        pyautogui.PAUSE = 0.05 

    def escrever(self, texto):
        """
        Digita um texto na tela.
        Usa a técnica do Clipboard (Ctrl+V) para garantir que acentos (ç, ã, é)
        saiam corretamente no Windows em Português.
        """
        try:
            # 1. Copia o texto para a memória temporária (Clipboard)
            pyperclip.copy(texto)
            
            # 2. Cola o texto
            # Esperamos um micro-segundo para o OS processar o clipboard
            time.sleep(0.05) 
            pyautogui.hotkey('ctrl', 'v')
            
        except Exception as e:
            logging.error(f"Erro ao digitar texto via clipboard: {e}")
            # Fallback: Tenta digitar tecla por tecla se o clipboard falhar
            pyautogui.write(texto)

    def pressionar(self, tecla):
        """
        Pressiona uma tecla única.
        Ex: 'enter', 'tab', 'esc', 'backspace', 'win'
        """
        try:
            pyautogui.press(tecla)
        except Exception as e:
            logging.error(f"Tecla inválida: {tecla} - {e}")

    def atalho(self, *teclas):
        """
        Executa um atalho de múltiplas teclas.
        Uso: atalho('ctrl', 'c') ou atalho('alt', 'tab')
        """
        try:
            pyautogui.hotkey(*teclas)
        except Exception as e:
            logging.error(f"Erro no atalho {teclas}: {e}")

    # =========================================================================
    # MACROS E FUNÇÕES DE EDIÇÃO (Abstração)
    # =========================================================================

    def selecionar_tudo(self):
        self.atalho('ctrl', 'a')

    def copiar(self):
        self.atalho('ctrl', 'c')

    def colar(self):
        self.atalho('ctrl', 'v')

    def apagar_palavra(self):
        """
        Apaga a palavra inteira à esquerda do cursor.
        Padrão Windows: Ctrl + Backspace
        """
        self.atalho('ctrl', 'backspace')

    def nova_linha(self):
        """
        Pula linha sem enviar o formulário (Shift + Enter)
        """
        self.atalho('shift', 'enter')