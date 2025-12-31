def quadrado(l: float) -> float:
    return l * l

def retangulo(b: float, h: float) -> float:
    return b * h

def triangulo(b: float, h: float) -> float:
    return (b * h) / 2

def trapezio(b1: float, b2: float, h: float) -> float:
    return ((b1 + b2) * h) / 2

def paralelogramo(b: float, h: float) -> float:
    return b * h

def losango(d1: float, d2: float) -> float:
    return (d1 * d2) / 2

def circulo(r: float) -> float:
    return 3.14 * r * r

def exibir(valor: float) -> None:
    print(f"Área calculada: {valor:.2f}")

def mensagem_pt() -> str:
    return "Olá, bem-vindo ao programa de cálculo de áreas!"

def mensagem_en() -> str:
    return "Hello, welcome to the area calculation program!"

def boas_vindas(lang: str = "pt") -> None:
    msg = mensagem_pt() if lang == "pt" else mensagem_en()
    print(msg)

def menu() -> None:
    boas_vindas("pt")

    while True:
        print("\nEscolha a figura geométrica para calcular a área:")
        print("1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Triângulo")
        print("4 - Trapézio")
        print("5 - Paralelogramo")
        print("6 - Losango")
        print("7 - Círculo")
        print("0 - Sair")

        opcao = input("Digite a opção: ")

        try:
            if opcao == "1":
                l = float(input("Digite o lado: "))
                exibir(quadrado(l))
            elif opcao == "2":
                b = float(input("Digite a base: "))
                h = float(input("Digite a altura: "))
                exibir(retangulo(b, h))
            elif opcao == "3":
                b = float(input("Digite a base: "))
                h = float(input("Digite a altura: "))
                exibir(triangulo(b, h))
            elif opcao == "4":
                b1 = float(input("Digite a base maior: "))
                b2 = float(input("Digite a base menor: "))
                h = float(input("Digite a altura: "))
                exibir(trapezio(b1, b2, h))
            elif opcao == "5":
                b = float(input("Digite a base: "))
                h = float(input("Digite a altura: "))
                exibir(paralelogramo(b, h))
            elif opcao == "6":
                d1 = float(input("Digite a diagonal maior: "))
                d2 = float(input("Digite a diagonal menor: "))
                exibir(losango(d1, d2))
            elif opcao == "7":
                r = float(input("Digite o raio: "))
                exibir(circulo(r))
            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
            
if __name__ == "__main__":
    menu()
    
