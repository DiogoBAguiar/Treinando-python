import logging
import threading
import webbrowser
import difflib
from typing import Dict, List, Optional
from AppOpener import give_appnames, open as app_open, close as app_close

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class ControladorApps:
    """
    Gestor de Aplicativos e Sites.
    Responsável por catalogar, abrir e fechar softwares.
    
    Características Avançadas:
    - Indexação Assíncrona: Não trava o boot do sistema.
    - Busca Fuzzy: Entende nomes aproximados (ex: 'Exel' -> 'Excel').
    - Priorização: Sites favoritos abrem instantaneamente.
    """
    def __init__(self):
        # Cache de apps (começa vazio e enche em background)
        self._apps_instalados: List[str] = []
        self._indexacao_concluida: bool = False
        self._status_erro: bool = False
        
        # Sites de acesso rápido (bypass do AppOpener)
        self._sites_favoritos: Dict[str, str] = {
            "chat gpt": "https://chat.openai.com",
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "whatsapp": "https://web.whatsapp.com",
            "github": "https://github.com",
            "stackoverflow": "https://stackoverflow.com",
            "gmail": "https://mail.google.com",
            "netflix": "https://netflix.com",
            "spotify web": "https://open.spotify.com"
        }

        # Inicia a indexação em background para o Jarvis ligar instantaneamente
        t = threading.Thread(target=self._indexar_apps_background, daemon=True)
        t.start()

        # Inscreve-se no barramento
        bus.inscrever(Eventos.CMD_APP, self._processar_evento)
        
        logging.info("Serviço de Apps iniciado (Indexação rodando em background...)")

    def _indexar_apps_background(self) -> None:
        """
        Tarefa pesada: Varre o registro do Windows para listar programas.
        Roda em thread separada.
        """
        try:
            # upper=False retorna tudo em minúsculo para facilitar a busca
            apps = give_appnames(upper=False)
            self._apps_instalados = list(apps) if apps else []
            self._indexacao_concluida = True
            
            logging.info(f"Indexação de Apps concluída: {len(self._apps_instalados)} programas encontrados.")
            # Opcional: Avisar no log que está pronto
            bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "INFO", "msg": "Catálogo de Apps atualizado", "origem": "Apps"}))
            
        except Exception as e:
            self._status_erro = True
            logging.error(f"Falha crítica ao indexar aplicativos: {e}", exc_info=True)

    def _processar_evento(self, evento: Evento) -> None:
        """Roteador de comandos vindos do Barramento."""
        dados = evento.dados
        acao = dados.get("acao")
        nome = dados.get("nome")
        
        if not nome: 
            return

        if acao == "abrir":
            self.abrir(nome)
        elif acao == "fechar":
            self.fechar(nome)

    def _falar(self, texto: str) -> None:
        """Atalho para enviar feedback de voz."""
        bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": texto}))

    def abrir(self, nome_falado: str) -> None:
        """
        Lógica inteligente de abertura.
        1. Verifica Sites Favoritos.
        2. Verifica Apps Instalados (Fuzzy Match).
        """
        nome_limpo = nome_falado.lower().strip()

        # 1. Tenta Site (Rápido e garantido)
        if nome_limpo in self._sites_favoritos:
            url = self._sites_favoritos[nome_limpo]
            self._falar(f"Abrindo site {nome_limpo}")
            webbrowser.open(url)
            return

        # 2. Verifica status da indexação
        if not self._indexacao_concluida:
            if self._status_erro:
                self._falar("Houve um erro ao ler seus programas. Tente reiniciar.")
            else:
                self._falar("Ainda estou lendo a lista de programas. Aguarde um momento.")
            return

        # 3. Busca Fuzzy (Aproximada)
        # cutoff=0.5 significa que precisa ter 50% de semelhança
        matches = difflib.get_close_matches(nome_limpo, self._apps_instalados, n=1, cutoff=0.5)
        
        if matches:
            melhor_match = matches[0]
            
            # Se o nome for diferente, avisa o usuário qual programa achou
            if melhor_match != nome_limpo:
                self._falar(f"Abrindo {melhor_match}")
            else:
                self._falar(f"Iniciando {melhor_match}")
            
            # Executa em thread para o Jarvis não travar enquanto o Windows carrega o programa
            threading.Thread(target=self._executar_abertura_win, args=(melhor_match,)).start()
        else:
            self._falar(f"Não encontrei o aplicativo {nome_limpo} instalado.")

    def _executar_abertura_win(self, nome_real: str) -> None:
        """Chamada real ao sistema operacional."""
        try:
            app_open(nome_real, match_closest=True, throw_error=True)
        except Exception as e:
            logging.error(f"Erro ao abrir '{nome_real}': {e}")
            self._falar(f"Ocorreu um erro ao tentar iniciar {nome_real}.")

    def fechar(self, nome_falado: str) -> None:
        """Tenta encerrar o processo."""
        nome_limpo = nome_falado.lower().strip()
        
        # Não conseguimos fechar abas específicas do navegador facilmente via comando
        if nome_limpo in self._sites_favoritos:
            self._falar("Para fechar sites, diga 'Fechar Janela'.")
            return

        self._falar(f"Fechando {nome_limpo}")
        
        # Tenta fechar de forma assíncrona
        def _task_fechar():
            try:
                app_close(nome_limpo, match_closest=True, throw_error=True)
            except Exception:
                # AppOpener reclama se não achar o processo rodando, podemos ignorar
                logging.warning(f"Tentativa de fechar '{nome_limpo}' falhou ou app não estava aberto.")
                
        threading.Thread(target=_task_fechar).start()