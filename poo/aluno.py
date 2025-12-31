class Aluno :
    def __init__(self,nome,idade,matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

a = Aluno ('Diogo',23,'202514320028')

print('Nome do aluno:',a.nome)
print('Idade do aluno:',a.idade)
print('Matricula do aluno:',a.matricula)    