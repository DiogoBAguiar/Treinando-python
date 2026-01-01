# core/event_bus.py
import logging
import threading
from collections import defaultdict

class Evento:
    """
    Objeto que carrega os dados do evento.
    """
    def __init__(self, tipo, dados=None):
        self.tipo = tipo
        self.dados = dados if dados else {}

    def __repr__(self):
        return f"<Evento {self.tipo}: {self.dados}>"

class EventBus:
    def __init__(self):
        # Dicionário onde a chave é o nome do evento e o valor é uma lista de funções
        self.assinantes = defaultdict(list)
        # Lock para garantir que threads não briguem ao publicar ao mesmo tempo
        self._lock = threading.Lock()

    def inscrever(self, tipo_evento, funcao_callback):
        """
        Um módulo chama isso para 'ouvir' um tipo de evento.
        :param tipo_evento: String (da classe Eventos)
        :param funcao_callback: Função que receberá o objeto Evento
        """
        with self._lock:
            self.assinantes[tipo_evento].append(funcao_callback)
            logging.debug(f"Nova inscrição em '{tipo_evento}': {funcao_callback.__name__}")

    def publicar(self, evento):
        """
        Dispara um evento para todos os interessados.
        """
        tipo = evento.tipo
        
        # Se ninguém estiver ouvindo, apenas ignora (ou loga)
        if tipo not in self.assinantes:
            return

        # Notifica todos os inscritos
        # Nota: Estamos rodando na thread de quem publicou. 
        # Em sistemas maiores, usaríamos uma fila para processar em background.
        with self._lock:
            lista_callbacks = self.assinantes[tipo][:] # Cópia para segurança

        for callback in lista_callbacks:
            try:
                callback(evento)
            except Exception as e:
                logging.error(f"Erro ao processar evento '{tipo}': {e}", exc_info=True)

# Instância Global (Singleton)
# Assim, qualquer arquivo pode fazer 'from core.event_bus import bus' e usar o mesmo canal.
bus = EventBus()