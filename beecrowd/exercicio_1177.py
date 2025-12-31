t = int(input())
n = []
if t<2 or t> 50:
   t=int(input()) 
for i in range(1000):
    valor_a_ser_inserido = i % t
    n.append(valor_a_ser_inserido)
    print(f"N[{i}] = {valor_a_ser_inserido}")  