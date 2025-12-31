num = 0
print("A - Aumentar")
print("D - Diminuir")
print("S - Sair")
codigo=input('Informe o código: ') 
while codigo!="A" and codigo!="D" and codigo!="S":
    print("Código inválido")
    codigo=input('Informe o código: ')
while codigo == 'A' or codigo == 'D' or codigo == 'S': 
    if codigo == 'A':
        num += 1
    elif codigo == 'D':
        num -= 1
    elif codigo == 'S':
        break    
    print("Número atual:", num)
    print("A - Aumentar")
    print("D - Diminuir")
    print("S - Sair")
    codigo=input('Informe o código: ')   

        
print("Número final:", num)  


  
    