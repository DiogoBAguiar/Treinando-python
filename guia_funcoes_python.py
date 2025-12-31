# -*- coding: utf-8 -*-

"""
Guia de Estudo: Funções Nativas do Python
Este script foi criado para demonstrar o uso de diversas funções
nativas (built-in) da linguagem Python.
Cada seção aborda uma categoria de funções com exemplos práticos.
"""

# Para usar as funções de controle de objeto e metaprogramação,
# vamos definir algumas classes de exemplo primeiro.

class Pessoa:
    """Uma classe simples para representar uma pessoa."""
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e sou {self.profissao}."

class Animal:
    """Classe base para animais."""
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return "Som genérico de animal"

class Cachorro(Animal):
    """Subclasse que representa um cachorro."""
    def __init__(self, nome, raca):
        # 🔹 super() – chama métodos da superclasse.
        # Chama o __init__ da classe pai (Animal) para inicializar nome e especie.
        super().__init__(nome, especie="Cachorro")
        self.raca = raca
        self._idade_privada = 0

    def emitir_som(self):
        return "Au au!"

    # 🔹 @property() – cria um atributo "read-only" (apenas leitura).
    @property
    def idade(self):
        """Este é um getter para a idade, permitindo apenas a leitura."""
        return self._idade_privada

    # 🔹 @classmethod() – método que opera na classe, não na instância.
    @classmethod
    def criar_com_ano_nascimento(cls, nome, raca, ano_nascimento):
        """Um 'construtor alternativo' que cria uma instância a partir do ano de nascimento."""
        # Note que o primeiro argumento é 'cls', a própria classe.
        from datetime import date
        idade_calculada = date.today().year - ano_nascimento
        cachorro = cls(nome, raca)
        cachorro._idade_privada = idade_calculada
        return cachorro

    # 🔹 @staticmethod() – método que não depende da classe ou da instância.
    @staticmethod
    def eh_mamifero():
        """Método estático que retorna uma informação geral sobre a espécie."""
        # Note que não recebe 'cls' nem 'self'.
        return True

print("--- Início do Guia de Funções Nativas do Python ---")

# ==============================================================================
# 🔹 1. Manipulação de tipos e conversões
# ==============================================================================
print("\n### 1. Manipulação de tipos e conversões ###")

# int(), float(), complex() – conversão para tipos numéricos.
numero_str = "100"
numero_float = 12.5
print(f"'{numero_str}' como int: {int(numero_str)}")
print(f"{numero_float} como int: {int(numero_float)}")
print(f"'10' como float: {float('10')}")
print(f"Número complexo com 3 e 4: {complex(3, 4)}")

# str() – converte para string.
ano = 2025
lista_numeros = [1, 2, 3]
print(f"O número {ano} como string: '{str(ano)}'")
print(f"A lista {lista_numeros} como string: '{str(lista_numeros)}'")

# bool() – converte para booleano. (0, None, "", [], {} são False)
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool([]): {bool([])}")
print(f"bool(['a']): {bool(['a'])}")

# list(), tuple(), set(), dict() – criam coleções.
string_letras = "abacaxi"
tupla_frutas = ('maçã', 'banana', 'cereja')
lista_de_pares = [('a', 1), ('b', 2)]

print(f"A string '{string_letras}' como lista: {list(string_letras)}")
print(f"A lista {lista_numeros} como tupla: {tuple(lista_numeros)}")
print(f"A string '{string_letras}' como conjunto (remove duplicadas): {set(string_letras)}")
print(f"A lista de pares {lista_de_pares} como dicionário: {dict(lista_de_pares)}")

# frozenset() – cria um conjunto imutável.
conjunto_congelado = frozenset(['a', 'b', 'c'])
print(f"Conjunto congelado (imutável): {conjunto_congelado}")
# conjunto_congelado.add('d')  # Isso causaria um erro (AttributeError)

# bytes(), bytearray(), memoryview() – manipulam dados binários.
texto_para_bytes = "Olá, Diogo!"
dados_em_bytes = bytes(texto_para_bytes, 'utf-8')
print(f"'{texto_para_bytes}' em bytes: {dados_em_bytes}")

