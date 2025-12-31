print("Horário de início:")
hi, mi, si = int(input("Hora: ")), int(input("Minuto: ")), int(input("Segundo: "))
print("Horário de Término:")
hf, mf, sf = int(input("Hora: ")), int(input("Minuto: ")), int(input("Segundo: "))
inicio = hi * 3600 + mi * 60 + si
fim = hf * 3600 + mf * 60 + sf
duracao = (fim - inicio) % (24 * 3600)
h = duracao // 3600
m = (duracao % 3600) // 60
s = duracao % 60
print(f"Tempo de uso da máquina: {h} hora(s), {m} minuto(s) e {s} segundo(s).")

