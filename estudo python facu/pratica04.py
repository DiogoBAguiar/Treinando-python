valor_gasto = float(input("Quanto o cliente gastou?"))
numero_cupom = valor_gasto//20
numero_cupom = numero_cupom*2
resto = valor_gasto%20
valor_para_20 = 20 - resto
print(f"A quantidade de cupons que o cliente receberá é de {numero_cupom:.2f}")
print( f"Faltam R${valor_para_20:.2f} para ganhar mais 2 cupons")