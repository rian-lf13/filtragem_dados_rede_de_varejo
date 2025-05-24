import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import salvar_grafico

class AnaliseVendas:
    def __init__(self, caminho_dados):
        self.dados = pd.read_csv(caminho_dados)
        self.dados['Data_Pedido'] = pd.to_datetime(self.dados['Data_Pedido'], dayfirst=True)
        self.dados['Ano'] = self.dados['Data_Pedido'].dt.year

    def explorar_dados(self):
        print("\n[INFO] Colunas e tipos:")
        print(self.dados.dtypes)
        print("\n[INFO] Estáticas descritivas:")
        print(self.dados['valor_Venda'].describe())
        print("\n[INFO] Valores nulos:")
        print(self.dados.isnull().sum())

    def total_vendas_estado(self, salvar= False):
        df = self.dados.groupby('Estado')['Valor_Venda'].sum().reset_index()
        plt.figure(figsize=(16, 6))
        sns.barplot(data=df, 
                    x='Estado',
                    y='Valor_Venda',
                    hue= 'Estado', 
                    palette='husl',
                    legend=False)
        plt.title('Total de Vendas por Estado')
        plt.xticks(rotation=45)
        if salvar:
            salvar_grafico('grafico/vendas_por_estado.png')
        else:
            plt.show()