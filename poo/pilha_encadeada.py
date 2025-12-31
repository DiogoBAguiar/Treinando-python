"""Escreva um programa que use uma pilha para determinar se uma
string é um palíndromo (isto é, tem a mesma leitura no sentido
normal e no sentido inverso). O programa deve ignorar espaços em
branco, pontuação e caracteres especiais."""

class Pilha:
    def __init__(self):
        self._dados = []

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        if not self.esta_vazia():
            return self._dados.pop()

    def esta_vazia(self):
        return len(self._dados) == 0

    def topo(self):
        if not self.esta_vazia():
            return self._dados[-1]

    def __str__(self):
        return str(list(reversed(self._dados)))


class VerificadorPalindromo:
    def __init__(self, frase):
        self.frase = frase
        self.pilha = Pilha()

    def verificar(self) -> bool:
        
        frase_formatada = ''.join(ch for ch in self.frase if ch.isalnum()).lower()
        
        for letra in frase_formatada:
            self.pilha.empilhar(letra)
        
        frase_invertida = ''
        while not self.pilha.esta_vazia():
            frase_invertida += self.pilha.desempilhar()
        
        return frase_formatada == frase_invertida

    def __str__(self):
        if self.verificar():
            return f'A frase "{self.frase}" é um palíndromo.'
        else:
            return f'A frase "{self.frase}" não é um palíndromo.'

while True:
    print('Digite "sair" para encerrar.')
    frase = input('Digite uma frase: ')
    if frase.lower() == 'sair':
        print('Encerrando o programa...')
        print("-"*50)
        break
    print(VerificadorPalindromo(frase))
    
    
