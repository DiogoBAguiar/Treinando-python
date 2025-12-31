a,b,c = input().split()
a,b,c = float(a), float(b), float(c)
delta = (b * b) - (4 * a * c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + delta**0.5) / (2 * a)
    r2 = (-b - delta**0.5) / (2 * a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
