lista=[]
positivos = 0
for i in range(6):
    n = float(input())
    lista.append(n)
    if n > 0:
        positivos += 1
print(f"{positivos} valores positivos")        