
lista_produtos = []
soma_dos_precos = 0.0
print("-" * 30)
QUANTIDADE_PRODUTOS = int(input("Quantos produtos deseja cadastrar? "))
print("-" * 30)
print(f"Por favor, insira os dados para {QUANTIDADE_PRODUTOS} produtos.")
print("-" * 30)
for i in range(QUANTIDADE_PRODUTOS):
    print(f"\n Inserindo dados do Produto #{i+1}")
    while True:
        try:
            codigo = int(input("   Digite o código (número inteiro): "))
            break
        except ValueError:
            print("   ERRO: O código deve ser um número inteiro. Tente novamente.")
    descricao = input("   Digite a descrição: ")
    while True:
        try:
            preco_str = input("   Digite o preço (ex: 6.50): ").replace(',', '.')
            preco = float(preco_str)
            if preco >= 0: 
                break
            else:
                print("   ERRO: O preço não pode ser negativo. Tente novamente.")
        except ValueError:
            print("   ERRO: Valor de preço inválido. Tente novamente.")
    soma_dos_precos += preco
    produto = (codigo, descricao, preco)
    lista_produtos.append(produto)
if lista_produtos:
    media_precos = soma_dos_precos / len(lista_produtos)
    maior_preco = max(p[2] for p in lista_produtos)
else:
    media_precos = 0
    maior_preco = 0

print("\n" + "=" * 40)
print("          ANÁLISE DOS PRODUTOS")
print("=" * 40)
print("\n Descrição do(s) produto(s) mais caro(s):")
encontrou_caro = False
for produto in lista_produtos:
    if produto[2] == maior_preco:      
        print(f"   - {produto[1]}")
        encontrou_caro = True
if not encontrou_caro:
    print("   Nenhum produto cadastrado.")

print(f"\n Códigos dos produtos com preço abaixo da média (R$ {media_precos:.2f}):")

encontrou_barato = False
for produto in lista_produtos:
    if produto[2] < media_precos:
        print(f"   - Código: {produto[0]}")
        encontrou_barato = True
if not encontrou_barato:
    print("   Nenhum produto encontrado com preço abaixo da média.")

print("\n" + "=" * 40)
print("Programa finalizado.")