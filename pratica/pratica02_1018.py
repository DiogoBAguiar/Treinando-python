valor = int(input())
notas_100 = int(valor/100)
resto_100 = valor % 100
notas_50 = int(resto_100/50)
resto_50 = resto_100 % 50
notas_20 = int(resto_50/20)
resto_20 = resto_50 % 20
notas_10 = int(resto_20/10)
resto_10 = resto_20 % 10
notas_5 = int(resto_10/5)
resto_5 = resto_10 % 5
notas_2 = int(resto_5/2)
resto_2 = resto_5 % 2
notas_1 = resto_2
print(f"{valor}")
print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")    