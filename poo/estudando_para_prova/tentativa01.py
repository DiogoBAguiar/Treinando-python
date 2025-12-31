class PilhaException(Exception):
    pass
class FilaException(Exception):
    pass
class No:
    def __init__ (self,dado=None):
        self.__dado = dado
        self.__proximo = None
    @property
    def dado (self):
        return self.__dado
    @property
    def proximo (self):
        return self.__proximo
    
    @dado.setter
    def dado(self ,novo): 
        self.__dado = novo
    @proximo.setter
    def proximo(self ,novo): 
        self.__proximo = novo
        
    
    