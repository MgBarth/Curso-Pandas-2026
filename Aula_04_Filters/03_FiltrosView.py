# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %% Quais os clientes que tem 0 pontos?

filtro = clientes["qtdePontos"] == 0

clientes_0 = clientes[filtro]
clientes_0

# %% Tentando criar uma coluna nova

clientes_0["flag_1"] = 1

# %%

clientes_0 #Mostra a nova coluna (como um post-it grudado)
clientes   #Não mostra a nova coluna. Não é acessado.
