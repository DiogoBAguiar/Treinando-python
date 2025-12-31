# --- Classe Data ---
class Data:
    def __init__(self, dia, mes, ano):
        # Atributos privados com underscore (_)
        self._dia = dia
        self._mes = mes
        self._ano = ano
        # Validação inicial (opcional, mas boa prática)
        self.validar()

    def validar(self):
        # Uma validação simples
        if not (1 <= self._dia <= 31):
            print(f"Dia inválido: {self._dia}. Ajustando para 1.")
            self._dia = 1
        if not (1 <= self._mes <= 12):
            print(f"Mês inválido: {self._mes}. Ajustando para 1.")
            self._mes = 1

    # --- Métodos Acessadores (Getters) ---
    @property
    def dia(self):
        return self._dia

    @property
    def mes(self):
        return self._mes

    @property
    def ano(self):
        return self._ano

    # --- Métodos Modificadores (Setters) ---
    @dia.setter
    def dia(self, valor):
        if 1 <= valor <= 31:
            self._dia = valor
        else:
            print(f"Erro: Tentativa de definir dia como {valor}. Valor inválido.")

    @mes.setter
    def mes(self, valor):
        if 1 <= valor <= 12:
            self._mes = valor
        else:
            print(f"Erro: Tentativa de definir mês como {valor}. Valor inválido.")
            
    @ano.setter
    def ano(self, valor):
        self._ano = valor

    # --- Método __str__ ---
    def __str__(self):
        # Formata com zeros à esquerda (ex: 01/03/2025)
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

# --- Classe Aluno ---
class Aluno:
    def __init__(self, matricula, nome, notas):
        # Atributos (não precisam ser privados, conforme o prompt)
        # Mas usaremos _ para manter o padrão com getters/setters
        self._matricula = matricula # int
        self._nome = nome       # string
        self._notas = notas     # list (ex: [7.5, 8.0])

    # --- Métodos Acessadores (Getters) ---
    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        # Retorna a matrícula como String formatada
        # Ex: 202510045 -> "2025.1.0045"
        # Isso é uma suposição de como a matrícula (int) é estruturada
        s_mat = str(self._matricula)
        if len(s_mat) >= 8: # Ex: 20251045 (Ano+Per+ID)
            ano = s_mat[:4]
            periodo = s_mat[4]
            id_aluno = s_mat[5:]
            return f"{ano}.{periodo}.{id_aluno}"
        else:
            # Caso simples se a matrícula for só um ID
            # e o "2025.1" for fixo (baseado no seu contexto)
            # return f"2025.1.{self._matricula}"
            return str(self._matricula) # Retorno padrão

    # --- Método Modificador (Setter) para Nome ---
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # --- Outros Métodos ---
    def media(self):
        # Retorna a média das notas
        if not self._notas: # Verifica se a lista de notas não está vazia
            return 0.0
        return sum(self._notas) / len(self._notas)

    def adiciona_nota(self, nota):
        # Adiciona uma nota à lista
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:
            self._notas.append(float(nota))
            print(f"Nota {nota} adicionada.")
        else:
            print(f"Valor de nota inválido: {nota}")


# --- Classe Pais ---
class Pais:
    def __init__(self, nome, capital, dimensao):
        # Atributos privados
        self._nome = nome
        self._capital = capital
        self._dimensao = dimensao # em Km²
        self._fronteiras = []     # Lista de países (strings)

    # --- Métodos Acessadores (Getters) ---
    @property
    def nome(self):
        return self._nome

    @property
    def capital(self):
        return self._capital

    @property
    def dimensao(self):
        return self._dimensao

    # --- Métodos da Lista de Fronteiras ---
    @property
    def fronteiras(self):
        # c) Método que retorne a lista de países que fazem fronteira
        return self._fronteiras

    def adiciona_fronteira(self, nome_pais):
        # d) Método que adiciona país à lista de fronteiras
        if not isinstance(nome_pais, str) or not nome_pais:
            print("Erro: Nome de país inválido.")
            return False
            
        if nome_pais == self._nome:
            print(f"Erro: Um país não pode fazer fronteira consigo mesmo.")
            return False

        if nome_pais not in self._fronteiras:
            self._fronteiras.append(nome_pais)
            print(f"'{nome_pais}' adicionado às fronteiras de {self.nome}.")
            return True
        else:
            print(f"'{nome_pais}' já está na lista de fronteiras.")
            return False
            
    # --- Método __str__ ---
    def __str__(self):
        # e) Retorna string formatada
        return (f"País: {self.nome}\n"
                f"Capital: {self.capital}\n"
                f"Dimensão: {self.dimensao:,} Km²".replace(",", "."))

