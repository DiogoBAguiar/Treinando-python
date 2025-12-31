class Conta_corrente :
    def __init__(self, numero , cpf , saldo = 0):
        self.numero = numero
        self.cpf = cpf 
        self.saldo = saldo
    
    def creditar(self, valor):
        self.saldo += valor
    
    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
    
    if __name__ == '__main__':
        minha_conta = Conta_corrente("1234-5","876543212",150)
        
        minha_conta.creditar(100)   
        minha_conta.debitar(80)
        
        print(f"O")             