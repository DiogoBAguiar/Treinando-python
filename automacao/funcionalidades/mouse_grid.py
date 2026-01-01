import pyautogui
import logging
from config import SCROLL_SPEED, MOUSE_DURATION, MAPA_NUMEROS
from core.event_bus import bus, Evento
from core.definitions import Eventos

class ControladorMouse:
    def __init__(self):
        """
        Módulo Especialista: Controle do Mouse.
        Arquitetura: Event-Driven (Ouve CMD_MOUSE no barramento).
        """
        # Configurações de Segurança do PyAutoGUI
        pyautogui.FAILSAFE = True 
        pyautogui.PAUSE = 0.01 

        # Dados da Tela
        self.largura_tela, self.altura_tela = pyautogui.size()
        
        # Pré-cálculo da grade numérica (1-9)
        self.grade_coords = self._calcular_centroides_grade()

        # --- INSCRIÇÃO NO BARRAMENTO ---
        # A partir de agora, qualquer evento CMD_MOUSE será entregue nesta função
        bus.inscrever(Eventos.CMD_MOUSE, self.processar_evento)
        
        logging.info("Serviço de Mouse iniciado e aguardando eventos.")

    def processar_evento(self, evento):
        """
        Recebe o pacote de dados do EventBus e executa a ação física.
        Payload esperado: {"tipo": "...", "setor": 5, "direcao": "baixo"}
        """
        dados = evento.dados
        tipo = dados.get("tipo")
        
        try:
            if tipo == "clique":
                self.clicar()
            elif tipo == "duplo":
                self.clique_duplo()
            elif tipo == "direita":
                self.clique_direito()
            
            elif tipo == "mover_setor":
                setor = dados.get("setor")
                if sector:
                    self.mover_para_setor(setor)
            
            elif tipo == "rolar":
                direcao = dados.get("direcao")
                if direcao:
                    self.rolar(direcao)
                    
        except Exception as e:
            logging.error(f"Erro ao executar comando de mouse '{tipo}': {e}")

    # =========================================================================
    # LÓGICA MATEMÁTICA E FÍSICA (Mantida igual)
    # =========================================================================

    def _calcular_centroides_grade(self):
        """Calcula o centro (x,y) dos 9 setores da tela."""
        w = self.largura_tela / 3
        h = self.altura_tela / 3
        coords = {}
        
        # Mapa lógico (Teclado Numérico)
        mapa_logico = {
            7: (0, 0), 8: (1, 0), 9: (2, 0),
            4: (0, 1), 5: (1, 1), 6: (2, 1),
            1: (0, 2), 2: (1, 2), 3: (2, 2)
        }

        for numero, (col, lin) in mapa_logico.items():
            center_x = (col * w) + (w / 2)
            center_y = (lin * h) + (h / 2)
            coords[numero] = (center_x, center_y)
            
        return coords

    def mover_para_setor(self, numero):
        """Move o cursor para o setor especificado."""
        if numero in self.grade_coords:
            x, y = self.grade_coords[numero]
            try:
                pyautogui.moveTo(x, y, duration=MOUSE_DURATION)
                return True
            except pyautogui.FailSafeException:
                logging.warning("Movimento cancelado pelo FailSafe.")
                return False
        return False

    def clicar(self):
        pyautogui.click()

    def clique_duplo(self):
        pyautogui.doubleClick()

    def clique_direito(self):
        pyautogui.rightClick()

    def rolar(self, direcao):
        """
        Rola a página.
        """
        if direcao == "baixo":
            pyautogui.scroll(-SCROLL_SPEED)
        elif direcao == "cima":
            pyautogui.scroll(SCROLL_SPEED)

    # Métodos dummy para manter compatibilidade caso algo antigo chame,
    # mas o controle visual agora é via Evento UI_ATUALIZAR_GRADE na Interface.
    def mostrar_grade(self): pass
    def ocultar_grade(self): pass