tempo_gasto = int(input())
velocidade_media = int(input())
distancia_percorrida = tempo_gasto * velocidade_media
litros_consumidos = distancia_percorrida / 12
print(f"{litros_consumidos:.3f}")