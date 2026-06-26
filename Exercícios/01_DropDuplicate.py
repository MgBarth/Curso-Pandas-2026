# %% Selecione a primeira transação diária de cada cliente

import pandas as pd

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %% Ordenando
"""
Aqui, criamos uma nova coluna com as datas ordenadas de forma
crescente, e após essa ordenação deixamos na coluna apenas
a data (sem horário), onde o primeiro valor é o mais recente
(mais cedo no dia, caso a data seja a mesma).
"""

df = df.sort_values(["IdCliente", "DtCriacao"], ascending=True)
df["Data"] = pd.to_datetime(df["DtCriacao"]).dt.date
df.head()

# %% Dropando
"""
Dropando os clientes e datas duplicados, deixando apenas a
transação mais recente.
"""

df = df.drop_duplicates(keep="first", subset=["IdCliente", "Data"])
df.head()