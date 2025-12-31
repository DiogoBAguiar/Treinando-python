texto = input("Digite um texto: ")
texto_maiusculo = ""
for caractere in texto:
    if 'a' <= caractere <= 'z':
        maiuscula = chr(ord(caractere) - 32)
        texto_maiusculo += maiuscula
    else:
        texto_maiusculo += caractere

print(f"Texto em maiúsculo:{texto_maiusculo}")
