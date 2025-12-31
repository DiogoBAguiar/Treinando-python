estados_validos = {"AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"}
contagem = {unidade: 0 for unidade in estados_validos}

qtd_pessoas = int(input("Quantas pessoas serão entrevistadas? "))

for i in range(1, qtd_pessoas + 1):
    while True:
        estado = input(f"Pessoa {i}: para qual estado do Nordeste deseja ir (sigla)? ").strip().upper()

        if estado in estados_validos:
            contagem[estado] += 1
            print(f" Registro de {estado} efetuado com sucesso.\n")
            break
        else:
            print(" Estado inválido. Tente novamente.\n")

print("\n Resultado das entrevistas:\n")
for unidade, total in sorted(contagem.items()):
    print(f"{unidade}: {total} pessoa(s)")
