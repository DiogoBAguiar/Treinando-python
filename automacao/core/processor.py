# core/processor.py
import logging
from config import MAPA_NUMEROS
from core.definitions import Eventos
from core.event_bus import bus, Evento

class Processador:
    def __init__(self):
        """
        O Processador agora é puramente LÓGICO.
        Ele não tem mais 'braços' (self.mouse) nem 'boca' (self.voz).
        Ele apenas escuta a Voz Reconhecida e Publica Ordens.
        """
        # 1. Se inscreve para ouvir o reconhecimento de voz
        bus.inscrever(Eventos.VOZ_RECONHECIDA, self.processar_voz)
        
        # Publica que o sistema iniciou (quem estiver ouvindo, que reaja)
        bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "🟢 Online"}))
        bus.publicar(Evento(Eventos.LOG_SISTEMA, {"msg": "Processador de Eventos Iniciado"}))
        
        self.ativo = True

    def _normalizar(self, texto):
        # (Sua lógica de normalização fonética continua aqui - mantive resumida)
        erros = {"jacques": "jarvis", "chaves": "jarvis", "tati pt": "chat gpt"}
        for erro, corr in erros.items():
            if erro in texto: texto = texto.replace(erro, corr)
        return texto

    def processar_voz(self, evento):
        """
        Callback disparado automaticamente quando o Event Bus recebe VOZ_RECONHECIDA.
        """
        texto_bruto = evento.dados.get("texto", "")
        texto = self._normalizar(texto_bruto.lower().strip())
        
        logging.info(f"[Processador] Analisando: {texto}")

        # --- LÓGICA DE ESTADO (Acordar/Dormir) ---
        if "acordar" in texto:
            self.ativo = True
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "🟢 Ativo"}))
            # O processador não fala mais diretamente. Ele pede pro sistema falar.
            # (Ainda não criamos o ouvinte de voz, faremos no próximo passo)
            return

        if "dormir" in texto:
            self.ativo = False
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "💤 Dormindo"}))
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_GRADE, {"estado": "ocultar"}))
            return

        if not self.ativo:
            return

        # --- DECISÃO DE COMANDOS (Publicação de Eventos) ---
        
        # 1. Sistema
        if texto in ["tchau jarvis", "encerrar sistema"]:
            bus.publicar(Evento(Eventos.CMD_SISTEMA, {"acao": "desligar"}))
            return

        # 2. Apps
        if texto.startswith("abrir "):
            nome = texto.replace("abrir ", "").strip()
            # Em vez de self.apps.abrir(nome), publicamos o desejo:
            bus.publicar(Evento(Eventos.CMD_APP, {"acao": "abrir", "nome": nome}))
            
        elif texto.startswith("fechar "):
            nome = texto.replace("fechar ", "").strip()
            bus.publicar(Evento(Eventos.CMD_APP, {"acao": "fechar", "nome": nome}))

        # 3. Mouse
        elif "clicar" in texto:
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "clique"}))
        elif "direita" in texto:
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "direita"}))
        elif "grade" in texto:
            estado = "ocultar" if "ocultar" in texto else "mostrar"
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_GRADE, {"estado": estado}))
            
        # 4. Navegação Numérica
        for nome_num, valor_int in MAPA_NUMEROS.items():
            if nome_num in texto:
                bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "mover_setor", "setor": valor_int}))
                break