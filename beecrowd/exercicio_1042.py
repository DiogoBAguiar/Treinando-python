def sort_simples():
    entrada = input().split()
    a, b, c = map(int, entrada)
    if a > b and a > c:
        maior = a
    elif b > c:
        maior = b
    else:
        maior = c
    if a < b and a < c:
        menor = a
    elif b < c:
        menor = b
    else:
        menor = c
        
    meio = a + b + c - maior - menor
    print(menor)
    print(meio)
    print(maior)
    print()
    print(a)
    print(b)
    print(c)

sort_simples()


    
        