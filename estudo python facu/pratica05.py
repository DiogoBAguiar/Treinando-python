valor_produto = float(input("Digite o valor do produto: "))
valor_a_vista = valor_produto*0.9
valor_parcelado = valor_produto*1.2
valor_parcela = valor_parcelado/4
print(f"O valor do produto é R${valor_produto:.2f}." )
print(f"Se for à vista valerá R${valor_a_vista:.2f}." )
print(f"Se for diretamente no cartão de crédito à vista valerá R${valor_produto:.2f}." )
print(f"Se for parcelado ficará R${valor_parcelado:.2f} e cada parcela será de R${valor_parcela:.2f}.")