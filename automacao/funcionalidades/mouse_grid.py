import pyautogui
import logging
from typing import Dict, Tuple, Optional, Any

# Imports de Configuração
from config import SCROLL_SPEED, MOUSE_DURATION

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class ControladorMouse:
    """
    Controlador de Hardware (Mouse).
    Executa ações físicas baseadas em eventos do sistema.
    
    Funcionalidades:
    - Grade Numérica (1-9): Move o cursor para setores da tela.
    - Cliques: Esquerdo, Direito, Duplo.
    - Rolagem: Scroll suave.
    """
    def __init__(self):
        # Configurações de Segurança do PyAutoGUI
        # Se o usuário jogar o mouse para o canto superior esquerdo, lança FailSafeException
        pyautogui.FAILSAFE = True 
        pyautogui.PAUSE = 0.01 

        # Dados da Tela
        self._largura_tela, self._altura_tela = pyautogui.size()
        
        # Pré-cálculo da grade para performance (Cache de Coordenadas)
        # Formato: { 1: (x, y), 2: (x, y), ... }
        self._grade_coords: Dict[int, Tuple[int, int]] = self._calcular_centroides_grade()

        # Inscrição no Barramento
        bus.inscrever(Eventos.CMD_MOUSE, self._processar_evento)
        
        logging.info(f"Serviço de Mouse iniciado (Resolução: {self._largura_tela}x{self._altura_tela})")

    def _calcular_centroides_grade(self) -> Dict[int, Tuple[int, int]]:
        """
        Divide a tela em uma matriz 3x3 e calcula o ponto central (x,y) de cada setor.
        Mapeamento baseado no Teclado Numérico (Numpad):
        7 8 9
        4 5 6
        1 2 3
        """
        w = self._largura_tela / 3
        h = self._altura_tela / 3
        coords = {}
        
        # Mapeamento Lógico (Numpad -> Matriz Coluna/Linha)
        mapa_logico = {
            7: (0, 0), 8: (1, 0), 9: (2, 0),
            4: (0, 1), 5: (1, 1), 6: (2, 1),
            1: (0, 2), 2: (1, 2), 3: (2, 2)
        }

        for numero, (col, lin) in mapa_logico.items():
            # Calcula o centro do retângulo
            center_x = int((col * w) + (w / 2))
            center_y = int((lin * h) + (h / 2))
            coords[numero] = (center_x, center_y)
            
        return coords

    def _processar_evento(self, evento: Evento) -> None:
        """
        Callback disparado pelo Barramento.
        Payload esperado: {"tipo": str, ...args}
        """
        dados = evento.dados
        tipo = dados.get("tipo")
        
        try:
            if tipo == "clique":
                self._clicar()
            elif tipo == "duplo":
                self._clique_duplo()
            elif tipo == "direita":
                self._clique_direito()
            
            elif tipo == "mover_setor":
                setor = dados.get("setor")
                if isinstance(setor, int):
                    self._mover_para_setor(setor)
            
            elif tipo == "rolar":
                direcao = dados.get("direcao")
                if direcao:
                    self._rolar(str(direcao))
                    
        except pyautogui.FailSafeException:
            logging.warning("Movimento de mouse abortado pelo usuário (FailSafe).")
            # Opcional: Avisar via voz que parou
            bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": "Movimento cancelado."}))
            
        except Exception as e:
            logging.error(f"Erro ao executar comando de mouse '{tipo}': {e}", exc_info=True)

    def _mover_para_setor(self, numero: int) -> bool:
        """Move o cursor suavemente para o centro do setor numérico."""
        if numero in self._grade_coords:
            x, y = self._grade_coords[numero]
            pyautogui.moveTo(x, y, duration=MOUSE_DURATION)
            return True
        return False

    def _clicar(self) -> None:
        pyautogui.click()

    def _clique_duplo(self) -> None:
        pyautogui.doubleClick()

    def _clique_direito(self) -> None:
        pyautogui.rightClick()

    def _rolar(self, direcao: str) -> None:
        """Rola a página verticalmente."""
        clicks = SCROLL_SPEED if direcao == "cima" else -SCROLL_SPEED
        pyautogui.scroll(clicks)