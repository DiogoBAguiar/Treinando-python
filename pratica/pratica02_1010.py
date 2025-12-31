codigo01,quantidade01,valor01=input().split()
codigo02,quantidade02,valor02=input().split()
codigo01,quantidade01,codigo02,quantidade02=int(codigo01),int(quantidade01),int(codigo02),int(quantidade02)
valor01,valor02=float(valor01),float(valor02)
valor_total=quantidade01*valor01+quantidade02*valor02
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")