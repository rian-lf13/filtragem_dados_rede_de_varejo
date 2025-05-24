import matplotlib.pyplot as plt
import pandas as pd
import os

def salvar_grafico(caminho):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()

def salvar_relatorio_excel(df, nome_arquivo):
    os.makedirs('relatorios', exist_ok=True)
    caminho = f'relatorios/{nome_arquivo}.xlsx'
    df.to_excel(caminho, index=False)
    print(f'[INFO] Relatório salvo em: {caminho}')   
    