class No:
    def __init__(self, dado=None , proximo = None):
        self.__dado = dado
        self.__proximo = proximo

    def get_dado(self):
        return self.__dado
        
    def get_proximo(self):
        return self.__proximo

    def set_dado(self, novo_dado):
        self.__dado = novo_dado
        
    def set_proximo(self, novo_proximo):
        self.__proximo = novo_proximo
        
    def __str__(self):
        return str(self.__dado)


class PilhaException(Exception):
    pass
    
class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        
    def estaVazia(self) -> bool:
        return self.__tamanho == 0
        
    def tamanho(self) -> int:
        return self.__tamanho
        
    def empilhar(self, valor):
        novo_no = No(valor)
        if self.estaVazia():
            self.__topo = No(valor)
        novo_no.set_proximo(self.__topo)
        self.__topo = novo_no
        self.__tamanho += 1

    def desempilhar(self):
        if self.estaVazia():
            raise PilhaException("Lista Vazia")
        dado_removido = self.__topo.get_dado()
        self.__topo = self.__topo.get_proximo()
        
        self.__tamanho -= 1
        return dado_removido
        
    def topo(self):
        if self.estaVazia():
            raise PilhaException("Pilha esta vazia")
        return self.__topo.get_dado()
        
    def esvaziar(self):
        self.__topo = None
        self.__tamanho = 0
        
    def __str__(self) -> str:
        if self.estaVazia():
            return "Pilha: []"
        string_pilha = "Pilha: [ (topo) "
        no_atual = self.__topo
        while no_atual != None :
            string_pilha += f"{no_atual.get_dado()} -> "
            no_atual = no_atual.get_proximo()
        string_pilha += "None (Base) ]"
        return string_pilha
def _converter_para_minuscula_manual(char: str) -> str | None:

    MAIUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"

    for c in MINUSCULAS:
        if c == char:
            return char
    indice = 0
    for c_maiuscula in MAIUSCULAS:
        if c_maiuscula == char:
            indice_minuscula_atual = 0
            for c_minuscula in MINUSCULAS:
                if indice_minuscula_atual == indice:
                    return c_minuscula
                indice_minuscula_atual += 1
        indice += 1

    return None

def eh_palindromo(texto_original: str) -> bool:
  
    string_limpa = ""
    for char in texto_original:
        letra_convertida = _converter_para_minuscula_manual(char)

        if letra_convertida is not None:
            string_limpa += letra_convertida 

    if not string_limpa:
        return True

    pilha = Pilha()
    for letra in string_limpa:
        pilha.empilhar(letra)
 
    try:
        for letra in string_limpa:
            letra_da_pilha = pilha.desempilhar()
            if letra != letra_da_pilha:
                return False
    except PilhaException:
        return False

    return True

def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            return "Erro, Digite um numero inteiro válido"
minha_pilha = Pilha()

