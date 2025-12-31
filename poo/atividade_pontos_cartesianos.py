class Ponto:
    def __init__(self,x,y): #__init__ cria uma area de memoria/endereço para aquela determinada variavel
        self.x = x # O init é chamado automaticamente , precisa chamar a class. Ex: ponto1 = Ponto()
        self.y = y # Self.x ou y é de fato o real atributo. Os que estão no __init__(x,y) são o que vem do input
    def Quadrante(self):
        if (self.x == 0 and self.y == 0):
            return "Origem"
        elif (self.x > 0 and self.y > 0):
            return "Q1"
        elif (self.x < 0 and self.y > 0):
            return "Q2"
        elif (self.x < 0 and self.y < 0):
            return "Q3"
        elif (self.x > 0 and self.y < 0):
            return "Q4"
        elif (self.x == 0 and self.y > 0 or self.x == 0 and self.y < 0):
            return "Coordenada no eixo Y"
        elif (self.x > 0 and self.y == 0 or self.x < 0 and self.y == 0):
            return "Coordenada no eixo x"
ponto1 = Ponto(1,2)
print ("Coordenadas do Ponto 1 (%d,%d)"%(ponto1.x,ponto1.y))    
print ('Ponto 1 pertence a(o) %s'%(ponto1.Quadrante()))    
        