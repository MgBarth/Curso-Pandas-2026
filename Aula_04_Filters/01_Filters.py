# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.info(memory_usage='deep')

# %% Exemplo para explicação pt.1

exemplo = pd.DataFrame({
    "Nome" : ["Miguel", "Ronaldo", "Eduarda", "Jeferson"],
    "Idade" : [24 , 15, 27, 16],
    "UF" : ["SC" , "RJ", "SP", "SP"]
})

filtro = exemplo['Idade'] >= 18
filtro #Retorna uma serie com os valores booleanos

# %% Exemplo para explicação pt.2
"""
Aqui, passamos uma serie com a mesma dimensão do df (mesmo tamanho)
com valores booleanos. Quando passamos como posição, o df retorna
apenas as posições das quais tem como valor 'True', assim
filtrando nosso df através da condição aplicada no filtro.

Se passarmos uma serie de dimensão diferente, iria nos retornar
um ValueError.
"""

exemplo[filtro]

# %% Voltando aos nossos dados reais, QtdePontos >= 50
# SELECT *
# FROM df
# WHERE QtdePontos >= 50

filtro1 = df['QtdePontos'] >= 50

df[filtro1]

# %% QtdePontos between 50 & 100
# não sei escrever isso em SQL
"""
(condição 1) & (condição 2) & ...

Esse comando exige que todas as condições especificadas
sejam verdadeiras para que o booleano seja 'True'.
"""

filtro2 = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)

df[filtro2]

# %% QtdePontos igual a 1 ou maior que 100 / == 1 | == 100
"""
(condição 1) | (condição 2) | ...

O comando '|' significa 'ou'. Ou seja, se uma das condições
forem verdadeiras, o valor booleano atribuído será "True".
"""

filtro3 = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro3]