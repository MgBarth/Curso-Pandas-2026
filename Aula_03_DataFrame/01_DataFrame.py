"""
Explorando DataFrames
"""

# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%
"""
As vezes trabalhamos com uma quantidade muito grande de
dados, onde se pedirmos para mostrar todo o dataframe,
podemos estar utilizando uma quantidade muito grande
do espaço da memória do computador. Para contornarmos
isso e ainda conseguirmos saber se o dataframe foi
gerado da forma correta, utilizamos os métodos
'.head()' para nos retornar as 5 primeiras linhas de nosso
dataframe, ou o '.tail()' para nos retornar as 5 últimas
linhas de nosso dataframe. Também existe o '.sample()'
que retorna 1 linhas aleatória do dataframe.
"""
df_clientes.head()
df_clientes.tail()
df_clientes.sample()

# %%
"""
Ou podemos direcionar quantas linhas queremos que nos
retorne, da seguinte maneira:
"""

df_clientes.head(n=10)
df_clientes.tail(n=7)
df_clientes.sample(n=20)

# %%
"""
Quantas linhas e colunas há em meu dataframe?

Como sei o nome das colunas e os índices do meu dataframe?
"""

df_clientes.shape #Retorna nº de linhas e colunas.

df_clientes.columns #Nome das colunas
df_clientes.index #Índices do dataframe

# %%
"""
Retorna o quanto o dataframe ocupa da sua memória RAM.
Tamém retorna algumas características de cada coluna
do dataframe, como os tipos de variáveis.

O parâmetro "memory_usage='deep'" que passamos dentro do
'.info()' faz retornar não somente uma estimativa de
quanto de nossa memória o dataframe está utilizando, mas
sim o valor exato.
A estimativa costuma ter um grande erro associada,
por isso a importância desse parâmetro.
"""

df_clientes.info(memory_usage='deep')

# %%
"""
Para retornar quais os tipos de variável de cada coluna
utilizamos o atributo '.dtypes' em nosso dataframe.
Ele irá retornar uma series, onde o índice é o nome
da coluna e o valor é o tipo de variável.
Podemos pedir o tipo apenas de uma coluna, basta passá-la
como índice para consultar apenas ela.
"""

df_clientes.dtypes
df_clientes.dtypes["DtCriacao"] #Variável 'O' refere-se ao
                                #tipo 'object', que normal-
                                #mente é string, mas pode
                                #ser uma lista, tupla, etc.