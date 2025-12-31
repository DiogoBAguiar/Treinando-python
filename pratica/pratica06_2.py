qtd_cidades=int(input("Digite a quantidade de cidades participantes : "))
cidades = []
for i in range(qtd_cidades):
    nome_cidade = input(f"Digite o nome da cidade {i+1}: ").strip()
    cidades.append(nome_cidade)
votos = {cidade: 0 for cidade in cidades}
print("\nInício da votação:")
for i in range(100):
    voto = input(f"Voto da pessoa {i+1}: ").strip()
    if voto in votos:
        votos[voto] += 1
    else:
        print("Cidade inválida! Voto não computado.")
max_votos = max(votos.values())
vencedoras = [cidade for cidade, qtd_votos in votos.items() if qtd_votos == max_votos]
print(f"Cidade(s) vencedora(s) com {max_votos} voto(s):")
for cidade in vencedoras:
    print(f"- {cidade}")