dados_mutaveis = bytearray(b'abcde')
dados_mutaveis[0] = ord('A')  # Modificando o primeiro byte
print(f"Bytearray modificado: {dados_mutaveis}")

vista_memoria = memoryview(dados_mutaveis)
print(f"Memory view do bytearray: {vista_memoria[0:3].tobytes()}")

# ==============================================================================
# 🔹 2. Matemática e números
# ==============================================================================
print("\n### 2. Matemática e números ###")

# abs() – valor absoluto.
print(f"Valor absoluto de -15.5 é: {abs(-15.5)}")

# pow(base, exp) – potência.
print(f"2 elevado a 8 é: {pow(2, 8)}")

# round() – arredondamento.
numero_decimal = 3.14159
print(f"Arredondando {numero_decimal} para o inteiro mais próximo: {round(numero_decimal)}")
print(f"Arredondando {numero_decimal} para 2 casas decimais: {round(numero_decimal, 2)}")

# divmod(x, y) – retorna quociente e resto.
quociente, resto = divmod(10, 3)
print(f"10 dividido por 3 é {quociente} com resto {resto}")

# sum(), min(), max() – operações sobre coleções.
valores = [10, 5, 25, 1, 99]
print(f"Na lista {valores}:")
print(f"  A soma é: {sum(valores)}")
print(f"  O mínimo é: {min(valores)}")
print(f"  O máximo é: {max(valores)}")

# ==============================================================================
# 🔹 3. Iteração e sequências
# ==============================================================================
print("\n### 3. Iteração e sequências ###")

# len() – tamanho.
curso = "Engenharia de Software"
print(f"O tamanho da string '{curso}' é: {len(curso)}")
print(f"O tamanho da lista {valores} é: {len(valores)}")

# range() – sequência de números.
print("Números de 0 a 4 usando range(5):")
for i in range(5):
    print(i, end=' ')
print()

# enumerate() – enumeração em laços.
materias = ["Cálculo", "Algoritmos", "Banco de Dados"]
print("Enumerando matérias do curso:")
for indice, materia in enumerate(materias):
    print(f"  {indice}: {materia}")

# zip() – junta iteráveis em pares.
alunos = ["Diogo", "João", "Maria"]
notas = [9.5, 8.0, 10.0]
print("Juntando alunos e notas com zip:")
for aluno, nota in zip(alunos, notas):
    print(f"  {aluno} tirou a nota {nota}")

# map() – aplica uma função a cada item de um iterável.
numeros_para_mapear = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x*x, numeros_para_mapear))
print(f"O quadrado dos números {numeros_para_mapear} é: {quadrados}")

# filter() – filtra elementos de um iterável.
numeros_para_filtrar = range(10)
pares = list(filter(lambda x: x % 2 == 0, numeros_para_filtrar))
print(f"Filtrando números pares de 0 a 9: {pares}")

# sorted() – ordena elementos.
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2]
print(f"Lista desordenada: {numeros_desordenados}")
print(f"Lista ordenada: {sorted(numeros_desordenados)}")

# reversed() – inverte a ordem.
print("Contagem regressiva de 'Python':")
for char in reversed("Python"):
    print(char, end=' ')
print()

# all(), any() – verificam condições em iteráveis.
lista1 = [True, True, True]
lista2 = [True, False, True]
lista3 = [False, False, False]
print(f"all({lista1})? {all(lista1)}")  # True, todos são verdadeiros
print(f"all({lista2})? {all(lista2)}")  # False, um é falso
print(f"any({lista2})? {any(lista2)}")  # True, pelo menos um é verdadeiro
print(f"any({lista3})? {any(lista3)}")  # False, nenhum é verdadeiro

# ==============================================================================
# 🔹 3.5. Estruturas de Controle e Manipulação de Listas
# ==============================================================================
print("\n### 3.5. Estruturas de Controle e Manipulação de Listas ###")

# --- Estruturas de Controle ---
print("\n--- Estruturas de Controle ---")

