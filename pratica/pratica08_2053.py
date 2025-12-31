def cyk(palavra, regras, terminais, variaveis, inicial):
    n = len(palavra)
    tabela = [ [set() for _ in range(n)] for _ in range(n) ]

    for i, c in enumerate(palavra):
        for var in regras:
            if (c,) in regras[var]:
                tabela[i][0].add(var)

    for l in range(1, n):  
        for i in range(n - l):  
            for k in range(l): 
                left = tabela[i][k]
                right = tabela[i + k + 1][l - k - 1]
                for B in left:
                    for C in right:
                        for A in regras:
                            if (B, C) in regras[A]:
                                tabela[i][l].add(A)

    return inicial in tabela[0][n - 1]


def main():
    instancia = 1
    while True:
        try:
            raiz = input().strip()
            if raiz == "":
                continue
            V = input().strip()
            T = input().strip()

            regras = dict()
            for v in V:
                regras[v] = set()

            while True:
                linha = input().strip()
                if linha == "# -> #":
                    break
                A, _, B = linha.partition(" -> ")
                B = B.strip()
                if len(B) == 1:
                    regras[A].add((B,))
                else:
                    regras[A].add(tuple(B))

            print(f"Instancia {instancia}")
            instancia += 1

            while True:
                palavra = input().strip()
                if palavra == "#":
                    break
                if palavra == "":
                    print(" nao e uma palavra valida")
                    continue

                if cyk(palavra, regras, T, V, raiz):
                    print(f"{palavra} e uma palavra valida")
                else:
                    print(f"{palavra} nao e uma palavra valida")

            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()
