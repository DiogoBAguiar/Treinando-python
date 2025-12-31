#Sem Poo
carros = []
def adicionar_carro(marca,modelo,ano):
    carro = {"marca":marca,"modelo":modelo,"ano":ano}
    carros.append(carro)

def mostrar_carros():
    for carro in carros:
        print(f"{carro['marca']} {carro['modelo']} {carro['ano']}")

adicionar_carro("Toyota","Corolla",2020)
adicionar_carro("Honda","Civic",2019)

mostrar_carros()

#Com Poo

class Carro:
    def __init__(self,marca,modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
    
    def mostrar_info(self):
        print(f"{self.marca} {self.modelo} {self.ano}")

carro1 = Carro("Toyota","Corolla",2020)
carro2 = Carro("Honda","Civic",2019)

carro1.mostrar_info()
carro2.mostrar_info()                        