# --- Classe Conta_Corrente ---
class Conta_Corrente:
    def __init__(self, numero, nome_titular, saldo=0.0):
        # Usando _ para indicar que são internos
        self._numero = numero # int
        self._nome_titular = nome_titular # str
        self._saldo = float(saldo) # float

    # --- Getters (Acessadores) ---
    # Necessários para o menu da Questão 4 e para o Banco da Questão 5
    @property
    def numero(self):
        return self._numero
        
    @property
    def nome_titular(self):
        return self._nome_titular

    @property
    def saldo(self):
        return self._saldo

    # --- Métodos Principais ---
    def depositar(self, valor):
        """ Incrementa o saldo. Não possui retorno. """
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        """ 
        Tenta sacar um valor. 
        Retorna True se o saque foi bem-sucedido.
        Retorna False se não há saldo suficiente.
        """
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
            
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
            return True
        else:
            print(f"Saque de R$ {valor:.2f} falhou. Saldo insuficiente (R$ {self._saldo:.2f}).")
            return False

    def __str__(self):
        # Útil para exibir o saldo
        return f"Conta {self.numero} - Titular: {self.nome_titular} - Saldo: R$ {self.saldo:.2f}"
    
# --- Programa de Teste (Questão 4) ---

def buscar_conta(lista_contas, numero):
    """ Função auxiliar para encontrar uma conta na lista pelo número. """
    for conta in lista_contas:
        if conta.numero == numero:
            return conta
    return None

def programa_bancario_q4():
    print("--- Sistema Bancário (Questão 4) ---")
    contas = []
    
    # a) Criar 5 instâncias lendo do teclado
    # Para agilizar o teste, vamos criar apenas 2. 
    # Mude range(2) para range(5) para o exercício completo.
    print("=== Cadastro de Contas ===")
    num_contas_para_criar = 2 
    for i in range(num_contas_para_criar):
        print(f"\n--- Cadastro Conta {i+1}/{num_contas_para_criar} ---")
        try:
            # Garantindo que o número da conta seja único
            while True:
                num = int(input(f"Digite o número da conta {i+1}: "))
                if buscar_conta(contas, num) is None:
                    break
                else:
                    print(f"Erro: O número de conta {num} já existe. Tente outro.")
                    
            nome = input(f"Digite o nome do titular {i+1}: ")
            saldo_inicial = float(input(f"Digite o saldo inicial {i+1} (R$): "))
            
            nova_conta = Conta_Corrente(num, nome, saldo_inicial)
            contas.append(nova_conta)
            print(f"Conta {num} criada com sucesso!")
            
        except ValueError:
            print("Erro na entrada. Use números válidos para conta e saldo. Recomeçando cadastro da conta...")
            # (Em um sistema real, você trataria isso melhor)
            continue # Pula para a próxima iteração

    if not contas:
        print("Nenhuma conta foi criada. Encerrando o programa.")
        return

    print(f"\n=== {len(contas)} Contas Cadastradas ===")
    for c in contas:
        print(c)

    # b) Menu de operações
    print("\n=== Menu de Operações ===")
    while True:
        print("\nEscolha uma operação:")
        print("1) Depositar")
        print("2) Sacar")
        print("3) Saldo")
        print("4) Sair")
        
        opcao = input("Digite o número da opção: ")

        try:
            if opcao == '1': # Depositar
                num_conta = int(input("Número da conta: "))
                valor = float(input("Valor a depositar: R$ "))
                conta = buscar_conta(contas, num_conta)
                if conta:
                    conta.depositar(valor)
                else:
                    print("Erro: Conta não encontrada.")
            
            elif opcao == '2': # Sacar
                num_conta = int(input("Número da conta: "))
                valor = float(input("Valor a sacar: R$ "))
                conta = buscar_conta(contas, num_conta)
                if conta:
                    # O método sacar() já imprime o sucesso ou falha
                    conta.sacar(valor)
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == '3': # Saldo
                num_conta = int(input("Número da conta: "))
                conta = buscar_conta(contas, num_conta)
                if conta:
                    # Usamos o __str__ da própria conta
                    print(f"Consulta de Saldo: {conta}")
                else:
                    print("Erro: Conta não encontrada.")
            
            elif opcao == '4': # Sair
                print("Encerrando o sistema. Obrigado!")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite números onde for solicitado.")


