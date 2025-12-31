valor_compra_dolar = float(input("Qual o valor em Dolar do produto? US$"))
uss_rs = float(input("Qual a cotação do Dolar Americano para o Real? R$"))
convercao = valor_compra_dolar*uss_rs
taxa_importacao = convercao*0.2
icms = convercao*0.17
valor_total = convercao + taxa_importacao + icms
print(f"O valor do produto em reais é de {convercao:.2f}.")
print(f"A taxa de importação é de R${taxa_importacao:.2f}")
print(f"O ICMS é de R${icms:.2f}")
print(f"O valor total com taxas e impostos será de R${valor_total:.2f}")
