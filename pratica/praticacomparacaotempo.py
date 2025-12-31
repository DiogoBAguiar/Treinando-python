def resultado(a,b):
    
    if a<b:
        diferenca = b-a
        hora = diferenca //3600
        minuto = diferenca % 3600 // 60
        segundo = diferenca % 3600 % 60
        print(f"Jogador 1 ganhou com vantagem de {hora:02}h{minuto:02}m{segundo:02}s")
    elif a>b:
        diferenca = a-b
        hora = diferenca //3600
        minuto = diferenca % 3600 // 60
        segundo = diferenca % 3600 % 60
        print(f"Jogador 2 ganhou com vantagem de {hora:02}h{minuto:02}m{segundo:02}s")
    else:
        print("Empataram")
        
hora1,minuto1,segundo1=input("Digite a Hora, os segundos e os minutos do jogador 01:").split()
hora2,minuto2,segundo2=input("Digite a Hora, os segundos e os minutos do jogador 02:").split()
hora1,minuto1,segundo1=int(hora1),int(minuto1),int(segundo1)
hora2,minuto2,segundo2=int(hora2),int(minuto2),int(segundo2)
tempo_jogador_01 = hora1*3600 + minuto1*60 + segundo1
tempo_jogador_02 = hora2*3600 + minuto2*60 + segundo2

resultado(tempo_jogador_01,tempo_jogador_02)
    
    
    