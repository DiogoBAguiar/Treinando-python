def duracao_jogo():
    inicio, fim = map(int, input().split())

    if inicio == fim:
        duracao = 24
    elif inicio < fim:
        duracao = fim - inicio
    else:
        duracao = (24 - inicio) + fim

    print(f"O JOGO DUROU {duracao} HORA(S)")

duracao_jogo()
