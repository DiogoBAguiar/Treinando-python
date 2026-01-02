import logging
from typing import Dict, Any, Optional

# Import de Configuração
from config import MAPA_NUMEROS

# Imports da Arquitetura de Eventos
from core.event_bus import bus, Evento
from core.definitions import Eventos

class Processador:
    """
    Unidade de Processamento Lógico (NLU Simples).
    Analisa o texto recebido e decide qual evento disparar.
    Atua como um 'Roteador' entre a Voz e as Funcionalidades.
    """
    def __init__(self):
        # Estado inicial do assistente
        self._ativo: bool = True
        
        # Inscreve-se para receber transcrições de áudio
        bus.inscrever(Eventos.VOZ_RECONHECIDA, self._processar_intencao)
        
        # Notifica o sistema que o cérebro está online
        bus.publicar(Evento(Eventos.LOG_SISTEMA, {"nivel": "INFO", "msg": "Processador Lógico Iniciado", "origem": "Processador"}))
        # Feedback visual inicial
        bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "🟢 Online"}))

    def _normalizar_comando(self, texto_bruto: str) -> str:
        """
        Limpa e corrige o texto recebido para facilitar o reconhecimento.
        Corrige nomes que o Vosk entende errado (Ex: 'Jacques' -> 'Jarvis').
        """
        texto = texto_bruto.lower().strip()
        
        # Dicionário de correções fonéticas (O que ele ouviu -> O que deveria ser)
        correcoes = {
            # Variações do Nome do Assistente
            "james": "jarvis",
            "jacques": "jarvis",
            "javes": "jarvis",
            "chaves": "jarvis",
            "jarbas": "jarvis",
            "chave": "jarvis",
            "já fiz": "jarvis",
            "já lhes": "jarvis",  # <--- SEU ERRO CORRIGIDO
            "já a": "jarvis",     # <--- SEU ERRO CORRIGIDO
            "já lhe": "jarvis",
            "já vi": "jarvis",    # Erro comum também
            "já fiz": "jarvis",
            
            # Variações do ChatGPT
            "chatos o peter": "chat gpt",
            "chat o peter": "chat gpt",
            "tati pt": "chat gpt",
            "tati petê": "chat gpt",
            "chat gepetê": "chat gpt",
            "chat pt": "chat gpt",
            
            # Verbos comuns que o Vosk erra
            "abri ": "abrir ",
            "abre ": "abrir "
        }

        for errado, correto in correcoes.items():
            if errado in texto:
                texto = texto.replace(errado, correto)
        
        return texto

    def _processar_intencao(self, evento: Evento) -> None:
        """
        Callback principal. Recebe o texto, decide o que fazer e publica a ordem.
        """
        texto_original = evento.dados.get("texto", "")
        if not texto_original:
            return

        texto = self._normalizar_comando(texto_original)
        
        # Loga apenas se for algo relevante
        if len(texto) > 2:
            logging.debug(f"[Processador] Analisando: '{texto}' (Estado: {'Ativo' if self._ativo else 'Dormindo'})")

        # =====================================================================
        # 1. CONTROLE DE ESTADO (Prioridade Máxima)
        # =====================================================================
        
        # Acordar
        # Agora "já lhes acordar" vira "jarvis acordar" antes de chegar aqui
        if "jarvis acordar" in texto or texto == "acordar":
            self._ativo = True
            bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": "Estou aqui."}))
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "🟢 Ativo"}))
            return

        # Dormir
        if "jarvis dormir" in texto or texto == "dormir":
            self._ativo = False
            bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": "Entrando em espera."}))
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_STATUS, {"texto": "💤 Dormindo"}))
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_GRADE, {"estado": "ocultar"}))
            return

        # Comandos de Encerramento (Kill Switch)
        if self._ativo and texto in ["encerrar sistema", "desligar assistente", "tchau jarvis"]:
            bus.publicar(Evento(Eventos.CMD_FALAR, {"texto": "Desligando sistemas. Até logo."}))
            bus.publicar(Evento(Eventos.CMD_SISTEMA, {"acao": "desligar"}))
            return

        # Se estiver dormindo, ignora qualquer outro comando
        if not self._ativo:
            return

        # =====================================================================
        # 2. ROTEAMENTO DE COMANDOS
        # =====================================================================

        # --- APLICATIVOS ---
        if texto.startswith("abrir "):
            nome_app = texto.replace("abrir ", "").strip()
            bus.publicar(Evento(Eventos.CMD_APP, {"acao": "abrir", "nome": nome_app}))
            return

        elif texto.startswith("fechar "):
            nome_app = texto.replace("fechar ", "").strip()
            if "programa" not in nome_app and "sistema" not in nome_app:
                bus.publicar(Evento(Eventos.CMD_APP, {"acao": "fechar", "nome": nome_app}))
            return

        # --- MOUSE (Cliques e Grade) ---
        if "grade" in texto:
            acao = "ocultar" if ("ocultar" in texto or "sair" in texto) else "mostrar"
            bus.publicar(Evento(Eventos.UI_ATUALIZAR_GRADE, {"estado": acao}))
            return
        
        if "zerar" in texto or "limpar" in texto:
             bus.publicar(Evento(Eventos.UI_ATUALIZAR_GRADE, {"estado": "ocultar"}))
             return

        if "clicar" in texto:
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "clique"}))
            return
            
        if "duplo" in texto:
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "duplo"}))
            return
            
        if "direita" in texto:
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "direita"}))
            return

        if "rolar" in texto:
            direcao = "baixo" if "baixo" in texto else "cima"
            bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "rolar", "direcao": direcao}))
            return

        # Navegação por Grade (Números)
        for palavra_num, valor_int in MAPA_NUMEROS.items():
            if palavra_num in texto:
                bus.publicar(Evento(Eventos.CMD_MOUSE, {"tipo": "mover_setor", "setor": valor_int}))
                return

        # --- TECLADO ---
        if "selecionar tudo" in texto:
            bus.publicar(Evento(Eventos.CMD_TECLADO, {"acao": "atalho", "dados": "ctrl+a"}))
            return
            
        if "copiar" in texto:
            bus.publicar(Evento(Eventos.CMD_TECLADO, {"acao": "atalho", "dados": "ctrl+c"}))
            return
            
        if "colar" in texto:
            bus.publicar(Evento(Eventos.CMD_TECLADO, {"acao": "atalho", "dados": "ctrl+v"}))
            return
            
        if "enter" in texto:
            bus.publicar(Evento(Eventos.CMD_TECLADO, {"acao": "atalho", "dados": "enter"}))
            return

        if texto.startswith("escrever ") or texto.startswith("digitar "):
            mensagem = texto.replace("escrever ", "").replace("digitar ", "")
            bus.publicar(Evento(Eventos.CMD_TECLADO, {"acao": "escrever", "dados": mensagem}))
            return