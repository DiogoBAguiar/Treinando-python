a,b,c = input().split()
a,b,c = map(int, (a,b,c))
maior_ab = (a + b + abs(a - b)) / 2
maior = (maior_ab + c + abs(maior_ab - c)) / 2
print(f"{maior:.0f} eh o maior")