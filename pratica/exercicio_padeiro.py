def circulo(r: float) -> float:
    """
    Calcula a área de um círculo.
    """
    return 3.14 * r * r
def quadrado(l: float) -> float:
    """
    Calcula a área de um quadrado.
    """
    return l * l

def main():
    print("Produção de pastéis")
    
    """Solicita ao usuário o tamanho do lado da travessa quadrada e a diagonal da forma redonda"""
    lado_travessa = float(input("Informe o lado da travessa (em cm): "))
    diagonal_forma = float(input("Informe a diagonal da forma redonda (em cm): "))

    """Calcula o lado do quadrado interno da forma redonda"""
    lado_quadrado_interno = diagonal_forma / (2 ** 0.5)

    """O diâmetro da forma é igual ao lado do quadrado interno"""
    diametro = lado_quadrado_interno
    raio = diametro / 2

    """Calcula quantas formas cabem por linha e no total na travessa"""
    quantidade_por_linha = int(lado_travessa // diametro)
    quantidade_total = quantidade_por_linha ** 2

    """Calcula as áreas da travessa e da forma redonda"""
    area_travessa = quadrado(lado_travessa)
    area_forma = circulo(raio)

    """Calcula área ocupada e a área desperdiçada"""
    area_ocupada = quantidade_total * area_forma
    area_desperdicada = area_travessa - area_ocupada

    
    print("\n___RESULTADO_FINAL__")
    print(f"Total de formas : {quantidade_total}")
    print(f"Área da travessa : {area_travessa:.2f} cm²")
    print(f"Área de uma forma redonda : {area_forma:.2f} cm²")
    print(f"Área desperdiçada : {area_desperdicada:.2f} cm²") 
    print(f"Área útil : {area_ocupada:.2f} cm²")

if __name__ == "__main__":
    main() 
