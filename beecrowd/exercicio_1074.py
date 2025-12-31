while True:
    qtd_numeros =int(input())
    if  qtd_numeros <= 0:
        qtd_numeros = int(input())
    else:
        break

for i in range (qtd_numeros):
    numero=int(input())
    if numero == 0:
        print("NULL") 
    elif numero <=0 :
         if numero%2 != 0:
             print ("ODD NEGATIVE")
         else:
             print ("EVEN NEGATIVE") 
    else:
         if numero%2 != 0:
             print ("ODD POSITIVE")
         else:
             print ("EVEN POSITIVE")                     