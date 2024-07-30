'''Questão 1: Leitura e Manipulação de Arquivos CSV. 

Você recebeu um arquivo CSV chamado “transacoes.csv” contendo informações sobre transações financeiras. Usando o arquivo como base, escreva um script em Python que: 

1) Leia o arquivo CSV. 

2) Calcule e imprima o valor total das compras e vendas. 

3) Calcule a quantidade de compras e a quantidade de vendas. 

4) Salve o arquivo ordenado por data, de maneira decrescente. 

----==RESPOSTA=----
'''

#Estarei utilizando a biblioteca Pandas para a manipulação do .CSV

import pandas as pd

#Lendo o arquivo transacoes (3).csv
data_frame = pd.read_csv('transacoes (3).csv')


#Calculando os valores de Compra e Venda.

compras_df = data_frame[data_frame['Tipo']=='Compra']
vendas_df = data_frame[data_frame['Tipo']=='Venda']

valor_total_compras = compras_df['Valor'].sum()
valor_total_vendas = vendas_df['Valor'].sum()

#Calculando a quantidade de Compras e Vendas.

quantidade_compras = len(data_frame[data_frame['Tipo'] == 'Compra'])
quantidade_vendas = len(data_frame[data_frame['Tipo']=='Venda'])

#Aqui estou salvando o novo arquivo ordenado por data de maneira decrescente.

novo_data_frame = data_frame.sort_values(by='Data', ascending=False)
novo_data_frame_local = 'transacoes(Ordenadas).csv'

novo_data_frame.to_csv(novo_data_frame_local, index=False)


#Saída final contendo os dados processados.
print(f'''
      
      O Arquivo foi ordenado e salvo em: transacoes(Ordenadas).csv

      -----=Output=-----
    {vendas_df}
    -Valor Total das compras: R$ {valor_total_compras}
    -Valor Total das Vendas: R$ {valor_total_vendas} 
    -Quantidade de Compras: {quantidade_compras}
    -Quantidade de Vendas: {quantidade_vendas}

''')

#Coloquei esse input para que caso o código seja executado via terminal do Python, ele não acabe abrindo e fechando instantaneamente, assim o mesmo só irá fecar após pressionar ENTER
input("Pressione ENTER para finalizar o código")