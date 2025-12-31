for quadrado in range(11):
    print(f"{quadrado}²=", quadrado * quadrado)

for cubo in range(11):
    print(f"{cubo}³=", cubo * cubo * cubo)

for raiz_quadrada in range(101):
    print(f"Raiz quadrada de {raiz_quadrada}= {raiz_quadrada**0.5 :.2f}")    
   
#---------------------------------------------------
# Se qtd for maiusculo(QTD), será um valor constante que não deve ser mudado
qtd = 4 
soma = 0
qtde_valido = 0
for i in range(qtd):
    valor = int(input('Valor:'))
    soma += valor
    if valor >= 0 and valor <= 100:
        qtde_valido += 1
media = soma / qtd  
print(f"qtd_validos={qtde_valido}")  
print(f"Soma={soma}")
print(f"Media={media:.2f}")    
#----------------------------------------------------
for i in range (10,-1,-1):
    print(i)
#----------------------------------------------------
soma_media = 0
for i in range (3):
    soma = 0
    print("turma", i+1)
    qtd = int(input('Quantidade de aluno: '))
    qtd_al
    for j in range(qtd):
        print('aluno',j+1)
        nota = int(input(f"Nota->Turma {i+1} Aluno {j+1}:")) 
        soma_aluno += nota
        soma += nota
    media = soma/qtd
    soma_media += media
    print(media) 
media_geral_turma = soma_media/3
media_geral_aluno = soma_aluno

print(f"Media geral: {media_geral_turma:.2f}")        
