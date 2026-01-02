import logging
import threading
from collections import defaultdict
from typing import Dict, List, Callable, Any, Optional

class Evento:
    """
    Classe que representa um evento disparado no sistema.
    Carrega o tipo do evento e um dicionário de dados (payload).
    """
    def __init__(self, tipo: str, dados: Optional[Dict[str, Any]] = None):
        self.tipo = tipo
        self.dados = dados if dados else {}

    def __repr__(self):
        return f"<Evento type='{self.tipo}' data={self.dados}>"

class EventBus:
    """
    Barramento de Eventos (Padrão Publish/Subscribe).
    Gerencia a comunicação assíncrona entre os módulos do sistema.
    Thread-Safe.
    """
    def __init__(self):
        # Mapeia: "nome_evento" -> [funcao_callback1, funcao_callback2]
        self._assinantes: Dict[str, List[Callable[[Evento], None]]] = defaultdict(list)
        # Assinantes que querem ouvir TUDO (wildcard)
        self._assinantes_globais: List[Callable[[Evento], None]] = []
        # Lock para garantir segurança entre threads (Interface vs Audio vs Logica)
        self._lock = threading.RLock()

    def inscrever(self, tipo_evento: str, callback: Callable[[Evento], None]):
        """
        Registra uma função para ser chamada quando 'tipo_evento' ocorrer.
        
        :param tipo_evento: String identificadora do evento (ex: 'cmd_mouse').
                            Use '*' para escutar todos os eventos.
        :param callback: Função que recebe um objeto Evento.
        """
        with self._lock:
            if tipo_evento == "*":
                if callback not in self._assinantes_globais:
                    self._assinantes_globais.append(callback)
                    logging.debug(f"Novo ouvinte global registrado: {callback.__name__}")
            else:
                if callback not in self._assinantes[tipo_evento]:
                    self._assinantes[tipo_evento].append(callback)
                    logging.debug(f"Nova inscrição em '{tipo_evento}': {callback.__name__}")

    def desinscrever(self, tipo_evento: str, callback: Callable[[Evento], None]):
        """
        Remove um ouvinte do barramento. Útil para desligar plugins ou limpar memória.
        """
        with self._lock:
            try:
                if tipo_evento == "*":
                    if callback in self._assinantes_globais:
                        self._assinantes_globais.remove(callback)
                elif tipo_evento in self._assinantes:
                    if callback in self._assinantes[tipo_evento]:
                        self._assinantes[tipo_evento].remove(callback)
                        # Se não houver mais ninguém ouvindo esse evento, limpa a chave
                        if not self._assinantes[tipo_evento]:
                            del self._assinantes[tipo_evento]
                logging.debug(f"Removido ouvinte de '{tipo_evento}': {callback.__name__}")
            except ValueError:
                logging.warning(f"Tentativa de desinscrever callback inexistente em '{tipo_evento}'")

    def publicar(self, evento: Evento):
        """
        Dispara um evento para todos os interessados.
        O processamento ocorre na Thread de quem publicou (Síncrono por padrão).
        
        :param evento: Objeto da classe Evento.
        """
        tipo = evento.tipo
        
        # 1. Recupera listas de callbacks (cópia defensiva para evitar erro se a lista mudar durante loop)
        with self._lock:
            callbacks_especificos = self._assinantes.get(tipo, [])[:]
            callbacks_globais = self._assinantes_globais[:]

        todas_callbacks = callbacks_globais + callbacks_especificos

        if not todas_callbacks:
            # logging.debug(f"Evento '{tipo}' publicado, mas ninguém ouviu.")
            return

        # 2. Executa os callbacks
        for callback in todas_callbacks:
            try:
                callback(evento)
            except Exception as e:
                # O erro de um módulo não pode derrubar o barramento
                logging.error(
                    f"ERRO ao processar evento '{tipo}' no callback '{callback.__name__}': {e}", 
                    exc_info=True
                )

# Instância Global (Singleton Pattern)
# Importe esta variável 'bus' em outros arquivos.
bus = EventBus()