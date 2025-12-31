qtd_positivos = 0
soma_positivos = 0
for _ in range(6):
    valor = float(input())
    if valor > 0 :
        qtd_positivos += 1
        soma_positivos += valor
media = soma_positivos/qtd_positivos
print(f"{qtd_positivos} valores positivos")  
print(f"{media:.1f}")      