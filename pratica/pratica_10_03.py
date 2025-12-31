while True:
    codigo = int(input())  
    if codigo == 0:
        break  

    resultados = list(map(int, input().split()))

    mary_wins = resultados.count(0) 
    john_wins = resultados.count(1)  

    print(f"Mary won {mary_wins} times and John won {john_wins} times")
