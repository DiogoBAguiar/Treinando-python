class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def calcular_diagonal(self):
        return (self.largura**2 + self.altura**2) ** 0.5
    def mostrar_info(self):
        print(f"Largura: {self.largura}, Altura: {self.altura}, Area: {self.calcular_area()}, Perimetro: {self.calcular_perimetro()}, Diagonal: {self.calcular_diagonal()}")
    def eh_quadrado(self):
        if self.largura == self.altura:
            return True
        else:
            return False

class Aluno:
    def __init__(self,nome,idade,notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas)/len(self.notas)
    def frequencia(self, presencas, total_aulas):
        return (presencas/total_aulas)*100
    def qtd_aprovacoes(self):
        return len([nota for nota in self.notas if nota >= 60])
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Media: {self.calcular_media()}, Aprovacoes: {self.qtd_aprovacoes()}")

class Conta_Corrente:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor      
    
    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
    
    def mostrar_info(self):
        print(f"Conta: {self.numero_conta}, Titular: {self.titular}, Saldo: {self.saldo}")   

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def Quadrante(self):
        if self.x > 0 and self.y > 0:
            return "Q1"
        elif self.x < 0 and self.y > 0:
            return "Q2"
        elif self.x < 0 and self.y < 0:
            return "Q3"
        elif self.x > 0 and self.y < 0:
            return "Q4"
        elif self.x == 0 and self.y != 0:
            return "Eixo Y"
        elif self.y == 0 and self.x != 0:
            return "Eixo X"
        else:
            return "Origem"

valor01= Conta_Corrente(3000)
