def ler_nota_valida():
    while True :
        nota = float(input())
        if 0 <= nota <= 10:
            return nota 
        else:
            print("nota invalida")
nota1 = ler_nota_valida()
nota2 = ler_nota_valida()
media = (nota1 + nota2) / 2
print(f"media = {media:.2f}")