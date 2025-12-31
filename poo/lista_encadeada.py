class No:
    def __init__(self,dado = None):
        self.__dado = dado
        self.__prox = None
    
    @property
    def dado(self):
        return self.__dado
    
    @dado.setter
    def dado(self, novo):
        self.__dado = novo
    
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, novo):
        self.__prox = novo
    
class Lista_Encadeada:
    def __init__(self):
         self.__inicio = []
    def inserir_inicio(self, no):
        pass
    def inserir_meio(self, posicao , no):
        pass
    def inserir_fim(self, no):
        pass
    def remover_inicio(self,no):
        pass
    def remover_meio(self,posicao,no):
        pass
    def remover_fim(self,no):
        pass
    def tamanho(self):
        p = self.__inicio

        tamanho = 0
        while p != None:
            tamanho += 1
            p = p.prox
            return tamanho

    def __str__(self):
        saida = 'Lista: ['
        p = self.__inicio

        while p != None:
        saida += f'{p.dado}'
        p = p.prox

        if p != None:
            saida += ', '

        saida += ']'
        return saida 
    
class Lista_Encadeada_v2:

  def __init__(self):
    self.__inicio = []

  def inserir(self, pos, no):
    pass

  def remover(self, pos, no):
    pass
  def consultar(self, pos):
    if self.__inicio == None:
        return None
    else :
        if pos <= 0:
            return self.__inicio
        else:
            if pos > self.tamanho():
                p = self.__inicio
                while p.prox != None:
                    p = p.prox
                return p
            else:
                p = self.__inicio
                q = None
                
                for i in range(pos):
                    q = p
                    p = p.prox
                
                return q        

  def tamanho(self):
    p = self.__inicio

    tamanho = 0
    while p != None:
      tamanho += 1
      p = p.prox
    return tamanho

  def __str__(self):
    saida = 'Lista: ['
    p = self.__inicio

    while p != None:
      saida += f'{p.dado}'
      p = p.prox

      if p != None:
        saida += ', '

    saida += ']'
    return saida

if __name__ == '__main__':

  p = Lista_Encadeada()                       