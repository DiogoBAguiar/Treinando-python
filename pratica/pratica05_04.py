#Quem chegou primeiro?
qtd_atletas = int(input("Digite a quantidade de atletas: "))

while qtd_atletas < 1:
    print("Quantidade de atletas deve ser maior que 0")
    qtd_atletas = int(input("Digite a quantidade de atletas: "))
    
atleta_mais_rapido = 0
competidores = 0     
for i in range(qtd_atletas):
    print("Atleta", i+1)
    atleta = input("Nome do atleta: ")
    hora,minuto,segundo = input("Digite o tempo do atleta (hh:mm:ss): ").split(":")
    hora,minuto,segundo = int(hora),int(minuto),int(segundo)
    print(f"Atleta {atleta} - Tempo: {hora}:{minuto}:{segundo}")
    tempo = hora*3600 + minuto*60 + segundo
    if tempo < 3600*2 :
        menor_tempo = tempo
        atleta_mais_rapido = atleta
        competidores += 1
    else:
        print("Atleta desclassificado")
if competidores > 0:
    print(f"Atleta mais rapido: {atleta_mais_rapido}")
    print(f"Menor tempo: {menor_tempo//3600}:{(menor_tempo%3600)//60}:{menor_tempo%60}")
    
    
    
    
   