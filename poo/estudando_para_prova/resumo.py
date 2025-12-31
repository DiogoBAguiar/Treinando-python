# --- 1. CLASSES DE ESTRUTURAS DE DADOS ---

class No:
    """ Classe Nó (com getters/setters) [cite: 418-421] """
    def __init__(self, dado=None , proximo = None):
        self.__dado = dado
        self.__proximo = proximo
    def get_dado(self): return self.__dado
    def get_proximo(self): return self.__proximo
    def set_dado(self, novo_dado): self.__dado = novo_dado
    def set_proximo(self, novo_proximo): self.__proximo = novo_proximo
    def __str__(self): return str(self.__dado)

class PilhaException(Exception): pass
class FilaException(Exception): pass

class Pilha:
    """ Classe Pilha Encadeada (baseada na PRÁTICA 2) [cite: 438-440, 479-488, 523-526] """
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        
    def estaVazia(self) -> bool: return self.__tamanho == 0
    def tamanho(self) -> int: return self.__tamanho
        
    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.set_proximo(self.__topo)
        self.__topo = novo_no
        self.__tamanho += 1
        
    def desempilhar(self):
        if self.estaVazia(): raise PilhaException("Pilha Vazia")
        dado_removido = self.__topo.get_dado()
        self.__topo = self.__topo.get_proximo()
        self.__tamanho -= 1
        return dado_removido
        
    def topo(self):
        if self.estaVazia(): raise PilhaException("Pilha Vazia")
        return self.__topo.get_dado()
        
    def __str__(self) -> str:
        if self.estaVazia(): return "Pilha: []"
        s = "Pilha: [ (topo) "
        no_atual = self.__topo
        while no_atual is not None:
            s += f"{no_atual.get_dado()} -> "
            no_atual = no_atual.get_proximo()
        s += "None (base) ]"
        return s

    def trocar_ocorrencias(self, valor_antigo, valor_novo):
        """ Método da Questão 2 (Trocar Ocorrências) """
        pilha_aux = Pilha()
        while not self.estaVazia():
            try:
                item = self.desempilhar()
                if item == valor_antigo:
                    pilha_aux.empilhar(valor_novo)
                else:
                    pilha_aux.empilhar(item)
            except PilhaException: pass 
        while not pilha_aux.estaVazia():
            try:
                self.empilhar(pilha_aux.desempilhar())
            except PilhaException: pass

class Fila:
    """ Classe Fila Encadeada (baseada na PRÁTICA 3) [cite: 1969-2048] """
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def estaVazia(self) -> bool: return self.__tamanho == 0
    def tamanho(self) -> int: return self.__tamanho

    def adicionar(self, valor):
        novo_no = No(valor)
        novo_no.set_proximo(None) 
        if self.estaVazia(): self.__inicio = novo_no
        else:
            p = self.__inicio
            while p.get_proximo() is not None:
                p = p.get_proximo()
            p.set_proximo(novo_no)
        self.__tamanho += 1

    def remover(self):
        if self.estaVazia(): raise FilaException("Fila Vazia")
        dado_removido = self.__inicio.get_dado()
        self.__inicio = self.__inicio.get_proximo()
        self.__tamanho -= 1
        return dado_removido
        
    def primeiro(self):
        if self.estaVazia(): raise FilaException("Fila Vazia")
        return self.__inicio.get_dado()

    def __str__(self) -> str:
        if self.estaVazia(): return "Fila: [Vazia]"
        s = "Fila: [ (frente) "
        no_atual = self.__inicio
        while no_atual is not None:
            s += f"{no_atual.get_dado()} -> "
            no_atual = no_atual.get_proximo()
        s += "None (trás) ]"
        return s

class Lista:
    """ Classe Lista Encadeada (baseada em Exercícios - Listas) [cite: 857-871] """
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0
    
    def estaVazia(self) -> bool: return self.__tamanho == 0
    def tamanho(self) -> int: return self.__tamanho
    
    def inserir_final(self, valor):
        novo_no = No(valor)
        novo_no.set_proximo(None) 
        if self.estaVazia():
            self.__inicio = novo_no
        else:
            p = self.__inicio
            while p.get_proximo() is not None:
                p = p.get_proximo()
            p.set_proximo(novo_no)
        self.__tamanho += 1
            
    def __str__(self) -> str:
        if self.estaVazia(): return "Lista: []"
        s = "Lista: [ (início) "
        no_atual = self.__inicio
        while no_atual is not None:
            s += f"{no_atual.get_dado()} -> "
            no_atual = no_atual.get_proximo()
        s += "None (fim) ]"
        return s

    def contar_ocorrencias(self, valor) -> int:
        """ Método da Questão 3 (Contar Ocorrências) """
        contador = 0
        no_atual = self.__inicio
        while no_atual is not None:
            if no_atual.get_dado() == valor:
                contador += 1
            no_atual = no_atual.get_proximo()
        return contador


class Operacoes:
    
    @staticmethod
    def inverter_fila(fila_para_inverter: Fila):

        pilha_aux = Pilha()
        print(f"Invertendo... {fila_para_inverter}")
        try:
            while not fila_para_inverter.estaVazia():
                item = fila_para_inverter.remover() 
                pilha_aux.empilhar(item) 
        except FilaException: pass 
        
        print(f"Pilha auxiliar agora: {pilha_aux}")
        
        try:
            while not pilha_aux.estaVazia():
                item = pilha_aux.desempilhar() 
                fila_para_inverter.adicionar(item) 
        except PilhaException: pass 
        print(f"Fila invertida: {fila_para_inverter}")

    @staticmethod
    def potencia(x: float, n: int) -> float:

        if n == 0:
            return 1.0  
        else:
            return x * Operacoes.potencia(x, n - 1) # Chama a si mesma (estática)

    @staticmethod
    def fibonacci(n: int) -> int:

        if n == 1:
            return 0 
        elif n == 2:
            return 1 
        else:
            return Operacoes.fibonacci(n - 1) + Operacoes.fibonacci(n - 2)

    @staticmethod
    def soma_lista_recursiva(lista_nums: list) -> float:
       
        if len(lista_nums) == 0:
            return 0
        else:
            primeiro_elemento = lista_nums[0]
            resto_da_lista = lista_nums[1:] 
            return primeiro_elemento + Operacoes.soma_lista_recursiva(resto_da_lista)

    @staticmethod
    def contar_brancos_recursiva(texto: str) -> int:
       
        if len(texto) == 0:
            return 0
        else:
            primeiro_char = texto[0]
            resto_da_string = texto[1:]
            if primeiro_char == ' ':
                return 1 + Operacoes.contar_brancos_recursiva(resto_da_string)
            else:
                return Operacoes.contar_brancos_recursiva(resto_da_string)