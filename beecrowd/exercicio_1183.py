o = input().strip()
matriz = []
soma = 0.0
content = 0
for i in range(12):
    linha = [float(input()) for i in range(12)]
    matriz.append(linha)
for i in range(12):
    for j in range(i + 1, 12):
        soma += matriz[i][j]
        content += 1
if o == 'S':
    print(f"{soma:.1f}")
elif o == 'M':
    media = soma / content
    print(f"{media:.1f}")
