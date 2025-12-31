class No:
    def __init__(self,dado = None):
        self.__dado = dado
        self.__prox = None
    
    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self,dado):
        self.__dado = dado
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self,prox):
        self.__prox= prox

class Fila:
    def __init__(self):
        self.__itens =[]
    def vazia(self):
        return len(self.__itens) == 0
    def primeiro(self):
        if(self.vazia()):
            return None
        return self.__itens[0]
    def inserir(self,item):
        self.__itens.append(item)
    def remover(self):
        if(self.vazia()):
            return None
        return self.__itens.pop(0)


class Pilha:
    def __init__(self):
        self.__itens =[]
    def vazia(self):
        return len(self.__itens) == 0
    def topo(self):
        if(self.vazia()):
            return None
        return self.__itens[-1]
    def empilhar(self,item):
        self.__itens.append(item)
    def desempilhar(self):
        if(self.vazia()):
            return None
        return self.__itens.pop()


def inverter_fila(fila_original: Fila):

    pilha_a = Pilha()
    
    while not fila_original.vazia():
        item = fila_original.remover()
        pilha_a.empilhar(item)
        
    while not pilha_a.vazia():
        item = pilha_a.desempilhar()
        fila_original.inserir(item)