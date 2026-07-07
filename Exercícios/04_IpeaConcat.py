"""
Vamos trabalhar com alguns dados de homicídios no Brasil,
realizando a concatenação dos dados para que possamos
juntar todos em um mesmo arquivo (em um só dataset).
"""
# %%

import pandas as pd

# %%

df_geral = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df_geral = df_geral.rename(columns={"valor" : "homicidios"})
df_geral.head()

# %%

df_negros = pd.read_csv("../data/ipea/homicidios-negros.csv", sep=";")
df_negros = df_negros.rename(columns={"valor" : "homicidios-negros"})
df_negros.head()

# %%
"""
Para concatenar os dois sem duplicar o nome e período, podemos
indicar o que queremos que o concat identifique como índice
através do método '.set_index()'
"""

df_geral = df_geral.set_index(["nome", "período"])
df_negros = df_negros.set_index(["nome", "período"])

# %% Concatenando

pd.concat([df_geral, df_negros], axis=1)

# %%
