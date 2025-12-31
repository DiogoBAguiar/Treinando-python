def fatorial(n):
    if n == 0:
      return 0
    elif n == 1:
        return 1
    else:
      return n*fatorial(n-1)
def insere_fila(topo, valor):
  p = topo
  
  while (p.proximo != None):
    p = p.proximo
  
  q = No()
  q.dado = valor
  p.proximo = q
  q.proximo = None
    

def soma_ate_N(n):
  if (n < 1):
    print("Erro: Esta função não aceita numeros menores do que 1.")
    return 0
  elif (n == 1):
    return n
  else:
    return (n + soma_ate_N(n - 1))    

def listaAoContrario( no ) :
          if( no.get_proximo() != None ) :
                listaAoContrario( no.get_proximo())
                print ( "{}".format(no.get_dado()))    
  
def hanoi ( n , de , para , aux ) :
    if ( n > 0 ):
        hanoi(n-1, de, aux, para)
        print ("Mova o disco "+str(n)+" de "+de+" para "+para)
        hanoi(n-1, aux, para, de)

hanoi(3, "A", "C", "B")

        