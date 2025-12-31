misterio=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range (3):
    print(type(misterio[i]),misterio[i])
    
for i in range (3):
    for j in range (4):
        print(i,j,misterio[i][j])  

#--------------------------------------------------
lista=[0]*4
matriz1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz1)):
    for j in range (len (matriz1[i])) :
        matriz1 [i][j]=1
print(matriz1)        
#---------------------------------------------------
def gerar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    
    for i in range(linhas):
        matriz.append([0]*colunas)  
    return matriz   

notas = gerar_matriz(4,3)  

for i in range (4):
    for j in range(3):
        notas[i][j] = int(input(f'Aluno {i+1} Nota {j+1}'))             