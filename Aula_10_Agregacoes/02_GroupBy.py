# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

# %% Método .groupby()
"""
Retorna a contagem de cada coluna agrupado por cada "IdCliente".
"""

transacoes.groupby(by=["IdCliente"]).count()

# %%
"""
Retorna a contagem da coluna "IdTransacao" agrupado por cada "IdCliente"
"""

transacoes.groupby(by=["IdCliente"])["IdTransacao"].count() #Retorna serie
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count() #Retorna dataframe

# %% Caso quisesse que a coluna IdCliente não fosso o índice do df
# Usamos o 'as_index=False' para isso!

transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

# %%
"""
Calculando simultaneamente (ainda por cliente):

# Qtde_transacoes
# Total_pontos
# Pontos / Qtde_transacoes (Média de pontos, ou pontos por transação)

Aqui vamos conhecer a função '.agg()', onde fazemos várias agregações
de forma simultânea, passando tudo pela função. Na função, criamos um
dicionário e nele destacamos o nome da coluna (como chave) e o tipo de
agregação que queremos passar nela (como valor).

Escrevemos os métodos como strings pois esses métodos padrões o pandas
já reconhece, mesmo como strings. Os métodos e funçãos que nós mesmos
criamos ou que sejam de outras bibliotecas devem ser escritos sem
as aspas.
"""

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
                     .agg({"IdTransacao" : ["count"],
                         "QtdePontos" : ["sum", "mean"]
                          }))

summary

# %% 
"""
Quando solicitamos as colunas do nosso df, ele retorna como
'MultiIndex', que representa como se fosse uma hierarquia em
nosso df (como na coluna 'QtdePontos' que possui 'mean' e 'sum').
"""

summary.columns

# %%
"""
Isso costuma ser ruim para se trabalhar, então podemos contornar
isso atribuindo de forma arbritária as colunas da seguinte forma:
"""

summary.columns = ['IdCliente', 'QtdeTransacao', 'QtdePontos', 'Avg_PontosTransacao']
summary