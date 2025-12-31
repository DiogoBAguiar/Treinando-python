#Analise da turma
soma = 0
aprovados = 0
reprovados = 0

for i in range(40):
    print('Aluno', i + 1)
    nota = float(input(f"Nota => Aluno {i + 1}: "))
    soma += nota
    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1

media_geral_turma = soma / (i+1)

print(f"Média geral da turma: {media_geral_turma:.2f}")
print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")