# Uma função simpls que encontra o maior número em uma lista

def encontrar_maior(lista_de_numeros):
    if not lista_de_numeros:
        return None
    
    maior_ate_agora = lista_de_numeros[0]
    
    for numero in lista_de_numeros:
        if numero > maior_ate_agora:
            maior_ate_agora = numero
    return maior_ate_agora

numeros = [10, 3, 5, 7, 2, 8]
maior_numero = encontrar_maior(numeros)  
print(maior_numero)      