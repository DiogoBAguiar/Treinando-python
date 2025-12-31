def localizar_palavra_mais_frequente(texto):
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
    maior_freq = max(frequencias.values())
    palavras_mais_frequentes = []
    for palavra in frequencias:
        if frequencias[palavra] == maior_freq:
            palavras_mais_frequentes.append(palavra)   
    for palavra in palavras_mais_frequentes:
        posicoes = []
        for i in range(len(palavras)):
            if palavras[i] == palavra:
                posicoes.append(i + 1) 
        print(f"Palavra(s) com maior frequência:{palavra}' ocorre {maior_freq} vezes nas posições: {posicoes}")
texto_usuario = input("Digite um texto: ")
localizar_palavra_mais_frequente(texto_usuario)
