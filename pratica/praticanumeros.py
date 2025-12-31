def numero(a,b,c,d):
    
    if a > b and a > c and a>d:
        maior = a
    elif b > c and b > d:
        maior = b
    elif c > d :
        maior = c
    else:
        maior = d 
           
    if a < b and a < c and a < d:
        menor = a
    elif b < c and b < d:
        menor = b
    elif c < d:
        menor = c
    else:
        menor = d

    print(maior)
    print(menor)
    
n1,n2,n3,n4= input().split() 
n1,n2,n3,n4= int(n1),int(n2),int(n3),int(n4)  
numero(n1,n2,n3,n4)
