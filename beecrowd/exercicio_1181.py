l = int(input())
t = input().strip()
matriz = []
for i in range(12):
    linha = [float(input()) for i in range(12)]
    matriz.append(linha)
soma = sum(matriz[l])
if t == 'S':
    print(f"{soma:.1f}")
elif t == 'M':
    media = soma / 12
    print(f"{media:.1f}")
