def retangulo(b,h: float) -> float:
    """
    Calcula a área de um retangulo.
    """
    return b * h

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
b = float(input("base do retangulo: "))
h = float(input("altura do retangulo: "))
exibir(retangulo(b,h))

print(f'A área do retangulo é = {retangulo(b,h):.2f}')