while True:
    try:
        s = input().strip()
    except EOFError:
        break
    if not s:
        continue

    lista_cpf = list(s)  
    partes = ['']   

    for cpf in lista_cpf:
        if cpf == '.' or cpf == '-':
            partes.append('')   
        else:
            partes[-1] += cpf     
    for p in partes:
        print(p)
