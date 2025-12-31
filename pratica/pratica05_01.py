#programa principal
quantidade = 1
mumero = int (input("Número: "))
maior = 0

while quantidade < 5:
    numero = int (input("Número: "))
    if numero > maior:
        maior = numero
    quantidade += 1    
print(numero , maior)  

# codigo principal (While true) 
quantidade = 1
numero = int (input("Número: "))
maior = 0
while True:
    numero = int (input("Número: "))
    if numero > maior:
        maior = numero
    quantidade += 1
    if quantidade == 5:
        break 
print(numero , maior)

#codigo principal (for) 
quantidade = 1
numero = int (input("Número: "))
maior = 0
for i in range(5):
    numero = int (input("Número: "))
    if numero > maior:
        maior = numero
    quantidade += 1
print(numero , maior)   