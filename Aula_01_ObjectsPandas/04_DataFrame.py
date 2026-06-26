# %%

import pandas as pd

idades = [
    35, 34, 25, 26, 28, 32,
    24, 24, 28, 47, 55, 42,
    52, 45, 34, 31, 23, 29
]

nomes = [
    "Eduardo", "Maria", "Miguel", "Carolina", "Pietra", "Karino",
    "Miguel", "Julia", "Graziele", "Vitoria", "Lucas", "Sabrina",
    "Gabriel", "João", "Katia", "Edson", "Victor", "Nathalia"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%
"""
Pode-se imaginar, de forma didática, o dataframe como
um varal, ao qual escolhemos o que estendemos nele
para que possamos enxergar.

O DataFrame nada mais é que um conjunto de series (caso haja mais de uma).
Funciona como uma planilha de excel, onde possui linhas e colunas.
A planilha é o DataFrame e cada coluna é uma serie.
"""


df = pd.DataFrame() #DataFrame vazio
df["Idades"] = series_idades #"Penduramos" as idades.
df["Nomes"] = series_nomes #"Penduramos" os nomes.
df

# %% Navegando em minha planilha: Acessando uma coluna específica

df["Idades"] # Retorna uma serie

# %% Navegando em minha planilha: Acessando todas as infosd de uma linha específica

df.iloc[0] # Retorna uma serie onde os índices se tornam as variáveis (colunas)

df.iloc[0]["Idades"] # Retorna uma serie com a linha e informação especificada.