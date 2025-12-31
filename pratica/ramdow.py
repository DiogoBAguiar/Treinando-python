import ramdow
"""list = ["Brunna","Eduarda","Clara","Rebecca","Elyza","Nely","Clara"]
print(ramdow.list)"""

def selecionar_nome():
    x = int(input("Quantos nomes gostaria de inserir? "))
    nomes = []
    
    for _ in range(x):
        nome = input("Digite o nome :")
        nomes.append(nome)
    nome_selecionado = ramdow.choice(nomes)   
    print(f"O nome selecionado é : ({nome_selecionado})") 

selecionar_nome()    