"""while True:
    type_cha=int(input())
    if 0 < type_cha < 5:
        break
soma_total = 0
for i in range(5):
    while True:
        participante_cha = int(input())
        if 0 < participante_cha < 5:
           break
    if type_cha == participante_cha:
        soma_total += 1

print(soma_total)  """ 

type_cha = int(input())
respostas = list(map(int, input().split()))
print(respostas.count(type_cha))
  