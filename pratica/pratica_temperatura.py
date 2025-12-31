def temperatura(a):
    if a<10:
        print("Muito frio")
    elif 10<=a<=15:
        print("Frio")
    elif 16<=a<=25:
        print("Agradável")
    elif 26<=a<=30:
        print("Quente")
    else:
        print("Muito Quente") 

temp=input("Digite a temperatura em ºC:") 
temp=int(temp)
temperatura(temp)                      