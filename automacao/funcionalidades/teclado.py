import time
import logging
import pyautogui
import pyperclip # Essencial para acentos e caracteres especiais
from typing import List, Union

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class ControladorTeclado:
    """
    Controlador de Hardware (Teclado).
    Executa digitação de texto e atalhos de sistema.
    
    Destaque Técnico:
    - Utiliza 'Clipboard Injection' para garantir que acentos (ç, ã, é)
      sejam digitados corretamente, contornando limitações do driver de teclado US/ABNT.
    """
    def __init__(self):
        # Configuração de segurança
        pyautogui.FAILSAFE = True
        
        # Inscreve-se no barramento
        bus.inscrever(Eventos.CMD_TECLADO, self._processar_evento)
        
        logging.info("Serviço de Teclado iniciado.")

    def _processar_evento(self, evento: Evento) -> None:
        """
        Callback disparado pelo Barramento.
        Payload esperado: {"acao": "escrever"|"atalho", "dados": str}
        """
        dados = evento.dados
        acao = dados.get("acao")
        conteudo = dados.get("dados") # O texto ou o atalho
        
        if not conteudo:
            return

        try:
            if acao == "escrever":
                self._escrever_via_clipboard(str(conteudo))
            elif acao == "atalho":
                self._executar_atalho(str(conteudo))
                
        except Exception as e:
            logging.error(f"Erro ao executar comando de teclado '{acao}': {e}", exc_info=True)
            # Feedback de erro opcional
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "⚠️ Erro Teclado"}))

    def _escrever_via_clipboard(self, texto: str) -> None:
        """
        Digita texto complexo usando a área de transferência.
        Isso resolve problemas de acentuação do PyAutoGUI.
        """
        if not texto: return
        
        try:
            # 1. Salva o clipboard atual (opcional, para ser gentil com o usuário)
            # backup = pyperclip.paste()
            
            # 2. Copia o novo texto
            pyperclip.copy(texto)
            
            # 3. Cola (Ctrl+V)
            # Pequeno delay para o sistema operacional processar a cópia
            time.sleep(0.1) 
            pyautogui.hotkey("ctrl", "v")
            
            logging.info(f"Texto digitado (via Clipboard): {texto[:20]}...")
            
        except Exception as e:
            logging.error(f"Falha ao usar clipboard: {e}")
            # Fallback: Tenta digitar caractere por caractere (sem acentos)
            pyautogui.write(texto)

    def _executar_atalho(self, combinacao: str) -> None:
        """
        Executa atalhos simples ("enter") ou compostos ("ctrl+c").
        """
        # Normaliza a string (remove espaços extras)
        teclas = [k.strip().lower() for k in combinacao.split("+")]
        
        logging.info(f"Executando atalho: {teclas}")
        
        try:
            # Desempacota a lista de teclas para o hotkey
            # Ex: hotkey('ctrl', 'alt', 'del')
            pyautogui.hotkey(*teclas)
        except Exception as e:
            logging.error(f"Atalho inválido ou falha na execução: {combinacao} - {e}")

    # Métodos legados de suporte (se necessário expansão futura)
    def selecionar_tudo(self):
        self._executar_atalho("ctrl+a")

    def copiar(self):
        self._executar_atalho("ctrl+c")

    def colar(self):
        self._executar_atalho("ctrl+v")