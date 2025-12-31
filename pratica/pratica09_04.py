def exibir_pontos(pontos):
    print("\n Pontos digitados:")
    for x, y in pontos:
        print(f"({x}, {y})")

def distancia_ate_origem(ponto):
    x, y = ponto
    return (x ** 2 + y ** 2) ** 0.5

def maior_distancia(pontos):
    maior = 0
    for ponto in pontos:
        dist = distancia_ate_origem(ponto)
        if dist > maior:
            maior = dist
    return maior

def pontos_nos_eixos(pontos):
    return [p for p in pontos if p[0] == 0 or p[1] == 0]

pontos = []

print("Digite coordenadas no plano cartesiano como números inteiros ou (0, 0) para encerrar o programa.")

while True:
    try:
        x,y = map(int, input("Digite (x,y) :").strip().split(","))
        
        if x == 0 and y == 0:
            print("\n Finalizando processo ... \n")
            break
        pontos.append((x, y))
    except ValueError:
        print(" Entrada inválida. Use apenas números inteiros.")


if pontos:
    exibir_pontos(pontos)

    dist = maior_distancia(pontos)
    print(f"\n Maior distância de um ponto até a origem: {dist:.2f}\n")

    nos_eixos = pontos_nos_eixos(pontos)
    print("\n Pontos nos eixos:\n")
    if nos_eixos:
        for p in nos_eixos:
            print(f"({p[0]}, {p[1]})")
    else:
        print("Nenhum ponto está sobre os eixos.")
else:
    print("Nenhum ponto foi digitado.")
