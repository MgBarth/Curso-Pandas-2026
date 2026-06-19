# %%

import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df.info(memory_usage='deep')

# %% Consultando os produtos de código 5 e 11
"""
Neste caso o IdProduto é do tipo string e não int, por isso
precisamos colocar os número entre aspas.
"""

filtro1 = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')
df[filtro1]

# %% Mesma consulta que a de cima, mas com o método .isin()

filtro1 = df['IdProduto'].isin(['5' , '11'])
df[filtro1]

# %% Outro dataset para usar .notna (igual a .notnull)

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %% Filtrando apenas clientes com data de criação não nula

filtro = ~df_clientes["DtCriacao"].isna()
filtro = df_clientes["DtCriacao"].notna()
df[filtro]
"""
As duas variáveis são idênticas. O '~' nega a afirmação que está
colocada, invertendo os valores de 'True' e 'False'.
"""

# %%
