import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from utils import salvar_grafico

class AnaliseVendas:
    def __init__(self, caminho_dados):
        self.dados = pd.read_csv(caminho_dados)
        self.dados['Data_Pedido'] = pd.to_datetime(self.dados['Data_Pedido'], dayfirst=True)
        self.dados['Ano'] = self.dados['Data_Pedido'].dt.year

    def explorar_dados(self, salvar=False, mostrar=True):
        
        if mostrar:
            print("\n[INFO] Colunas e tipos:")
            print(self.dados.dtypes)

            print("\n[INFO] Estaticas descritivas:")
            print(self.dados['Valor_Venda'].describe())

            print("\n[INFO] Valores nulos:")
            print(self.dados.isnull().sum())
        if salvar:
            os.makedirs('relatorio', exist_ok=True)

            resumo = pd.DataFrame({
                'Tipo': self.dados.dtypes.astype(str),
                'Valores Nulos': self.dados.isnull().sum()})
            
            desc = self.dados['Valor_Venda'].describe().to_frame().T
            desc.index = ['Estatísticas Descritivas']

            with open('relatorio/resumo_dados.csv', 'w') as f:
                resumo.to_csv(f)
                f.write('\n')
                desc.to_csv(f)

            print(f"\n[✔] Resumo dos dados salvo em 'relatorio/resumo_dados.csv'")

    def maior_venda_off_sup(self, salvar=False):
        df = self.dados[self.dados['Categoria'] == 'Office Supplies']
        total_cidade = df.groupby('Cidade')['Valor_Venda'].sum()
        cidade_maaior = total_cidade.idxmax()
        print(f"\n[RESULTADO] Cidade com maior venda em 'Office Supplies': {cidade_maaior}")
        print(total_cidade.sort_values(ascending=False))

        if salvar:
            os.makedirs('relatorio', exist_ok=True)
            total_cidade.sort_values(ascending=False).to_csv('relatorio/maior_venda_off_sup.csv',
                    encoding='utf-8',
                    sep='|',
                    header=True)

    def total_vendas_datas(self):
        df = self.dados.groupby('Data_Pedido')['Valor_Venda'].sum()
        plt.figure(figsize=(20, 6))
        df.plot(color='viridis')
        plt.title('Total de Vendas por Data do Pedido')
        plt.ylabel('Valor de Venda')
        plt.xlabel('Data do Pedido')
        plt.tight_layout()
        plt.show()

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