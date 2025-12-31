palavras = []
while True:
    entrada = input("Digite uma palavra (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break

    palavras.append(entrada)
frase = " ".join(palavras)
print(f"Frase final:{frase}")

