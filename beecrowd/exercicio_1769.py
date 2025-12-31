while True:
    try:
        linha = input().strip()
    except EOFError:
        break
    if not linha:
        continue
    numeros = []
    for c in linha:
        if c.isdigit():
            numeros.append(int(c))
    if len(numeros) != 11:
        print("CPF invalido")
        continue
    soma_b1 = 0
    for i in range(9):
        soma_b1 += numeros[i] * (i + 1)
    b1 = soma_b1 % 11
    if b1 == 10:
        b1 = 0
    soma_b2 = 0
    for i in range(9):
        soma_b2 += numeros[i] * (9 - i)
    b2 = soma_b2 % 11
    if b2 == 10:
        b2 = 0
    if b1 == numeros[9] and b2 == numeros[10]:
        print("CPF valido")
    else:
        print("CPF invalido")