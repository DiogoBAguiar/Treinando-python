dia_01 = int(input().split()[1])
hora_01, minuto_01, segundo_01 = map(int, input().split(" : "))
dia_02 = int(input().split()[1])
hora_02, minuto_02, segundo_02 = map(int, input().split(" : "))
if dia_02 < dia_01 :
    print("Digite um numero valido")
    dia_01 = int(input().split()[1])
    hora_01, minuto_01, segundo_01 = map(int, input().split(" : "))
    dia_02 = int(input().split()[1])
    hora_02, minuto_02, segundo_02 = map(int, input().split(" : "))    
    
tempo_em_segundos_01 = (dia_01 * 24 * 3600) + (hora_01 * 3600) + (minuto_01 * 60) + segundo_01
tempo_em_segundos_02 = (dia_02 * 24 * 3600) + (hora_02 * 3600) + (minuto_02 * 60) + segundo_02
tempo_total = tempo_em_segundos_02 - tempo_em_segundos_01
qtd_dias = tempo_total // (24 * 3600)
tempo_total %= (24 * 3600)
numero_horas = tempo_total // 3600
tempo_total %= 3600
numero_minutos = tempo_total // 60
numero_segundos = tempo_total % 60
print(f"{qtd_dias} dia(s)")
print(f"{numero_horas} hora(s)")
print(f"{numero_minutos} minuto(s)")
print(f"{numero_segundos} segundo(s)")
