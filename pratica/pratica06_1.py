def calculate_average(total_sum, count): 
    avg = total_sum / count
    return avg

qtd_people = int(input("Digite a quantidade de pessoas: "))
list_names = []
list_age = []
sum_age = 0  

for i in range(qtd_people):
    name = input("Digite o nome: ")
    list_names.append(name)
    age = int(input("Digite a idade: "))
    list_age.append(age)
    sum_age += age 

if qtd_people > 0: 
    avg_age = calculate_average(sum_age, qtd_people)
    print(f"\nA idade média é: {avg_age:.2f}") 

    print("\nPessoas mais velhas que a média:")
    found_older = False
    for i in range(qtd_people):
        if list_age[i] > avg_age:
            print(list_names[i])
            found_older = True
    if not found_older:
        print("Nenhuma pessoa é mais velha que a média.")
else:
    print("Nenhuma pessoa foi inserida.")