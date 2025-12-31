numero_aulas = int(input("Digite o número de aulas: "))
numero_faltas = int(input("Digite o número de faltas: "))
frequencia = (numero_aulas - numero_faltas) / numero_aulas * 100
print(f"A frequência do aluno é de {frequencia:.2f}%")
