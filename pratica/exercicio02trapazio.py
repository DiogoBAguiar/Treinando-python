def trapezio(b1: float, b2: float, h: float) -> float:
    """
    Calcula a área de um trapézio.
    """
    return ((b1 + b2) * h) / 2

def exibir(valor: float) -> None:
    """
    Exibe um valor numérico na tela.
    """
    print(f"Área calculada: {valor:.2f}")
def mensagem_pt() -> str:
    """
    Retorna uma mensagem de boas-vindas em português.
    """
    return "Olá, bem-vindo ao programa de cálculo de áreas do trapézio!"
def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
    
boas_vindas()
b1 = float(input("base 1 do trapezio: "))
b2 = float(input("base 2 do trapezio: "))
h = float(input("altura do trapezio: "))
exibir(trapezio(b1,b2,h))

print(f'A área do trapézio é = {trapezio(b1,b2,h):.2f}')