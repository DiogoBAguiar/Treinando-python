def contar_frequencia_palavras(texto):
    texto_tratado = ""
    for caractere in texto:
        if caractere.isalnum() or caractere.isspace():
            texto_tratado += caractere
        else:          
            texto_tratado += " "
    texto_tratado = texto_tratado.lower()
    palavras = texto_tratado.split()
    frequencias = {}

    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
    print("\nFrequência das palavras:")
    for palavra, freq in frequencias.items():
        print(f"{palavra}: {freq}")
texto_usuario = input("Digite um texto: ")
contar_frequencia_palavras(texto_usuario)
