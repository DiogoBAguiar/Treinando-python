import pandas as pd
from typing import Dict, List, Union

class AnalisadorDeDados:
    
    def __init__(self, caminho_arquivo: str):
        
        self.caminho_arquivo = caminho_arquivo
        self.df: Union[pd.DataFrame, None] = None
        self.colunas_numericas: List[str] = []
        self.colunas_categoricas: List[str] = []

    def carregar_e_limpar_dados(self) -> bool:
       
        try:
            self.df = pd.read_excel(self.caminho_arquivo, header=None, skiprows=1)
            self.df.columns = self.df.iloc[0]
            self.df = self.df.drop(self.df.index[0]).reset_index(drop=True)
            self._converter_tipos_colunas()
            return True
        except FileNotFoundError:
            print(f"Erro: O arquivo não foi encontrado em '{self.caminho_arquivo}'")
            return False
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante o carregamento: {e}")
            return False

    def _converter_tipos_colunas(self):
        """
        Método privado para converter colunas específicas para o tipo numérico.
        """
        colunas_para_converter = [
            'LIMIT_BAL', 'AGE',
            'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
            'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
        ]
        for coluna in colunas_para_converter:
            if coluna in self.df.columns:
                self.df[coluna] = pd.to_numeric(self.df[coluna])

    def descobrir_tipos_colunas(self, limiar_unicos: int = 10):
        """
        Classifica as colunas como numéricas ou categóricas com base nos dtypes
        e em um limiar de valores únicos.
        """
        if self.df is None:
            return

        numericas_inicial = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categoricas_inicial = self.df.select_dtypes(include=['object']).columns.tolist()

        if 'ID' in numericas_inicial:
            numericas_inicial.remove('ID')

        colunas_para_mover = [
            col for col in numericas_inicial if self.df[col].nunique() < limiar_unicos
        ]

        self.colunas_categoricas = categoricas_inicial + colunas_para_mover
        self.colunas_numericas = [col for col in numericas_inicial if col not in colunas_para_mover]

    def gerar_resumo_numerico(self) -> Union[pd.DataFrame, None]:
        """
        Gera o resumo estatístico (describe) para as colunas numéricas.

        Returns:
            pd.DataFrame: Um DataFrame com o resumo estatístico.
        """
        if self.df is not None and self.colunas_numericas:
            return self.df[self.colunas_numericas].describe().T
        return None

    def gerar_contagem_categorica(self) -> Union[Dict[str, pd.Series], None]:
        """
        Gera a contagem de frequência (value_counts) para as colunas categóricas.

        Returns:
            Dict[str, pd.Series]: Um dicionário onde as chaves são os nomes das
                                  colunas e os valores são Series do pandas com as contagens.
        """
        if self.df is not None and self.colunas_categoricas:
            return {col: self.df[col].value_counts() for col in self.colunas_categoricas}
        return None

    def verificar_dados_faltantes(self) -> int:
        """
        Verifica e retorna o número total de células com dados faltantes.

        Returns:
            int: O número total de valores nulos no DataFrame.
        """
        return self.df.isnull().sum().sum() if self.df is not None else 0

# --- Bloco de Execução e Apresentação ---
def apresentar_relatorio(analisador: AnalisadorDeDados):
    """
    Coordena a chamada dos métodos de análise e imprime um relatório formatado
    no console.
    """
    print("Iniciando a análise exploratória de dados...")
    print("\n" + "="*50)
    print("ETAPA 1: CARREGAMENTO E LIMPEZA DOS DADOS")
    print("="*50)

    if not analisador.carregar_e_limpar_dados():
        print("Falha ao carregar os dados. Abortando a análise.")
        return

    print("Dados carregados e limpos com sucesso!")

    print("\n" + "="*50)
    print("ETAPA 2: DESCOBERTA E CLASSIFICAÇÃO DE COLUNAS")
    print("="*50)
    analisador.descobrir_tipos_colunas()
    print(f"Colunas Numéricas Identificadas: {analisador.colunas_numericas}")
    print(f"Colunas Categóricas Identificadas: {analisador.colunas_categoricas}")

    print("\n" + "="*50)
    print("ETAPA 3: GERAÇÃO DO RELATÓRIO DE ANÁLISE")
    print("="*50)

    # Obter e apresentar o resumo numérico
    resumo_numerico = analisador.gerar_resumo_numerico()
    if resumo_numerico is not None:
        print("\n--- Resumo Estatístico das Colunas NUMÉRICAS ---")
        print(resumo_numerico)

    # Obter e apresentar a contagem categórica
    contagem_categorica = analisador.gerar_contagem_categorica()
    if contagem_categorica is not None:
        print("\n--- Contagem de Frequência das Colunas CATEGÓRICAS ---")
        for coluna, contagem in contagem_categorica.items():
            print(f"\n--- Contagem para a coluna: {coluna} ---")
            print(contagem)

    # Obter e apresentar a verificação de dados faltantes
    total_faltantes = analisador.verificar_dados_faltantes()
    print("\n--- Verificação de Dados Faltantes ---")
    if total_faltantes == 0:
        print("Ótima notícia: Não há dados faltando no dataset!")
    else:
        print(f"Atenção: Há um total de {total_faltantes} células com dados faltantes.")


if __name__ == "__main__":
    caminho_do_arquivo = r'c:\Users\Diogo Bruno\OneDrive\Área de Trabalho\aprendendo-pyton\estudo_ciencia_de_dados\exercicio_01\default_of_credit_card_clients.xls'
    
    analisador_de_credito = AnalisadorDeDados(caminho_do_arquivo)
    
    apresentar_relatorio(analisador_de_credito)

