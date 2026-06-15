# %%

import pandas as pd

idades = [
    35, 34, 25, 26, 28, 32,
    24, 24, 28, 47, 55, 42,
    52, 45, 34, 31, 23, 29
]

series_idades = pd.Series(idades)
series_idades = series_idades.sort_values() #Ordena os dados do menor para o maior.

# %% Consultando dados por posição de series/dataframes
"""
Para as series, os índices funcionam da mesma maneira
que as chaves nos dicionários. Ou seja, não conseguimos
acessar o último valor com o comando '[-1]', pois não
existe a chave '-1'.

Caso a serie seja reordenada, o índice '0'
pode deixar de ser o primeiro dado, pois ele segue
seu respectivo valor (relação chave:valor).

Para conseguirmos acessar os índices como posição e
não como chaves, utilizamos o método '.iloc', onde aí
sim podemos colocar o índice como posição,
e não como chave de um valor.

Com o '.iloc' estamos ignorando os índices e buscando
nas linhas dos dados, em resumo.
"""

print(f"""
Serie das idades ordenada:
{series_idades}

Chamando índice como chave:
      Chave 0: {series_idades[0]}
Chamando índice como posição: 
      Posição 0: {series_idades.iloc[0]}
      Posição -1: {series_idades.iloc[-1]}
      (Sim, com o .iloc podemos chamar a posição -1, pois não estamos tratando como chave.)
""")
# %% Para indexar chaves aos valores

nomes = [
    "Eduardo", "Maria", "Miguel", "Carolina", "Pietra", "Karino",
    "Miguel", "Julia", "Graziele", "Vitoria", "Lucas", "Sabrina",
    "Gabriel", "João", "Katia", "Edson", "Victor", "Nathalia"
]

series_nomes_idades = pd.Series(idades, index=nomes)
print(series_nomes_idades)
# %% Acessando pelo index e posição

print(f"""
Pela posição:
{series_nomes_idades.iloc[-1]}

Pelo index:
{series_nomes_idades['Miguel']}
""")
# %% Diferença de .iloc e .loc
"""
O '.iloc' utilizamos para navegar nas linhas de nosso
dataframe ou serie, enquanto o '.loc' utilizamos para
navegar através dos índices.
"""