# if, elif, else – Tomada de decisão
nota_aluno = 7.5
print(f"Analisando a nota {nota_aluno}:")
if nota_aluno >= 7.0:
    print("  Status: Aprovado!")
elif nota_aluno >= 5.0:
    print("  Status: Recuperação.")
else:
    print("  Status: Reprovado.")

# for – Laço de repetição
print("\nUsando 'for' para iterar sobre uma lista de matérias:")
for materia in materias: # 'materias' foi definida na seção 3
    print(f"  - Estudando {materia}")

# range() já foi visto, mas é frequentemente usado com for
print("\nTabuada do 5 usando 'for' e 'range':")
for i in range(1, 11): # de 1 a 10
    print(f"  5 x {i} = {5*i}")

# while – Laço de repetição condicional
print("\nUsando 'while' para uma contagem regressiva:")
contador = 3
while contador > 0:
    print(f"  {contador}...")
    contador -= 1
print("  Decolar!")

# break, continue, pass – Controle de fluxo dentro de laços
print("\nExemplo com 'break', 'continue' e 'pass':")
for num in range(1, 10):
    if num == 3:
        print("  Encontrei o 3, usando 'continue' para pular a impressão.")
        continue # Pula para a próxima iteração
    elif num % 2 == 0:
        # Apenas um exemplo para 'pass'
        pass # Não faz nada, apenas ocupa o lugar de um bloco de código
    elif num == 7:
        print("  Encontrei o 7, usando 'break' para sair do laço.")
        break # Interrompe o laço
    print(f"  Número atual: {num}")


# --- Métodos de Lista ---
print("\n--- Métodos de Lista ---")
# Criando uma lista para os exemplos
disciplinas = ["Algoritmos", "Cálculo", "Física"]
print(f"Lista inicial de disciplinas: {disciplinas}")

# append() – Adiciona um item ao final da lista
disciplinas.append("Química")
print(f"Após append('Química'): {disciplinas}")

# insert() – Adiciona um item em uma posição específica
disciplinas.insert(0, "Introdução à Eng. de Software")
print(f"Após insert(0, '...'): {disciplinas}")

# pop() – Remove e retorna o item de uma posição (padrão: último)
materia_removida = disciplinas.pop()
print(f"Após pop(), removeu '{materia_removida}': {disciplinas}")
primeira_materia = disciplinas.pop(0)
print(f"Após pop(0), removeu '{primeira_materia}': {disciplinas}")

# remove() – Remove o primeiro item com o valor especificado
disciplinas.remove("Cálculo")
print(f"Após remove('Cálculo'): {disciplinas}")

# index() – Retorna o índice do primeiro item com o valor especificado
disciplinas.append("Algoritmos") # Adicionando de volta para ter o que buscar
idx_algoritmos = disciplinas.index("Algoritmos")
print(f"O índice de 'Algoritmos' é: {idx_algoritmos}")

# count() – Retorna o número de vezes que um item aparece
contagem = disciplinas.count("Algoritmos")
print(f"'Algoritmos' aparece {contagem} vez(es).")

# sort() – Ordena a lista (in-place, ou seja, modifica a própria lista)
disciplinas.sort()
print(f"Lista ordenada com sort(): {disciplinas}")

# reverse() – Inverte a ordem dos elementos (in-place)
disciplinas.reverse()
print(f"Lista invertida com reverse(): {disciplinas}")

# ==============================================================================
# 🔹 3.6. Comprehensions, Lambdas e Geradores
# ==============================================================================
print("\n### 3.6. Comprehensions, Lambdas e Geradores ###")

# Funções Lambda (Anônimas)
print("\n--- Funções Lambda ---")
# Já usamos em map() e filter(). São pequenas funções de uma linha.
soma_lambda = lambda a, b: a + b
print(f"Resultado de uma função lambda (5+3): {soma_lambda(5, 3)}")

# List Comprehension – Uma forma concisa de criar listas
print("\n--- Comprehensions ---")
numeros = [1, 2, 3, 4, 5, 6]
quadrados_comp = [n**2 for n in numeros]
print(f"Quadrados (via List Comprehension): {quadrados_comp}")
pares_comp = [n for n in numeros if n % 2 == 0]
print(f"Números pares (via List Comprehension): {pares_comp}")

