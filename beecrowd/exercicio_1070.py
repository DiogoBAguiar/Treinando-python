numero = int(input())
impares = []
if numero % 2 == 0:
    numero += 1
for i in range(6):
    impares.append(numero)
    numero += 2
print(*impares, sep='\n')
    