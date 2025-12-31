casos_teste = int(input()) 
for _ in range(casos_teste):
    x, y = map(int, input().split())  
    menor = min(x, y)
    maior = max(x, y)
    soma_impares = 0
    for i in range(menor + 1, maior): 
        if i % 2 != 0:  
            soma_impares += i
    print(soma_impares)
    