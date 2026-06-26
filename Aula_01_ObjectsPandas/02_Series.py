# %%

import pandas as pd

idades = [
    35,
    34,
    25,
    24,
    52,
    45,
    34
]

# %% Modo sem pandas

media = sum(idades) / len(idades)
print(f"A média de idades é {idades}.")

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades) - 1)

print(f"""
A média é igual a {media}.
A variância é igual a {variancia}.
""")

# %% Transformando a lista em Serie para que possamos realizar calculos de forma simples.

series_idades = pd.Series(idades)
series_idades

"""
Os valores que estão dentro da serie sempre serão do
mesmo tipo. Ou seja, se há uma string no meio dos int's,
tudo será considerado como string.
Com as series, temos métodos que podemos utilizar,
para calcular estatísticas de nosso conjunto de dados
por exemplo. Um dos exemplos é o de cálculo da média,
onde fazermos 'serie.mean()' e nos retorna a média de
nossa serie.
"""

# %% Com pandas

media_idades = series_idades.mean()
variancia_idades = series_idades.var()

print(f"""
A média é igual a {media_idades}.
A variância é igual a {variancia_idades}.
""")

# %% Método 'describe' para retornar um sumário de nossa serie.

summary_idades = series_idades.describe()
print(f"""
Segue um resumo estatístico básico de nossos dados:
{summary_idades}
""")

#O valor de 'std' que retorna é o valor do desvio padrão.
# %%
