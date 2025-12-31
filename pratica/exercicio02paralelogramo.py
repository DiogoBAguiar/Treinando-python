def paralelogramo(b: float, h: float) -> float:
    """
    Calcula a área de um paralelogramo.
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
    return "Olá, bem-vindo ao programa de cálculo de áreas de paralelogramos!"
def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
    
boas_vindas()
b = float(input("base do paralelogramo: "))
h = float(input("altura do paralelogramo: "))
exibir(paralelogramo(b,h))

print(f'A área do paralelogramo é = {paralelogramo(b,h):.2f}')