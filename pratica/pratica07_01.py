# 1. Inicializa uma lista vazia para guardar os números
numeros_escolhidos = []
quantidade_total = 6

print(f"Por favor, digite {quantidade_total} números distintos entre 1 e 60.")

# 2. Loop para pedir números até a lista ter 6 itens
while len(numeros_escolhidos) < quantidade_total:
    try:
        entrada_str = input(f"Digite o {len(numeros_escolhidos) + 1}º número: ")
        numero_atual = int(entrada_str)

        # 3. Validações
        # Verifica se o número está fora do intervalo
        if not (1 <= numero_atual <= 60):
            print("Erro: O número precisa estar entre 1 e 60. Tente novamente.")
        
        # Verifica se o número já existe na lista
        elif numero_atual in numeros_escolhidos:
            print("Erro: Este número já foi escolhido. Tente novamente.")
        
        # Se passou nas validações, adiciona o número à lista
        else:
            numeros_escolhidos.append(numero_atual)
            print(f"-> Número {numero_atual} adicionado!")

    except ValueError:
        # Caso o usuário não digite um número inteiro
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        break # Interrompe o loop se o usuário pressionar Ctrl+C

# 4. Ordena a lista de números em ordem crescente
numeros_escolhidos.sort()

# 5. Exibe o resultado final
print("\n------------------------------------")
if len(numeros_escolhidos) == quantidade_total:
    print("Os 6 números escolhidos foram:")
    print(numeros_escolhidos)
else:
    print("A seleção de números não foi concluída.")
print("------------------------------------")
        
