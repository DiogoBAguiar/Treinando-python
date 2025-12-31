dicionario = {}
while True:
    nome = input("Digite um nome ou 'fim' para encerrar:").strip().lower()
    if nome == 'fim':
        break
    if nome in dicionario:
        dicionario[nome] += 1
    else:
        dicionario[nome] = 1

print("\n Contagem de nomes:")
for nome, contagem in dicionario.items():
    print(f"{nome}: {contagem}")        
    
    