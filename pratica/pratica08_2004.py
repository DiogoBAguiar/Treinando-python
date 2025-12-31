q = int(input())  

for i in range(q):
    n = int(input()) 
    alimentos_por_tipo = {}
    for i in range(n):
        t, p = map(int, input().split())
        if t not in alimentos_por_tipo:
            alimentos_por_tipo[t] = []
        alimentos_por_tipo[t].append(p)
    total = 0
    for tipo in alimentos_por_tipo:
        pesos = alimentos_por_tipo[tipo]
        
        validos = [p for p in pesos if 10 <= p <= 100]

        if validos:
            total += max(validos)
        else:
            total += max(pesos)  
    print(total)
