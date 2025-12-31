def ler_entrada():
    dados = []
    while True:
        try:
            linha = input()
            if linha == '':
                continue
            dados.extend(linha.strip().split())
        except EOFError:
            break
    return dados

def main():
    data = ler_entrada()
    idx = 0
    cidade = 1
    saida = []

    while True:
        if idx >= len(data):
            break

        N = int(data[idx])
        idx += 1
        if N == 0:
            break

        freq = [0] * 201
        total_pessoas = 0
        total_consumo = 0

        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            c = y // x
            freq[c] += x
            total_pessoas += x
            total_consumo += y

        partes = []
        for consumo in range(201):
            if freq[consumo] > 0:
                partes.append(f"{freq[consumo]}-{consumo}")

        media = total_consumo / total_pessoas
        media_truncada = int(media * 100) / 100
        parte_inteira = int(media_truncada)
        parte_decimal = int(media_truncada * 100) % 100

        bloco = f"Cidade# {cidade}:\n{' '.join(partes)}\nConsumo medio: {parte_inteira}.{parte_decimal:02d}"
        saida.append(bloco)
        cidade += 1

    print('\n\n'.join(saida))

main()

