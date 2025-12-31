alcool = 0
gasolina = 0
diesel = 0

while True:
    codigo = int(input())
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break  
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
   

"""contadores = [0, 0, 0, 0]

while True:
    codigo = int(input())
    if 1 <= codigo <= 3:
        contadores[codigo] += 1
    
    elif codigo == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {contadores[1]}")
print(f"Gasolina: {contadores[2]}")
print(f"Diesel: {contadores[3]}")"""
  
    