# Set e Dict Comprehensions
set_comp = {letra for letra in 'abracadabra'}
print(f"Conjunto de letras (via Set Comprehension): {set_comp}")
dict_comp = {f"item_{i}": i*10 for i in range(1, 4)}
print(f"Dicionário (via Dict Comprehension): {dict_comp}")

# Expressões Geradoras (Generator Expressions)
print("\n--- Expressões Geradoras ---")
# Parecem list comprehensions, mas usam parênteses.
# Elas não criam a lista inteira na memória, gerando valores sob demanda.
# Isso é ótimo para sequências muito grandes.
gerador_quadrados = (x*x for x in range(1000000))
print(f"Objeto gerador criado: {gerador_quadrados}")
# print(f"Os 5 primeiros valores do gerador:")
# for i in range(5):
#     print(f"  {next(gerador_quadrados)}")


# ==============================================================================
# 🔹 3.7. Métodos Comuns de Strings e Dicionários
# ==============================================================================
print("\n### 3.7. Métodos Comuns de Strings e Dicionários ###")

# --- Métodos de String ---
print("\n--- Métodos de String ---")
frase = "   Olá Mundo, Python é Incrível!   "
print(f"Original: '{frase}'")
print(f".strip(): '{frase.strip()}'") # Remove espaços no início/fim
print(f".lower(): '{frase.lower()}'") # Converte para minúsculas
print(f".upper(): '{frase.upper()}'") # Converte para maiúsculas
print(f".replace('Mundo', 'Diogo'): '{frase.strip().replace('Mundo', 'Diogo')}'")
palavras = frase.strip().split(',') # Divide a string em uma lista
print(f".split(','): {palavras}")
print(f".join(): {'-'.join(['a', 'b', 'c'])}") # Junta elementos de uma lista em uma string

# --- Métodos de Dicionário ---
print("\n--- Métodos de Dicionário ---")
aluno_info = {'nome': 'Diogo', 'curso': 'Eng. de Software', 'periodo': 2}
print(f"Dicionário de exemplo: {aluno_info}")
print(f".keys(): {aluno_info.keys()}")
print(f".values(): {aluno_info.values()}")
print(f".items(): {aluno_info.items()}") # Pares chave-valor

# .get() é uma forma segura de acessar chaves, evitando erros
print(f".get('nome'): {aluno_info.get('nome')}")
print(f".get('universidade', 'IFPB'): {aluno_info.get('universidade', 'IFPB')}") # Retorna valor padrão se a chave não existir

# ==============================================================================
# 🔹 3.8. Definição de Funções e Módulos
# ==============================================================================
print("\n### 3.8. Definição de Funções e Módulos ###")

# --- Definição de Funções (def) ---
print("\n--- Definição de Funções (def) ---")

# Esta é a forma de criar blocos de código reutilizáveis.
def saudacao(nome, saud="Olá"):
    """
    Esta é uma docstring. Ela documenta o que a função faz.
    Retorna uma saudação personalizada.
    """
    return f"{saud}, {nome}!"

# Chamando a função
print(f"Função com argumento padrão: {saudacao('Diogo')}")
print(f"Função com argumento nomeado: {saudacao(saud='Bem-vindo', nome='Bruno')}")


# Funções com número variável de argumentos (*args e **kwargs)
def relatorio_completo(aluno_principal, *outros_alunos, **detalhes_curso):
    """
    *args: agrupa múltiplos argumentos posicionais em uma tupla.
    **kwargs: agrupa múltiplos argumentos nomeados em um dicionário.
    """
    print(f"Aluno Principal: {aluno_principal}")
    if outros_alunos:
        print(f"Outros Alunos na equipe: {', '.join(outros_alunos)}")
    if detalhes_curso:
        print("Detalhes do Curso:")
        for chave, valor in detalhes_curso.items():
            print(f"  - {chave.replace('_', ' ').title()}: {valor}")

