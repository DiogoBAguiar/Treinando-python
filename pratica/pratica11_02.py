def verificacao_8_caracteres(senha):
    if len(senha) >= 8:
        return True
    else:
        return False
def verificacao_minima_maiuscula(senha):
    for caractere in senha:
        if 'A' <= caractere and caractere <= 'Z':
            return True
    return False
   
def verificacao_minima_02_minuscula(senha):
    contador = 0
    for caractere in senha:
        if 'a' <= caractere and caractere <= 'z':
            contador += 1
    if contador >= 2:
        return True
    else:
        return False 
def verificacao_minima_numero(senha):
    for caractere in senha:
        if '0' <= caractere and caractere <= '9':
            return True
    return False
def verificacao_minima_02_especial(senha):
    contador = 0
    for caractere in senha:
        if not ('a' <= caractere <= 'z' or 'A' <= caractere <= 'Z' or '0' <= caractere <= '9'):
            contador += 1
    if contador >= 2:
        return True
    else:
        return False
def verificar_funcoes(senha,verificacao_8_caracteres, verificacao_minima_maiuscula, verificacao_minima_02_minuscula, verificacao_minima_numero, verificacao_minima_02_especial):
    if (verificacao_8_caracteres(senha) and
        verificacao_minima_maiuscula(senha) and
        verificacao_minima_02_minuscula(senha) and
        verificacao_minima_numero(senha) and
        verificacao_minima_02_especial(senha)):
        return True
    else:
        return False
senha = input("Digite uma senha: ")
if verificar_funcoes(senha, verificacao_8_caracteres, verificacao_minima_maiuscula, verificacao_minima_02_minuscula, verificacao_minima_numero, verificacao_minima_02_especial)== True:
    print("Senha válida")
else:
    print("Senha inválida")




