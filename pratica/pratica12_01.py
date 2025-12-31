def contar_caracteres(texto):
    minusculas = 0
    maiusculas = 0
    numericos = 0
    especiais = 0
    total = len(texto)

    for i in texto:
        if i.islower():
            minusculas += 1
        elif i.isupper():
            maiusculas += 1
        elif i.isdigit():
            numericos += 1
        elif not i.isalnum():
            especiais += 1

    print("Quantidade de letras minúsculas:", minusculas)
    print("Quantidade de letras maiúsculas:", maiusculas)
    print("Quantidade de símbolos numéricos:", numericos)
    print("Quantidade de caracteres especiais:", especiais)
    print("Quantidade total de símbolos:", total)


# Entrada do usuário
texto_usuario = input("Digite um texto: ")
contar_caracteres(texto_usuario)
