while True:
    try:
        linha = input()
        resultado = []
        maiuscula = True  

        for caracter in linha:
            if caracter == ' ':
                resultado.append(caracter)
            else:
                if maiuscula:
                    resultado.append(caracter.upper())
                else:
                    resultado.append(caracter.lower())
                maiuscula = not maiuscula  

        print(''.join(resultado))
    except EOFError:
        break