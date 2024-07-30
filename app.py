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


#Separando o dataframe de acordo com o tipo (Compra ou Venda)
compras_df = data_frame[(data_frame['Tipo'] == 'Compra')]  

vendas_df = data_frame[(data_frame['Tipo'] == 'Venda')]   
