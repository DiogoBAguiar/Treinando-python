def tipos_triangulo():
    a, b, c = map(float, input().split())
    if a >= b and a >= c:
        A = a
        B, C = (b, c) if b >= c else (c, b)
    elif b >= a and b >= c:
        A = b
        B, C = (a, c) if a >= c else (c, a)
    else:
        A = c
        B, C = (a, b) if a >= b else (b, a)
        
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        elif A**2 < B**2 + C**2:
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

tipos_triangulo()
