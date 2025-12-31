numero_aprovados = int(input("digite o número total de alunos aprovados:"))
numero_reprovados = int(input("digite o númeero total de alunos reprovados:"))
numero_total_alunos = numero_aprovados + numero_reprovados
porcentagem_aprovados = (numero_aprovados*100)/numero_total_alunos
print(f"A porcentagem de alunos aprovados na disciplina foram de {porcentagem_aprovados:.1f}%")
