n1 = float(input('salario atual:'))
n2 = float(input('aumento em %:'))
n3 = n1 + (n1 * n2 / 100)
print('o novo salario é de R${}'.format(n3))