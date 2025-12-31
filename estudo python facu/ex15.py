import math
b = float(input("Digite o valor de um cateto:  "))
c = float(input("Digite o valor do outro cateto:  "))   

# Calcula o ��ngulo entre o cateto e a hipotenusa
a = math.sqrt(b**2 + c**2)
print ("O valor da hipotenusa é:{:.2f} ".format(a))
