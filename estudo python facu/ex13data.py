from datetime import datetime

data1_str = input("Digite a data inicial (formato: dd/mm/yyyy): ")
data2_str = input("Digite a data final (formato: dd/mm/yyyy): ")
kminicial = float(input("Digite a quilometragem inicial: "))
kmfinal = float(input("Digite a quilometragem final: "))
data1 = datetime.strptime(data1_str, "%d/%m/%Y")
data2 = datetime.strptime(data2_str, "%d/%m/%Y")
delta_data = data2 - data1
delta_km = kmfinal - kminicial
print('O cliente alugou por {} dia(s) e rodou {} km '.format(delta_data.days, delta_km))
print('O valor a pagar é de R${}'.format(delta_data.days*60 + delta_km*0.15))