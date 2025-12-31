class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def Area (self):
        return self.base * self.altura

ret = Retangulo(10,6.5)
print ("Area do retangulo é %s"% ret.Area())
print(ret.base)
print(ret.altura)
print(ret)