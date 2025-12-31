"""
1. Escreva um programa que:
a) crie uma pilha;
b) exiba o seguinte menu de opções:
    EDITOR DE PILHA
    [1] EMPILHAR
    [2] DESEMPILHAR
    [3] EXIBIR ELEMENTO DO TOPO
    [4] EXIBIR A PILHA
    [5] TAMANHO DA PILHA
    [6] ESVAZIAR A PILHA
    [0] SAIR
    DIGITE SUA OPÇÃO:
c) leia a opção do usuário e execute a opção escolhida;
d) após a execução de cada opção, o programa deve retornar ao
menu para nova opção do usuário ou o encerramento do
programa.
"""
class No:
  def __init__(self, dado = None):
    self.__dado = dado
    self.__prox = None

  # get
  @property
  def dado(self):
    return self.__dado

  # set
  @dado.setter
  def dado(self, novo):
    self.__dado = novo

  # get
  @property
  def prox(self):
    return self.__prox

  # set
  @prox.setter
  def prox(self, novo):
    self.__prox = novo

class Pilha:
    def __init__(self):
        self._dados = []

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        if self.esta_vazia() == True:
            return self._dados.pop()

    def esta_vazia(self):
        return len(self._dados) == 0

    def topo(self):
      return self._dados[len(self._dados) - 1]