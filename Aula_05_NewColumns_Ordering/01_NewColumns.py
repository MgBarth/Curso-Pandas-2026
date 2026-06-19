# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %% Criando coluna: Somando 100 na quantidade de pontos de todos os clientes
# Operação com escalar (Valor numérico)

df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %% Reatribuindo e não criando nova coluna
"""
Dessa forma estamos reatribuindo a mesma coluna, ou seja, estamos
substituíndo a coluna original pela coluna com o 100 somado.
"""

df["qtdePontos"] = df["qtdePontos"] + 100
df.head()
# %% Filtrando clientes que tem email OU conta na twitch
# Operação entre duas series

df["email_or_twitch"] = df["flEmail"] + df["flTwitch"]
df.head() #O que tiver resultado igual a 1 ou 2 possui alguma das contas ou as duas contas.

# %% Filtrando clientes que tem email E twitch
# Operação entre duas series

df["email_and_twitch"] = df["flEmail"] * df["flTwitch"]
df.head()

# %% Realizando a operação de logaritmo natural na quantidade de pontos
# Utilizando NumPy.
# Operação com logaritmo
"""
O '+1' é para retirar os valores nulos, que retornariam valor indefinido
pois log de 0 (independente da base) é indefinido!

Essa operação é para reduzir a dispersão dos dados e conseguirmos
enxergar a dispersão deles de uma forma mais clara. A depender da
situação, é uma maneira válida de tratar nossos dados.
"""

df["log_qtdePontos"] = np.log( df["qtdePontos"] + 1 )
df.head()
# %% Comparando dispersões

df["qtdePontos"].describe()
df["log_qtdePontos"]. describe()

#--------------------------------------------------------------------------------------------------------------------------------------
# %% Plotando histograma df["qtdePontos"]

import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()

# %% Plotando histograma df["log_qtdePontos"]

plt.hist(df["log_qtdePontos"])
plt.grid(True)
plt.show()
# %%
