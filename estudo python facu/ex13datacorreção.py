from datetime import datetime

def obter_data(mensagem):
    while True:
        try:
            data_str = input(mensagem)
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("Formato inválido! Use o formato dd/mm/yyyy.")

def obter_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número válido.")

def calcular_preco(data1, data2, km_inicial, km_final):
    dias_alugados = (data2 - data1).days
    km_percorridos = km_final - km_inicial
    preco_total = dias_alugados * 60 + km_percorridos * 0.15
    return dias_alugados, km_percorridos, preco_total

data1 = obter_data("Digite a data inicial (formato: dd/mm/yyyy): ")
data2 = obter_data("Digite a data final (formato: dd/mm/yyyy): ")
km_inicial = obter_float("Digite a quilometragem inicial: ")
km_final = obter_float("Digite a quilometragem final: ")

if data2 < data1:
    print("Erro! A data final não pode ser antes da data inicial.")
elif km_final < km_inicial:
    print("Erro! A quilometragem final não pode ser menor que a inicial.")
else:
    dias, km, preco = calcular_preco(data1, data2, km_inicial, km_final)
    print(f"O cliente alugou por {dias} dia(s) e rodou {km} km.")
    print(f"O valor a pagar é de R${preco:.2f}")
