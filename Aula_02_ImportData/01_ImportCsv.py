# %% Lendo .csv

import pandas as pd

df = pd.read_csv("../data/clientes.csv" , sep=";")
df
# %% Salvando em .csv

df.to_csv("clientes.csv", index=False) #index=False retira os índices das linhas que são adicionados ao lado do arquivo.

# %% Salvando em .parquet

df.to_parquet("clientes.parquet", index=False)

# %% Lendo arquivo .parquet

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %% Salvando e lendo arquivos em .xlsx

df.to_excel("clientes.xlsx" , index=False) #Salvando

df_3 = pd.read_excel("clientes.xlsx") #Abrindo
df_3

# %%
