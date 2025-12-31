#Fraude ou não ?
n = int(input("Digite a quantidade de produtos:"))
qtd_fraude = 0
qtd_valido = 0
for i in range(n):
    print("Produto", i+1)
    produto = input("Produto: ")
    valor = float(input("Valor: "))
    valor_promocao = float(input("Valor promocao: "))
    if valor_promocao > valor*0.9:
        print("Fraude")
        qtd_fraude += 1
    else:
        print("Produto valido")
        qtd_valido += 1 
        
print(f"Quantidade de produtos validos: {qtd_valido}")
print(f"Quantidade de produtos fraudulentos: {qtd_fraude}")     
    