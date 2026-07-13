"""
Para transformarmos nosso conjunto de dados para o formato wide
ou para o formato long!

Nesse caso, cada métrica é uma coluna em nosso df 'homicidios-consolidado.csv'.
O que vamos fazer é criar um duas colunas, sendo uma identificando
a métrica utilizada ('homicidio-de-jovens-por-armas-de-fogo' por exemplo)
e outra com o valor da métrica propriamente.

De forma geral, estamos reduzindo o número de colunas e aumentando o
número de linhas, assim alterando o formato de nossa tabela, sem alterar
os dados que a compõem. Apenas alteramos a disposição das informações.

O formato long facilita tanto o processo de agrupamento e agregação dos dados,
como também a geração de gráficos para visualização.

Stack -> Empilha a tabela
Unstack -> Desempilha a tabela
"""
# %%

import pandas as pd

df = pd.read_csv("../Aula_12_EmpilhandoDados/homicidios-consolidado.csv", sep=";")
df.head()

# %% Stack
"""
Para transformar nossa tabela para long, precisamos primeiro 'setar' (definir)
os nossos índices que não devem ser alterados. Neste caso, estamos falando
das colunas 'nome' e 'período'.
"""

df = df.set_index(['nome', 'período'])

df_stack = df.stack() # Retorna uma série com as variáveis empilhadas

# Resetando índices para transformar em um DataFrame novamente

df_stack = df_stack.reset_index() #Os índices voltam a ser enumerados e as colunas retornam como chaves.

df_stack.columns = ["nome", "período", "métrica", "total"]

df_stack.head(n=20)

# %% Unstack

df_unstack = (df_stack.set_index(['nome', 'período', 'métrica'])
                      .unstack()
                      .reset_index())

# Gerou um DF com MultiIndex, vamos resolver isso:

metricas = df_unstack.columns.droplevel(0)[2:].to_list()
df_unstack.columns = ["nome", "período"] + metricas

df_unstack.head(20)