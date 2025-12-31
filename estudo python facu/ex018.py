import math
ângulo = float(input('digite um angulo qualquer : '))
seno = math.sin(math.radians(ângulo))
print('O angulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))