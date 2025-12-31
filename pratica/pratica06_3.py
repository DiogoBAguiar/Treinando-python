nomes = set()
print("Digite os nomes das pessoas. Para encerrar, digite 'fim'.")
while True:
    nome = input("Digite um nome: ").strip()
    if nome.lower() == "fim":
        break
    nomes.add(nome)
print("\nNomes diferentes que foram digitados:")
for nome in nomes:
    print(f"- {nome}")