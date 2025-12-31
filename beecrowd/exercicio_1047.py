def tempo_de_jogo_com_minutos():
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
    inicio_total = hora_inicial * 60 + minuto_inicial
    fim_total = hora_final * 60 + minuto_final

    if fim_total <= inicio_total:
        fim_total += 24 * 60
        
    duracao_total = fim_total - inicio_total
    horas = duracao_total // 60
    minutos = duracao_total % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

tempo_de_jogo_com_minutos()
