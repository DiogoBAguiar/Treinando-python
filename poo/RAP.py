def calcular_rap_por_unidade(df, unidade):
    df_unidade = df[df['unidade_academica'] == unidade]
    df_alunos = df_unidade[df_unidade['tipo_dado'] == 'aluno'].copy()
    df_professores = df_unidade[df_unidade['tipo_dado'] == 'professor'].copy()
    df_alunos['equivalente'] = df_alunos['quantidade'] * df_alunos['fator_ponderacao']
    df_professores['equivalente'] = df_professores['quantidade'] * df_professores['fator_ponderacao']
    total_alunos_equivalente = df_alunos['equivalente'].sum()
    total_professores_equivalente = df_professores['equivalente'].sum()
    if total_professores_equivalente > 0:
        rap = total_alunos_equivalente / total_professores_equivalente
    else:
        rap = 0
        
    return {
        "unidade_academica": unidade,
        "total_alunos_equivalente": round(total_alunos_equivalente, 4),
        "total_professores_equivalente": round(total_professores_equivalente, 4),
        "rap_calculada": round(rap, 4)
    }