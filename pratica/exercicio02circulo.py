def circulo(r: float) -> float:
    """
    Calcula a área de um círculo.
    """
    return 3.14 * r * r
def exibir(valor: float) -> None:
    """
    Exibe um valor numérico na tela.
    """
    print(f"Área calculada: {valor:.2f}")
def mensagem_pt() -> str:
    """
    Retorna uma mensagem de boas-vindas em português.
    """
    return "Olá, bem-vindo ao programa de cálculo de áreas de círculos!"
def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
    
boas_vindas()
r = float(input("raio do círculo: "))
exibir(circulo(r))

print(f'A área do círculo é = {circulo(r):.2f}')