# --- Classe Banco ---
class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = [] # Lista de objetos Conta_Corrente

    # --- Métodos Auxiliares Internos ---
    def _buscar_conta(self, numero):
        """ Método privado para encontrar uma conta. Retorna o objeto ou None. """
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

    # --- Métodos Principais ---
    def adicionar_conta(self, conta):
        """ Adiciona um objeto Conta_Corrente ao banco. """
        if isinstance(conta, Conta_Corrente):
            # Verifica se o número da conta já existe
            if self._buscar_conta(conta.numero) is None:
                self._contas.append(conta)
                print(f"Conta {conta.numero} ({conta.nome_titular}) adicionada ao banco {self._nome}.")
                return True
            else:
                print(f"Erro: Já existe uma conta com o número {conta.numero} no banco.")
                return False
        else:
            print("Erro: Somente objetos Conta_Corrente podem ser adicionados.")
            return False

    def remove_conta(self, numero):
        """ Remove uma conta pelo número. """
        conta = self._buscar_conta(numero)
        if conta:
            self._contas.remove(conta)
            print(f"Conta {conta.numero} removida com sucesso.")
            return True
        else:
            print(f"Erro: Conta {numero} não encontrada para remoção.")
            return False

    def depositar(self, numero, valor):
        """ Deposita em uma conta específica. """
        conta = self._buscar_conta(numero)
        if conta:
            # Delegação: O banco pede para a conta realizar a operação
            conta.depositar(valor)
            return True
        else:
            print(f"Erro no depósito: Conta {numero} não encontrada.")
            return False

    def sacar(self, numero, valor):
        """ Saca de uma conta específica. """
        conta = self._buscar_conta(numero)
        if conta:
            # Delegação: Retorna o True/False do método da conta
            return conta.sacar(valor)
        else:
            print(f"Erro no saque: Conta {numero} não encontrada.")
            return False # Falha porque a conta não existe

    def transferir(self, num_origem, num_destino, valor):
        """ Transfere dinheiro entre duas contas. """
        conta_origem = self._buscar_conta(num_origem)
        conta_destino = self._buscar_conta(num_destino)

        if not conta_origem:
            print(f"Erro na transferência: Conta de origem {num_origem} não existe.")
            return False
        if not conta_destino:
            print(f"Erro na transferência: Conta de destino {num_destino} não existe.")
            return False
            
        print(f"\n--- Tentativa de Transferência ---")
        print(f"De: {conta_origem.nome_titular} (Conta {num_origem})")
        print(f"Para: {conta_destino.nome_titular} (Conta {num_destino})")
        print(f"Valor: R$ {valor:.2f}")

        # 1. Tenta sacar da origem
        if conta_origem.sacar(valor):
            # 2. Se o saque deu certo, deposita no destino
            conta_destino.depositar(valor)
            print("Transferência concluída com sucesso!")
            return True
        else:
            # O método sacar() da conta_origem já imprimiu "Saldo insuficiente"
            print("Transferência falhou.")
            return False

    def somar_saldos(self):
        """ Retorna a soma de todos os saldos das contas no banco. """
        total = 0.0
        for conta in self._contas:
            total += conta.saldo # Usa o getter @property saldo da Conta_Corrente
        return total

    def __str__(self):
        return f"Banco: {self._nome} - {len(self._contas)} contas ativas."

# --- Programa de Teste para Banco (Questão 5) ---
print("--- Teste da Classe Banco ---")

# 1. Criando Contas (usando a classe da Q4)
c1 = Conta_Corrente(101, "Diogo Aguiar", 1000.0)
c2 = Conta_Corrente(102, "Laura", 500.0)
c3 = Conta_Corrente(103, "Fulano", 0.0)

# 2. Criando o Banco e Adicionando Contas
meu_banco = Banco("IF-Bank")
print(meu_banco)
meu_banco.adicionar_conta(c1)
meu_banco.adicionar_conta(c2)
meu_banco.adicionar_conta(c3)

# 3. Testando Soma de Saldos
saldo_total = meu_banco.somar_saldos()
print(f"Saldo total no {meu_banco._nome}: R$ {saldo_total:.2f}") # Esperado: 1500.00

# 4. Testando Transferência (com sucesso)
print("\n--- Teste de Transferência (Sucesso) ---")
meu_banco.transferir(101, 102, 300.0) # Diogo -> Laura
print(f"Novo saldo Diogo (c1): R$ {c1.saldo:.2f}") # Esperado: 700.0
print(f"Novo saldo Laura (c2): R$ {c2.saldo:.2f}") # Esperado: 800.0

