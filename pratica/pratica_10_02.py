combustiveis = {
    1: "Alcoól",
    2: "Gasolina",
    3: "Diesel",
    4: "Fim"
}
contadores = {
    1: 0,
    2: 0,
    3: 0
}
while True:
    codigo = int(input())
    if codigo == 4:
        break
    elif codigo not in combustiveis:
        continue
    else:
        if codigo in contadores:
            contadores[codigo] += 1
print("MUITO OBRIGADO")
print(f"Alcoól: {contadores[1]}")
print(f"Gasolina: {contadores[2]}")
print(f"Diesel: {contadores[3]}")
    