def substituir_vogais_por_asterisco(texto):
    novo_texto = ""
    vogais = "aeiouAEIOU"
    for caractere in texto:
        if caractere in vogais:
            novo_texto += "*"
        else:
            novo_texto += caractere
    return novo_texto
texto_usuario = input("Digite um texto: ")
print("Texto com vogais substituídas:", substituir_vogais_por_asterisco(texto_usuario))
