# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %% Convertendo o tipo de uma variável

df["qtdePontos"].astype(float) #Converte para float. Retorna uma serie.
df["qtdePontos"].astype(str)   #Converte para string. Retorna uma serie.
df["qtdePontos"].astype(bool)  ##Converte para booleano. Retorna uma serie.

# %% Alterando linhas com valores 'inválidos'
"""
Utilizamos o método '.replace()' para alterar um valor recorrente que possa
estar errado ou atrapalhando nossa análise, tratamento ou limpeza de dados.

Passamos um dicionário dentro dele onde a chave é o dado que está nos
atrapalhando e o valor é pelo que queremos substituí-lo em nosso df.

Nesse caso, o problema estava sendo gerado quando tentávamos passar a
função 'pd.to_datetime()' para formatar as datas em nosso df. As linhas
com valor de '0000-00-00 00:00:00.000' estavam retornando erro, pois é
um valor inválido para a data. O ERRO NÃO ESTAVA NOS VALORES NULOS, E
SIM NESSE VALOR EM ESPECÍFICO.

O dataset que baixamos já estava com este problema resolvido, por isso
deixei apenas como exemplo para ficar claro.
"""

df["DtCriacao"].replace(
    {
        "0000-00-00 00:00:00.000" : "2024-02-01 00:00:00.000"
    }
)

# %%