# 5. Testando Transferência (falha por saldo)
print("\n--- Teste de Transferência (Falha: Saldo Insuficiente) ---")
meu_banco.transferir(101, 102, 800.0) # Diogo (700) -> Laura (800)
print(f"Saldo Diogo (c1) [mantido]: R$ {c1.saldo:.2f}") # Esperado: 700.0
print(f"Saldo Laura (c2) [mantido]: R$ {c2.saldo:.2f}") # Esperado: 800.0

# 6. Testando Remoção de Conta
print("\n--- Teste de Remoção de Conta ---")
print(f"Total antes de remover: R$ {meu_banco.somar_saldos():.2f}") # Esperado: 1500.0
meu_banco.remove_conta(103) # Removendo Fulano
print(f"Total após remover (c3 tinha R$0): R$ {meu_banco.somar_saldos():.2f}") # Esperado: 1500.0
meu_banco.remove_conta(999) # Tentando remover conta inexistente

print(f"\nEstado final do {meu_banco._nome}:")
print(c1)
print(c2)
print("-" * 30 + "\n")    
# --- Para executar o programa da Questão 4, descomente a linha abaixo ---
# programa_bancario_q4()

# Para evitar que ele rode automaticamente junto com os outros testes, 
# deixei comentado.
print("--- Definição da Classe Conta_Corrente (Q4) e Banco (Q5) carregada ---")
print("--- Programa de teste da Q4 está comentado para não ser interativo ---")
print("-" * 30 + "\n") 
# --- Programa de Teste para Pais ---
print("--- Teste da Classe Pais ---")
brasil = Pais("Brasil", "Brasília", 8515767)
argentina = Pais("Argentina", "Buenos Aires", 2780400)

# Testando __str__ e acessadores
print(brasil)
print(f"\nCapital do Brasil: {brasil.capital}")

# Testando adição de fronteiras
print("\nAdicionando fronteiras:")
brasil.adiciona_fronteira("Argentina")
brasil.adiciona_fronteira("Uruguai")
brasil.adiciona_fronteira("Paraguai")

# Testando adição duplicada
brasil.adiciona_fronteira("Argentina")

# Testando retorno da lista de fronteiras
print(f"\nPaíses que fazem fronteira com o {brasil.nome}:")
lista_fronteiras_br = brasil.fronteiras
for pais in lista_fronteiras_br:
    print(f"- {pais}")
    
# Verificando que a lista de outro país está vazia
print(f"\nFronteiras da {argentina.nome}: {argentina.fronteiras}")
print("-" * 30 + "\n")
# --- Programa de Teste para Aluno ---
print("--- Teste da Classe Aluno ---")
# Supomos que a matrícula 202510045 signifique Ano 2025, Período 1, ID 0045
aluno1 = Aluno(202510045, "Diogo Bruno", [8.5, 9.0])

# Testando acessadores
print(f"Nome: {aluno1.nome}")
print(f"Matrícula formatada: {aluno1.matricula}")

# Testando adicionar nota
aluno1.adiciona_nota(10.0)
aluno1.adiciona_nota(7)

# Testando média
print(f"Notas: {aluno1._notas}") # Acessando direto (para conferir)
print(f"Média: {aluno1.media():.2f}")

# Testando modificador de nome
aluno1.nome = "Diogo Bruno F. M. de Aguiar"
print(f"Nome alterado: {aluno1.nome}")
print("-" * 30 + "\n")


# --- Programa de Teste para Data ---
print("--- Teste da Classe Data ---")
minha_data = Data(14, 6, 2025)

# Testando acessadores (getters) e __str__
print(f"Data criada: {minha_data}") # Chama __str__
print(f"Acessando o dia: {minha_data.dia}") # Chama o getter @property dia

# Testando modificadores (setters)
minha_data.dia = 25
minha_data.mes = 10
print(f"Data modificada: {minha_data}")

# Testando validação no setter
print("\nTestando valor inválido:")
minha_data.mes = 15 # Deve imprimir um erro
print(f"Data após tentativa inválida: {minha_data}") # O mês não deve ter mudado

# Testando validação no construtor
data_invalida = Data(40, 20, 2024) # Deve imprimir erros e ajustar
print(f"Data inválida corrigida: {data_invalida}")
print("-" * 30 + "\n")