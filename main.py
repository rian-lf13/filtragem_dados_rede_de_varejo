import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt


dados = pd.read_csv('dados.csv')
dados.shape
dados.head()
dados.tail()


# AnáliseExplporatória
dados.columns
dados.dtypes
dados['Valor_Venda'].descriibe()
dados[dados.duplicated()]
dados.isnull().sum()
dados.head()

#Filtrando os dados (Maior valor de venda de produtos "Office Supplies")

officesuplies_maiorvenda = dados[dados['Categoria'] == 'Office Supplies']
office_supplies_total = officesuplies_maiorvenda.groupby('Cidade')('Valor_Venda').sum()
cidade_maior_ven_ofsup = office_supplies_total.idxmax()
print(f'A cidade com maior venda de produtos "Office Supplies" é: {cidade_maior_ven_ofsup}')
office_supplies_total.sort_values(ascending=False)


