segundos = int(input())
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{horas}:{minutos}:{segundos_restantes}")