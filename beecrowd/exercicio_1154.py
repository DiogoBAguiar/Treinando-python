soma_idade=0
divisao=0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma_idade+=idade
    divisao+=1
media=(soma_idade)/ divisao   
print(f"{media:.2f}")    