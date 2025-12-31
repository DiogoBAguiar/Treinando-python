def triangulo(b: float, h: float) -> float:
    """
    Calcula a área de um triângulo.
    """
    return (b * h) / 2
def exibir(valor: float) -> None:
    """
    Exibe um valor numérico na tela.
    """
    print(f"Área calculada: {valor:.2f}")
def mensagem_pt() -> str:
    """
    Retorna uma mensagem de boas-vindas em português.
    """
    return "Olá, bem-vindo ao programa de cálculo de áreas!"
def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
    
boas_vindas()
b = float(input("base do triangulo: "))
h = float(input("altura do triangulo: "))
exibir(triangulo(b,h))

print(f'A área do retangulo é = {triangulo(b,h):.2f}')