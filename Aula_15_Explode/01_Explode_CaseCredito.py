# %%

import pandas as pd

df = pd.read_csv("dados_cartao.csv", sep=",")
df

# %%

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df

# %%

df["vlParcela"] = (df["vlVenda"] / df["qtParcelas"]).round(2)
df

# %%

df["ordemParcela"] = df.apply(lambda row : [i for i in range(row['qtParcelas'])], axis=1)
df

# %%
"""
O método explode() é usado para transformar os elementos de uma lista
ou array contidos em uma única célula em linhas separadas.
Ele "desembrulha" a lista, criando uma nova linha para cada item e
duplicando os valores das demais colunas para manter a integridade dos dados.
"""

df_explode = df.explode("ordemParcela")
df_explode

# %%

def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt =  f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode

# %% Agrupamento para informação do valor da parcela no determinado mês

(df_explode.groupby(["IdCliente", "dtParcela"])
           ['vlParcela'].sum()
           .reset_index()
           .pivot_table(index='IdCliente',
                        columns='dtParcela',
                        values='vlParcela',
                        fill_value=0))