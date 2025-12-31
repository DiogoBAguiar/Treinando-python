class Conta_Corrente:
    def __init__(self, nome_titular: str, numero: int, saldo: int = 0):
        self.__nome_titular = nome_titular
        self.__numero = numero
        self.__saldo = saldo
    
    def get_numero(self) -> int:
        return self.__numero
    
    def get_nome_titular(self) -> str:
        return self.__nome_titular
    def get_saldo(self) -> int:
        return self.__saldo
    def depositar(self, valor: int) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            print(f"ERRO: Valor de depósito R$ {valor/100:.2f} inválido para conta {self.__numero}.")
            return False
            
    def sacar(self, valor: int) -> bool:
        if valor <= 0:
            print(f"ERRO: Valor de saque R$ {valor/100:.2f} inválido para conta {self.__numero}.")
            return False
            
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

class Banco:

    def __init__(self):
        self.__lista_contas = []

    def __buscar_conta(self, numero_conta: int) -> Conta_Corrente | None:

        for conta in self.__lista_contas:
            if conta.get_numero() == numero_conta:
                return conta
        return None

    def adicionar_conta(self, conta: Conta_Corrente):
 
        if self.__buscar_conta(conta.get_numero()):
            print(f"ERRO: A conta número {conta.get_numero()} já existe.")
        else:
            self.__lista_contas.append(conta)
            print(f"Conta {conta.get_numero()} (Titular: {conta.get_nome_titular()}) adicionada ao banco.")

    def remove_conta(self, numero: int):

        conta = self.__buscar_conta(numero)
        if conta:
            self.__lista_contas.remove(conta)
            print(f"Conta {numero} removida com sucesso.")
        else:
            print(f"ERRO: Conta {numero} não encontrada para remoção.")

    def depositar(self, numero_conta: int, valor: int):
 
        conta = self.__buscar_conta(numero_conta)
        if conta:
            if conta.depositar(valor):
                print(f"Depósito de R$ {valor/100:.2f} na conta {numero_conta} realizado.")
        else:
            print(f"ERRO: Conta {numero_conta} não encontrada para depósito.")

    def sacar(self, numero_conta: int, valor: int):
 
        conta = self.__buscar_conta(numero_conta)
        if conta:
            sucesso = conta.sacar(valor)
            if sucesso:
                print(f"Saque de R$ {valor/100:.2f} na conta {numero_conta} realizado.")
            else:
                if valor > 0:
                    print(f"ERRO: Saldo insuficiente na conta {numero_conta}.")
        else:
            print(f"ERRO: Conta {numero_conta} não encontrada para saque.")

    def transferir(self, num_conta_origem: int, num_conta_destino: int, valor: int):

        if valor <= 0:
            print("ERRO: Valor de transferência deve ser positivo.")
            return
            
        conta_origem = self.__buscar_conta(num_conta_origem)
        conta_destino = self.__buscar_conta(num_conta_destino)

        if not conta_origem:
            print(f"ERRO: Conta de origem {num_conta_origem} não existe.")
            return
        if not conta_destino:
            print(f"ERRO: Conta de destino {num_conta_destino} não existe.")
            return
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de R$ {valor/100:.2f} da conta {num_conta_origem} para {num_conta_destino} realizada.")
        else:
            print(f"ERRO: Transferência falhou (saldo insuficiente na conta {num_conta_origem}).")

    def somar_saldos(self) -> int:
        
        soma_total = 0
        for conta in self.__lista_contas:
            soma_total += conta.get_saldo()
        return soma_total

    def exibir_saldo(self, numero_conta: int):
        
        conta = self.__buscar_conta(numero_conta)
        if conta:
            saldo_reais = conta.get_saldo() / 100.0
            print(f"--- Saldo Conta {numero_conta} (Titular: {conta.get_nome_titular()}) ---")
            print(f"Saldo atual: R$ {saldo_reais:.2f}")
        else:
            print(f"ERRO: Conta {numero_conta} não encontrada.")
            
def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("ERRO: Por favor, digite um número inteiro válido.")

def ler_float(mensagem: str) -> float:

    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("ERRO: Por favor, digite um valor numérico válido (ex: 100.50).")


if __name__ == "__main__":
    print("--- Iniciando Simulação Bancária ---")

    meu_banco = Banco()
    conta1 = Conta_Corrente("Diogo Bruno", 101, 10000) 
    conta2 = Conta_Corrente("Maria Silva", 102, 5000)
    conta3 = Conta_Corrente("João Souza", 103) 
    meu_banco.adicionar_conta(conta1)
    meu_banco.adicionar_conta(conta2)
    meu_banco.adicionar_conta(conta3)
    print("\n--- Testando Adição Duplicada ---")
    conta_duplicada = Conta_Corrente("Teste Duplicado", 101, 500)
    meu_banco.adicionar_conta(conta_duplicada)
    print("\n--- Realizando Operações ---")
    meu_banco.depositar(101, 2000)
    meu_banco.exibir_saldo(101) 
    meu_banco.sacar(102, 1000)
    meu_banco.exibir_saldo(102) 
    meu_banco.transferir(101, 103, 1500)
    meu_banco.exibir_saldo(101) 
    meu_banco.exibir_saldo(103) 
    print("\n--- Testando Falhas Esperadas ---")
    meu_banco.sacar(101, -500)
    meu_banco.sacar(103, 2000) 
    meu_banco.transferir(999, 101, 100)
    meu_banco.transferir(101, 888, 100)
    print("\n--- Verificando Saldo Total ---")
    saldo_total_centavos = meu_banco.somar_saldos()
    print(f"Saldo total em todas as contas do banco: R$ {saldo_total_centavos / 100.0:.2f}")
    print("\n--- Removendo Conta ---")
    meu_banco.remove_conta(102)
    meu_banco.exibir_saldo(102) 
    
    saldo_total_centavos = meu_banco.somar_saldos()
    print(f"Novo saldo total do banco (após remoção): R$ {saldo_total_centavos / 100.0:.2f}")
    print("\n--- Fim da Simulação ---")
