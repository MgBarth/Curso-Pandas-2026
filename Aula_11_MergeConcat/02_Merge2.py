"""
Realizando o merge sem renomear as colunas!!
"""
# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.columns.to_list()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.columns.to_list()

# %%
"""
Dessa forma, não precisamos colocar o parâmetro 'on=', pois
as colunas já estão especificadas no 'left_on=' e 'right_on='.
"""

transacoes.merge(
    right=clientes, left_on="IdCliente", right_on="idCliente",
    how='inner',
    suffixes= ['Transacao', 'Cliente']
)