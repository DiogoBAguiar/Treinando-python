class Pilha:
    def __init__(self):
          self._itens = []
    
    def verificacao_vazio (self):
        return len(self._itens)==0
    
    def empilhar (self,item):
        self._itens.append(item)
    
    """def __str__(self):
         p = self._topo
         msg=""
         while (p!=None):
             msg += p.dado
             p = p.prox
        return msg"""

class fila:
    def __init__(self,inicio,fim):
        self.inicio = inicio
        self.fim = fim
    def enfileirar(self,item):
        self.fim+=1
        self.item[self.fim]=item    
                