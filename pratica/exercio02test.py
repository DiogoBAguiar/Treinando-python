def quadrado(l):
    """Calcula a área de um quadrado."""
    return l * l

def retangulo(b, h):
    """Calcula a área de um retângulo."""
    return b * h

def triangulo(b, h):
    """Calcula a área de um triângulo."""
    return (b * h) / 2

def trapezio(b1, b2, h):
    """Calcula a área de um trapézio."""
    return ((b1 + b2) * h) / 2

def paralelogramo(b, h):
    """Calcula a área de um paralelogramo."""
    return b * h

def losango(d1, d2):
    """Calcula a área de um losango."""
    return (d1 * d2) / 2

def circulo(r):
    """Calcula a área de um círculo ."""
    return 3.14 * r * r

print("_______ TESTES DE ÁREAS _______ ")

"""quadrado"""
print("Quadrado:", quadrado(4))
print("espera-se 16")        

"""retângulo"""
print("Retângulo:", retangulo(5, 2))
print("espera-se 10")  

"""triângulo"""
print("Triângulo:", triangulo(6, 4))
print("espera-se 12")  

"""trapézio"""
print("Trapézio:", trapezio(6, 4, 2))
print("espera-se 20") 

"""paralelogramo"""
print("Paralelogramo:", paralelogramo(5, 3))
print("espera-se 15")  

"""losango"""
print("Losango:", losango(10, 4))
print("espera-se 20")     

"""círculo"""
print("Círculo:", circulo(2))
print("espera-se 12.56")         


