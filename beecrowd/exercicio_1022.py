def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

caso_teste = int(input())
for _ in range(caso_teste):
    entrada = input()
    n1, op1, d1, op, n2, op2, d2 = entrada.split()
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if op == '+':
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = n2 * d1

    divisor = mdc(abs(num), abs(den))
    num_simp = num // divisor
    den_simp = den // divisor

    print(f"{num}/{den} = {num_simp}/{den_simp}")