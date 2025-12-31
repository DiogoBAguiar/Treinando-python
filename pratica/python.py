nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

total_aulas = int(input("Digite o total de aulas do curso: "))
aulas_assistidas = int(input("Digite a quantidade de aulas que o aluno assistiu: "))

frequencia = (aulas_assistidas / total_aulas) * 100

if media >= 7.0 and frequencia >= 75:
    resultado = "Aprovado ;D"
else:
    resultado = "Reprovado :( "

print("------ Resultado Final ------")
print(f"Média final: {media:.2f}")
print(f"Frequência: {frequencia:.2f}%")
print(f"Situação: {resultado}")