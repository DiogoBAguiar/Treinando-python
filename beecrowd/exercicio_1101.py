while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        break
    menor = min(a, b)
    maior = max(a, b)
    soma = 0
    for i in range(menor, maior + 1):
        print(i, end=' ')
        soma += i
    print(f"Sum={soma}")