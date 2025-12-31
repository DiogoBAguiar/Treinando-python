n = int(input())
lista = list(map(int, input().split()))
menor_valor = lista[0]
posicao = 0
for i in range (1,n):
    if lista[i] < menor_valor:
        menor_valor = lista[i]
        posicao = i
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")        
   