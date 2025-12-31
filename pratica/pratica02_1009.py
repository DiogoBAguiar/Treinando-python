nome = input("")
salario_fixo = float(input(""))
total_vendas_mes = float(input(""))
comissao = total_vendas_mes * 0.15
valor_receber = salario_fixo + comissao
print(f"TOTAL = R$ {valor_receber:.2f}")
