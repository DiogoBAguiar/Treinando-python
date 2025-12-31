#cartoes do brasileirao
numero_rodadas = int(input("Número de rodadas: "))
numero_jogos = int(input("Número de jogos por rodada: "))

for rodada in range(1, numero_rodadas + 1):
    print(f"\nRodada {rodada}")
    total_amarelos = 0
    total_vermelhos = 0
    for jogo in range(1, numero_jogos + 1):
        print(f"Jogo {jogo}")
        cartoes_amarelos = int(input("Quantidade de cartões amarelos: "))
        cartoes_vermelhos = int(input("Quantidade de cartões vermelhos: "))
        total_amarelos += cartoes_amarelos
        total_vermelhos += cartoes_vermelhos
    print(f"Total de cartões amarelos na rodada {rodada}: {total_amarelos}")
    print(f"Total de cartões vermelhos na rodada {rodada}: {total_vermelhos}")