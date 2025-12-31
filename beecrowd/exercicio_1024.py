def criptografar_linha(linha):
    
    primeira_passada = ''
    for c in linha:
        if c.isalpha():
            primeira_passada += chr(ord(c) + 3)
        else:
            primeira_passada += c
            
    segunda_passada = primeira_passada[::-1]

    metade = len(segunda_passada) // 2
    terceira_passada = ''
    for i in range(len(segunda_passada)):
        if i >= metade:
            terceira_passada += chr(ord(segunda_passada[i]) - 1)
        else:
            terceira_passada += segunda_passada[i]

    return terceira_passada

n = int(input())

for _ in range(n):
    linha = input()
    print(criptografar_linha(linha))

