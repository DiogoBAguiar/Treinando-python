def somar(a,b):
    somar=a+b
    binario=bin(somar)
    octal=oct(somar)
    decimal=somar
    hexal=hex(somar)
    print(binario,octal,decimal,hexal,sep="\n")
def subtrair(a,b):
    subtrair=a-b
    binario=bin(subtrair)
    octal=oct(subtrair)
    decimal=subtrair
    hexal=hex(subtrair)
    print(binario,octal,decimal,hexal,sep="\n")
def multiplicacao(a,b):
    multiplicacao=a*b
    binario=bin(multiplicacao)
    octal=oct(multiplicacao)
    decimal=multiplicacao
    hexal=hex(multiplicacao)
    print(binario,octal,decimal,hexal,sep="\n")
def divisao(a,b):
    if b==0:
        print("ERRO")
    else:
     divisao=a/b
     binario=bin(divisao)
     octal=oct(divisao)
     decimal=divisao
     hexal=hex(divisao)
     print(binario,octal,decimal,hexal,sep="\n")
                
    
n1=int(input("Digite um número decimal:"),2)
n2=int(input("Digite um número decimal:"),2)
operador=input("Digite a função:")
if operador=="+":
    somar(n1,n2)
if operador=="-":
    subtrair(n1,n2) 
if operador=="*":
    multiplicacao(n1,n2)  
if operador=="/":
    divisao(n1,n2)
                  