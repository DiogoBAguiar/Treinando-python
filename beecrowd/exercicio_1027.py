import sys
from itertools import groupby

while True:
    try:
        linha = sys.stdin.readline()
        if not linha.strip():
            break
        n = int(linha)

        if n == 0:
            print(0)
            continue
        pontos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
        pontos.sort()
        ondas = {} 
        max_resultado = 1 if n > 0 else 0
        for _, grupo_de_pontos in groupby(pontos, lambda p: p[0]):
            atualizacoes_neste_x = []
            for x, y in grupo_de_pontos:
                eixo_sup = y - 1
                _, comp_baixo_ant = ondas.get(eixo_sup, (0, 0))
                novo_comp_cima = comp_baixo_ant + 1
                atualizacoes_neste_x.append((eixo_sup, 'cima', novo_comp_cima))         
                eixo_inf = y + 1
                comp_cima_ant, _ = ondas.get(eixo_inf, (0, 0))
                novo_comp_baixo = comp_cima_ant + 1
                atualizacoes_neste_x.append((eixo_inf, 'baixo', novo_comp_baixo))
            for eixo, tipo, novo_comp in atualizacoes_neste_x:
                comp_cima_atual, comp_baixo_atual = ondas.get(eixo, (0, 0))
                
                if tipo == 'cima':
                    ondas[eixo] = (novo_comp, comp_baixo_atual)
                else:
                    ondas[eixo] = (comp_cima_atual, novo_comp)
                max_resultado = max(max_resultado, novo_comp)
            
        print(max_resultado)

    except (EOFError, ValueError, IndexError):
        break