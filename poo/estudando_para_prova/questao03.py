class Pais:
    def __init__(self,nome:str,capital: str,dimensao:float ):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteiras = []
    
    def get_nome(self) -> str:
        return self.__nome
    def get_capital(self) -> str:
        return self.__capital
    def get_dimensao(self) -> float:
        return self.__dimensao
    def get_fronteiras(self) -> str:
        return self.__fronteiras
    
    def set_nome(self,nome:str):
        self.__nome = nome
    def set_capital(self,capital:str):
        self.__capital = capital
    def set_dimensao(self,dimensao:str):
        self.__dimensao = dimensao
    def adicionar_fronteira(self,nome_pais: str):
        if nome_pais not in self.__fronteiras:
            self.__fronteiras.append(nome_pais)
            return f"Adionado {nome_pais} a fronteira de {self.__nome}." 
        else:
            return f"{nome_pais} já existe na lista da fronteira de {self.__nome}."
    def __str__(self):
        return f"País:{self.__nome}\nCapital:{self.__capital}\nDimensão:{self.__dimensao}km²"

brasil = Pais("Brasil","Brasília",8515767.0)
print(brasil)
print(f"Get_nome: {brasil.get_nome()}")
print(f"Get_capital: {brasil.get_capital()}")
print(f"Get_dimensao: {brasil.get_dimensao()}")
print(f"Get_fronteiras: {brasil.get_fronteiras()}")

print(brasil.adicionar_fronteira("Argentina"))
brasil.adicionar_fronteira("Uruguai")
brasil.adicionar_fronteira("Paraguai")
brasil.adicionar_fronteira("Bolivia")

print(brasil.adicionar_fronteira("Argentina"))

print(brasil.get_fronteiras())