class Recursividade:
    def __init__(self,numero):
        self.numero = numero
    
    @property
    def numero(self):
        return self.numero
    
    def Fatorial(self):
        if self.numero == 0:
            return 0
        elif self.numero == 1:
            return 1
        else:
            return self.numero*Fatorial(self.numero-1)

while True:
    try:
        number = int(input())
       
         