print("\nChamando função com *args e **kwargs:")
relatorio_completo(
    "Diogo", "João", "Maria",
    curso="Engenharia de Software",
    instituicao="IFPB",
    periodo=2
)

# --- Módulos e Importação (import) ---
print("\n--- Módulos e Importação (import) ---")

# 'import' permite usar código de outros arquivos/bibliotecas.
# Exemplo 1: Importar um módulo inteiro
import math
print(f"O valor de Pi (do módulo math) é: {math.pi}")
print(f"A raiz quadrada de 16 (math.sqrt) é: {math.sqrt(16)}")

# Exemplo 2: Importar um item específico de um módulo
from random import choice
participantes = ["Diogo", "João", "Maria", "Ana"]
sorteado = choice(participantes)
print(f"De {participantes}, o sorteado foi: {sorteado}")

# Exemplo 3: Importar com um apelido (alias)
import datetime as dt
print(f"A data e hora atuais são: {dt.datetime.now()}")


# ==============================================================================
# 🔹 4. Entrada e saída
# ==============================================================================
print("\n### 4. Entrada e saída ###")

# print() – saída.
# Usada extensivamente neste script.
print("A função print() exibe informações no console.")

# input() – entrada do usuário.
# O código abaixo está comentado para não pausar a execução do script.
# Remova o '#' para testar.
# nome_usuario = input("Qual é o seu nome? ")
# print(f"Olá, {nome_usuario}! Bem-vindo ao guia.")

# open() – manipulação de arquivos.
# Escrevendo em um arquivo
try:
    with open("meu_arquivo_de_estudo.txt", "w", encoding='utf-8') as f:
        print("Escrevendo no arquivo 'meu_arquivo_de_estudo.txt'...")
        f.write("Linha 1: Python é uma linguagem poderosa.\n")
        f.write("Linha 2: Estudar é o caminho.\n")
        # f.write(123) # Descomente esta linha para forçar um TypeError
except (IOError, TypeError) as e:
    print(f"Ocorreu um erro ao manipular o arquivo: {e}")
else:
    # O bloco 'else' é executado se nenhuma exceção ocorrer no 'try'.
    print("Arquivo escrito com sucesso, sem exceções.")
finally:
    # O bloco 'finally' é sempre executado, com ou sem exceção.
    # É ideal para tarefas de "limpeza", como fechar conexões.
    print("Bloco 'finally': finalizando a operação com o arquivo.")


# Lendo o arquivo
try:
    with open("meu_arquivo_de_estudo.txt", "r", encoding='utf-8') as f:
        print("Lendo o conteúdo do arquivo:")
        conteudo = f.read()
        print(conteudo)
except IOError as e:
    print(f"Ocorreu um erro de I/O: {e}")


# ==============================================================================
# 🔹 5. Utilidades diversas
# ==============================================================================
print("\n### 5. Utilidades diversas ###")

# type() – retorna o tipo.
var_int = 42
var_str = "IFPB"
print(f"O tipo de {var_int} é {type(var_int)}")
print(f"O tipo de '{var_str}' é {type(var_str)}")

# isinstance(obj, classe) – verifica se um objeto pertence a uma classe.
print(f"A variável '{var_str}' é uma instância de str? {isinstance(var_str, str)}")
print(f"A variável {var_int} é uma instância de float? {isinstance(var_int, float)}")

# id() – endereço interno do objeto.
print(f"O endereço de memória de '{var_str}' é {id(var_str)}")

# dir() – lista atributos e métodos disponíveis.
print(f"Alguns atributos/métodos de uma string: {dir('texto')[:5]}")

# help() – documentação interativa.
print("A função help() é melhor usada no console interativo. Ex: help(list)")
# help(list) # Descomente para ver a ajuda sobre listas

# callable() – verifica se algo é chamável (função/objeto com __call__).
def minha_funcao():
    return "Função chamada"
print(f"minha_funcao é chamável? {callable(minha_funcao)}")
print(f"A variável {var_int} é chamável? {callable(var_int)}")

# hash() – retorna hash do objeto.
print(f"Hash da string 'Python': {hash('Python')}")
# print(f"Hash de uma lista (dará erro): {hash([1, 2])}") # TypeError: unhashable type: 'list'

