from analise_vendas import AnaliseVendas

def menu():
    analise= AnaliseVendas('dados/dataset.csv')

    opcoes = {
        '1': analise.explorar_dados,
        '2': analise.maior_venda_off_sup,
        '3': analise.total_vendas_datas
    }

    while True:
        print('''
        \t-[MENU DE ANÁLISE]
        \n[1] - Explorar dados
        \n[2] - Maior venda em "Office Supplies"
        \n[3] - Total de vendas por Data
        \n[4] - Total de vendas por Estado
        \n[5] - 10 cidades com maior venda
        \n[6] - Segmento com maior venda
        \n[7] - Total de vendas por Segmento e Ano
        \n[s] - Sair
        ''')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            analise.explorar_dados(salvar=True)
        elif escolha == '2':
            analise.maior_venda_off_sup(salvar=True)
        elif escolha == 'S' or escolha == 's':
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    menu()