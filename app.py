'''Questão 1: Leitura e Manipulação de Arquivos CSV. 

Você recebeu um arquivo CSV chamado “transacoes.csv” contendo informações sobre transações financeiras. Usando o arquivo como base, escreva um script em Python que: 

1) Leia o arquivo CSV. 

2) Calcule e imprima o valor total das compras e vendas. 

3) Calcule a quantidade de compras e a quantidade de vendas. 

4) Salve o arquivo ordenado por data, de maneira decrescente. '''


#Estarei utilizando a biblioteca Pandas para a manipulação do .CSV
#pip install pandas

import pandas as pd

#Lendo o arquivo transacoes (3).csv
data_frame = pd.read_csv('transacoes (3).csv')


#Calculando os valores de Compra e Venda.

valor_total_compra = data_frame[data_frame['Tipo']=='Compra']['Valor'].sum()
valor_total_venda = data_frame[data_frame['Tipo']=='Venda']['Valor'].sum()

#Calculando a quantidade de Compras e Vendas.

quantidade_compras = len(data_frame[data_frame['Tipo'] == 'Compra'])
quantidade_vendas = len(data_frame[data_frame['Tipo']=='Venda'])

#Salvando o arquivo ordenado por data de maneira decrescente.

novo_data_frame = data_frame.sort_values(by='Data', ascending=False)
novo_data_frame_local = 'transacoes(Ordenadas).csv'

novo_data_frame.to_csv(novo_data_frame_local, index=False)



print(f'''
      
      O Arquivo foi ordenado e salvo em: transacoes(Ordenadas).csv

      -----=Output=-----

    -Valor Total das compras: R$ {valor_total_compra}
    -Valor Total das Vendas: R$ {valor_total_venda} 
    -Quantidade de Compras: {quantidade_compras}
    -Quantidade de Vendas: {quantidade_vendas}
    
''')