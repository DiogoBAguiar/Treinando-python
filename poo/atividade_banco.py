class Conta_Corrente:
    def __init__(self,nome,saldo=0):
        self._nome = nome
        self._saldo = saldo
    
    @property
    def nome(self):
        return self._nome
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self,valor):
        if valor > 0 :
            self._saldo += valor
            return True
        else:
            return False
    
    def debitar(self,valor):
        if self._saldo - valor == 0  or self._saldo - valor >= 0 :
            self._saldo -= valor 
            return True
        else:
            return False
    
    def transferir(self,valor, conta_destino):
        if not isinstance(conta_destino, Conta_Corrente):
            return
        
        if self.debitar(valor):
            conta_destino.depositar(valor)
                  
conta_diogo = Conta_Corrente("Diogo Aguiar", 1500)
conta_ana = Conta_Corrente("Ana Silva", 500)

print(f"Saldo inicial de {conta_diogo.nome}: R$ {conta_diogo.saldo:.2f}")
print(f"Saldo inicial de {conta_ana.nome}: R$ {conta_ana.saldo:.2f}")
print("-" * 30)
print("Realizando transferência de R$ 300 de Diogo para Ana...")
conta_diogo.transferir(300, conta_ana)
print(f"\nSaldo final de {conta_diogo.nome}: R$ {conta_diogo.saldo:.2f}")
print(f"Saldo final de {conta_ana.nome}: R$ {conta_ana.saldo:.2f}")  
print("-" * 30)
print("Tentando transferir R$ 2000 de Ana para Diogo...")
conta_ana.transferir(2000, conta_diogo)
print(f"\nSaldo de {conta_diogo.nome} (inalterado): R$ {conta_diogo.saldo:.2f}") 
print(f"Saldo de {conta_ana.nome} (inalterado): R$ {conta_ana.saldo:.2f}")   