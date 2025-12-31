class Data:

    #-------Construtor da class data--------*

    def __init__(self,dia:int,mes:int,ano:int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    #--------Metodos Acessadores-------------*
    def get_dia(self) -> int:
        return self.__dia
    def get_mes(self) -> int:
        return self.__mes
    def get_ano(self) -> int:
        return self.__ano
    
    #--------Metodos Modificadores-------------*
    def set_dia(self,dia: int):
        if 1 <= dia <= 31:
            self.__dia = dia
    def set_mes(self,mes: int):
        if 1 <= mes <= 12:
            self.__mes = mes 
    def set_ano(self,ano: int):
            self.__ano = ano
    #--------Metodos  String-------------*
    def __str__(self) -> str:
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}"  
    
    


data_aniversario = Data(10, 5, 2000)

print(f"{data_aniversario}")
print(f"{data_aniversario.get_dia()}")
print(f"{data_aniversario.get_mes()}")
print(f"{data_aniversario.get_ano()}")
print(f"{data_aniversario}")
data_aniversario.set_dia(25)
data_aniversario.set_mes(12)
data_aniversario.set_ano(2025)
print(f"Data após a modificação: {data_aniversario}")                           