def quadrado(l: float) -> float:
    """
    Calcula a área de um quadrado.
    """
    return l * l

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
l = float(input("lado do quadrado: "))
exibir(quadrado(l))

print(f'A área do quadrado é = {quadrado(l):.2f}')
