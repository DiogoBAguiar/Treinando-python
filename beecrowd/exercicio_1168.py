QTD_LEDS_NUMEROS = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}
def calcular_leds(numero):
    total_leds = 0
    for digito in numero:
        total_leds += QTD_LEDS_NUMEROS[digito]
    return total_leds
numero_casos = int(input())
for _ in range(numero_casos):
    numero = input().strip()
    leds = calcular_leds(numero)
    print(f"{leds} leds")