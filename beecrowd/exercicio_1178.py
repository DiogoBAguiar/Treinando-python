valor_inicial = float(input())
n = []
valor_atual = valor_inicial
for _ in range(100):
    n.append(valor_atual)
    valor_atual /= 2   
for i, valor in enumerate(n):
    print(f"N[{i}] = {valor:.4f}")