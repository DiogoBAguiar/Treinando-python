import logging
import webbrowser
import difflib
from AppOpener import give_appnames, open as app_open, close as app_close
from core.event_bus import bus, Evento
from core.definitions import Eventos

class ControladorApps:
    def __init__(self): # Não recebe mais 'speaker'
        self.sites_favoritos = {
            "chat gpt": "https://chat.openai.com",
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "whatsapp": "https://web.whatsapp.com",
            "github": "https://github.com"
        }
        
        logging.info("Indexando aplicativos instalados...")
        self.lista_apps = give_appnames()
        
        # Inscrição no Barramento
        bus.inscrever(Eventos.CMD_APP, self.processar_evento)
        logging.info("Serviço de Apps iniciado.")

    def processar_evento(self, evento):
        acao = evento.dados.get("acao")
        nome = evento.dados.get("nome")
        
        if acao == "abrir":
            self.abrir(nome)
        elif acao == "fechar":
            self.fechar(nome)

    def _falar(self, texto):
        """
        Método auxiliar para publicar um pedido de fala no barramento.
        """
        bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": texto}))

    def abrir(self, nome_falado):
        nome_limpo = nome_falado.lower().strip()
        
        # 1. Sites
        if nome_limpo in self.sites_favoritos:
            self._falar(f"Abrindo site {nome_limpo}")
            webbrowser.open(self.sites_favoritos[nome_limpo])
            return True

        # 2. Fuzzy Apps
        matches = difflib.get_close_matches(nome_limpo, self.lista_apps, n=1, cutoff=0.5)
        
        if matches:
            melhor_match = matches[0]
            if melhor_match == nome_limpo:
                self._falar(f"Iniciando {melhor_match}")
                app_open(melhor_match, match_closest=True, throw_error=True)
            else:
                self._falar(f"Não achei {nome_limpo}, abrindo {melhor_match}")
                app_open(melhor_match, match_closest=True, throw_error=True)
            return True
        
        self._falar(f"Não encontrei o aplicativo {nome_limpo}")
        return False

    def fechar(self, nome_app):
        # Lógica simplificada de fechar
        try:
            # Se for site, não temos como fechar via AppOpener, avisamos o usuário
            if nome_app in self.sites_favoritos:
                self._falar("Para fechar sites, diga 'Fechar Janela'.")
                return

            self._falar(f"Fechando {nome_app}")
            app_close(nome_app, match_closest=True, throw_error=True)
        except:
            pass