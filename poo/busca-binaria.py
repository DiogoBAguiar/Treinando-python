def encontra_indice(chave,chaves):
    esquerda = 0
    direita = len(chaves) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if chaves[meio] == chave:
            return meio
        elif chaves[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
def busca_binaria_recursiva(chave, chaves, esquerda, direita):
    if esquerda > direita:
        return -1
    meio = (esquerda + direita) // 2
    if chaves[meio] == chave:
        return meio
    elif chaves[meio] < chave:
        return busca_binaria_recursiva(chave, chaves, meio + 1, direita)
    else:
        return busca_binaria_recursiva(chave, chaves, esquerda, meio - 1)
    

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

print(busca_binaria_recursiva(7, lista, 0, len(lista) - 1))
