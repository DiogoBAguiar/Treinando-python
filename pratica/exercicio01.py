def somar(num1: int, num2: int) -> int:
    """
    Realiza a soma de dois números inteiros.
    
    """
    return num1 + num2


def dividir(num1: int, num2: int) -> int:
    """
    Realizar a divisão de dois números inteiros.

    """
    return num1 / num2


def multiplicar(num1: int, num2: int) -> int:
    """
    Realizar a multiplicação de dois números inteiros.

    """
    return num1 * num2


def subtrair(num1: int, num2: int) -> int:
    """
    Realizar a subtração de dois números inteiros.
    """
    return num1 - num2


def exibir(num1: int, num2: int) -> None:
    """
    Exibe os números dados.

    """
    print(f"Primeiro número: {num1}")
    print(f"Segundo número: {num2}")


def mensagem_pt() -> str:
    """
    exibe uma mensagem de boas-vindas em português.
    
    """
    return "Olá, bem-vindo ao programa de operações matemáticas!"


def mensagem_en() -> str:
    """
    exibe uma mensagem de boas-vindas em inglês.
    """
    return "Hello, welcome to the math operations program!"


def boas_vindas() -> None:
    """
    Exibe uma mensagem de boas-vindas em português.
    """
    msg = mensagem_pt()
    print(msg)
