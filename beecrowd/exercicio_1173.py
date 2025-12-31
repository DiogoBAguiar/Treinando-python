n = 10
lista = []
valor_inicial = int(input())
for i in range(n):
    if i == 0:
        lista.append(valor_inicial)
    else:
        novo_valor = lista[i - 1] * 2
        lista.append(novo_valor)
    print(f"N[{i}] = {lista[i]}")