# ==============================================================================
# 🔹 6. Funções de criação e avaliação de código
# ==============================================================================
print("\n### 6. Funções de criação e avaliação de código ###")

# eval() – avalia expressão como Python.
expressao = "5 * (10 + 2)"
resultado_eval = eval(expressao)
print(f"O resultado da expressão '{expressao}' é: {resultado_eval}")

# exec() – executa código Python dinamicamente.
codigo_str = """
soma = 0
for i in range(5):
    soma += i
print(f'Soma calculada com exec(): {soma}')
"""
print("Executando um bloco de código com exec():")
exec(codigo_str)

# compile() – compila código em objeto executável.
codigo_compilado = compile("x = 10\ny = 20\nprint(f'Resultado de compile+exec: {x*y}')", 'script', 'exec')
print("Executando código pré-compilado:")
exec(codigo_compilado)

# ==============================================================================
# 🔹 7. Controle de objetos
# ==============================================================================
print("\n### 7. Controle de objetos ###")

# Usando a classe Pessoa definida no início do arquivo
dev = Pessoa("Diogo Bruno", "Estudante de Engenharia de Software")
print(f"Objeto criado: {dev.apresentar()}")

# hasattr(obj, nome) – verifica se o atributo existe.
print(f"O objeto 'dev' tem o atributo 'nome'? {hasattr(dev, 'nome')}")
print(f"O objeto 'dev' tem o atributo 'idade'? {hasattr(dev, 'idade')}")

# setattr(obj, nome, valor) – define atributo.
print("Definindo o atributo 'idade' com setattr(dev, 'idade', 20)...")
setattr(dev, 'idade', 20)
print(f"Agora 'dev' tem o atributo 'idade'? {hasattr(dev, 'idade')}")

# getattr(obj, nome) – pega atributo.
nome_obtido = getattr(dev, 'nome')
idade_obtida = getattr(dev, 'idade')
print(f"Valor obtido com getattr para 'nome': {nome_obtido}")
print(f"Valor obtido com getattr para 'idade': {idade_obtida}")

# delattr(obj, nome) – remove atributo.
print("Removendo o atributo 'idade' com delattr(dev, 'idade')...")
delattr(dev, 'idade')
print(f"Após remover, 'dev' tem o atributo 'idade'? {hasattr(dev, 'idade')}")


# ==============================================================================
# 🔹 8. Construção e metaprogramação
# ==============================================================================
print("\n### 8. Construção e metaprogramação ###")
# As funções super(), @classmethod, @staticmethod e @property
# foram demonstradas na definição das classes Animal e Cachorro no início.
# Vamos ver exemplos de seu uso aqui.

# Instância normal
rex = Cachorro("Rex", "Labrador")
print(f"{rex.nome} é um {rex.especie} da raça {rex.raca}.")
print(f"{rex.nome} faz: {rex.emitir_som()}")

# Usando o @classmethod como um construtor alternativo
bobby = Cachorro.criar_com_ano_nascimento("Bobby", "Vira-lata", 2020)
print(f"{bobby.nome} foi criado com o classmethod e tem {bobby.idade} anos.")

# Usando o @staticmethod
print(f"Um cachorro é mamífero? {Cachorro.eh_mamifero()}")

# Usando a @property
print(f"A idade de Bobby (lida via property) é: {bobby.idade}")
# bobby.idade = 6 # Isso causaria um erro (AttributeError: can't set attribute)

# globals(), locals() – dicionários de variáveis globais/locais.
print(f"Chaves no escopo global (algumas): {list(globals().keys())[:5]}")

def funcao_escopo():
    variavel_local = "Eu existo aqui dentro"
    print(f"Dicionário de variáveis locais: {locals()}")

funcao_escopo()

# vars() – retorna atributos de um objeto.
print(f"Atributos do objeto 'dev' (via vars()): {vars(dev)}")

# object() – cria um objeto base.
objeto_base = object()
print(f"Um objeto base, sem atributos: {objeto_base}")

print("\n--- Fim do Guia ---")



