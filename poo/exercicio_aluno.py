class Aluno:
    def __init__(self, nome_aluno, matricula_aluno):
        self.nome = nome_aluno
        self.matricula = matricula_aluno
        self.notas = []

    def adicionar_nota(self, nota):

        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"-> Aviso: Nota '{nota}' é inválida e não foi adicionada. A nota deve ser entre 0 e 10.")

    def calcular_media(self):

        if not self.notas:
            return 0.0
        media = sum(self.notas) / len(self.notas)
        return media

    def exibir_info(self):
        media_final = self.calcular_media()
        print("\n--- Informações do Aluno ---")
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Notas: {', '.join(map(str, self.notas)) if self.notas else 'Nenhuma nota cadastrada'}")
        print(f"Média final: {media_final:.2f}")

lista_de_alunos = []

print("--- Cadastro de Alunos e Notas ---")


while True:
    qtd_alunos = int(input("Digite a quantidade de alunos a cadastrar: "))
    if qtd_alunos>= 0 :
        break

for i in range(qtd_alunos):
    print(f"\n--- Inserindo dados do Aluno {i + 1} de {qtd_alunos} ---")
    nome = input("Digite o nome do(a) aluno(a): ")
    matricula = input(f"Digite a matrícula de {nome}: ")
    aluno_atual = Aluno(nome, matricula)
    while True:
        notas_input = input(f"Digite as notas de {nome} separadas por espaço (ou deixe em branco para pular): ")
        if not notas_input.strip():
            break        
        notas_str = notas_input.split()       
        try:         
            for nota_str in notas_str:
                nota = float(nota_str.replace(',', '.')) 
                aluno_atual.adicionar_nota(nota)
            break 
        except ValueError:
            print("-> Erro: Uma das notas digitadas não é um número válido. Tente novamente.")

    lista_de_alunos.append(aluno_atual)

print("\n===============================================")
print("Exibindo informações de todos os alunos cadastrados:")
print("===============================================")

if not lista_de_alunos:
    print("Nenhum aluno foi cadastrado.")
else:
    for aluno_obj in lista_de_alunos:
        aluno_obj.exibir_info()


