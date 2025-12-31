while True:
    numero = int(input("Digite um número positivo (ou 0 para sair): "))
    
    if numero == 0:
        print("Encerrando o loop")
        break
    
    if numero < 0:
        print("Número negativo não é valido.")  
    
    print("Você digitou:", numero)
