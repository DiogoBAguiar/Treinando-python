n1 = float(input('preço do produto: ')) 
n2 = float(input('desconto em % : '))
n3 = n1 - (n1 * n2 / 100)
print('o preço do produto com desconto é de R${}'.format(n3))