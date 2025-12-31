n = int(input().strip())

for _ in range(n):
    s = input().strip()
    k = int(input().strip())

    base = ord('A')
    lista = []

    for i in s:
       
        codigo = ord(i) - base
        codigo = (codigo - k) % 26    
        lista.append(chr(base + codigo))

    print(''.join(lista))
