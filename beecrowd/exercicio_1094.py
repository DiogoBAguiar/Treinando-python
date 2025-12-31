n = int(input())
total = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(n):
    qtd, tipo = input().split()
    qtd = int(qtd)    
    total += qtd   
    if tipo == 'C':
        total_coelhos += qtd
    elif tipo == 'R':
        total_ratos += qtd
    elif tipo == 'S':
        total_sapos += qtd

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")

percentual_coelhos = (total_coelhos / total) * 100
percentual_ratos = (total_ratos / total) * 100
percentual_sapos = (total_sapos / total) * 100

print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
