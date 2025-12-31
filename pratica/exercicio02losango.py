def losango(d1: float, d2: float) -> float:
    """
    Calcula a área de um losango.
    """
    return (d1 * d2) / 2
def exibir(valor: float) -> None:
    """
    Exibe um valor numérico na tela.
    """
    print(f"Área calculada: {valor:.2f}")
def mensagem_pt() -> str:
    """
    Retorna uma mensagem de boas-vindas em português.
    """
    return "Olá, bem-vindo ao programa de cálculo de áreas de losango!"
def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
    
boas_vindas()
d1 = float(input("diagonal maior do losango: "))
d2 = float(input("diagonal menor do losango: "))
exibir(losango(d1,d2))

print(f'A área do losango é = {losango(d1,d2):.2f}')