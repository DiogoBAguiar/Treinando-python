class soma:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @property
    def num1(self):
        return self.x
    
    @property
    def num2(self):
        return self.y
    
    def soma_impares_entre_eles(self):
        maior = max(self.num1, self.num2)
        menor = min(self.num1, self.num2)
        soma_total = 0
        for i in range(menor + 1 ,maior):
            if i%2 != 0 :
                soma_total += i 
        return soma_total        
        
n1 = int(input())   
n2 = int(input())

calculo = soma(n1,n2)
print(calculo.soma_impares_entre_eles()) 