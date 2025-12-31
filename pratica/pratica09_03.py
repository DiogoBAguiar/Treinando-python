produtos = []
qtd_produtos = int(input("Quantos produtos serão cadastrados? "))
for i in range(1, qtd_produtos + 1):
    print(f"\nProduto {i}")
    codigo = int(input("Digite o código do produto: "))
    descricao = input("Digite a descrição do produto: ").strip()
    preco = float(input("Digite o preço do produto: R$ "))
    
    produtos.append((codigo, descricao, preco))

maior_preco = max(produto[2] for produto in produtos)

mais_caros = [p[1] for p in produtos if p[2] == maior_preco]

media_preco = sum(p[2] for p in produtos) / len(produtos)

abaixo_media = [p[0] for p in produtos if p[2] < media_preco]

print("\n_____Resultado_____ \n")
print(f"\nProduto(s) mais caro(s) - R$ {maior_preco:.2f}:")
for i in mais_caros:
    print(f"- {i}")

print(f"\nMédia de preços: R$ {media_preco:.2f}")
print("Códigos dos produtos com preço abaixo da média:")
for f in abaixo_media:
    print(f"- {f}")
