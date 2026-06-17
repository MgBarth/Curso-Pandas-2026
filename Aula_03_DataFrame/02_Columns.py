
# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %% Linhas e colunas, Memória RAM ocupada, Tipagem de cada coluna

df.shape #Linhas e colunas

df.info(memory_usage="deep") #Memória

df.dtypes #Tipagem

# %% Renomar colunas
"""
No método '.rename()' passamos o parâmetro 'columns={}',
onde dentro do dicionário ({}) passamos a chave da qual
será o nome atual da coluna, e o valor que representará
o novo nome da coluna.

Neste método, ele não altera o dataframe 'df' que temos,
ele cria um novo dataframe porém com a alteração do nome
da coluna que instruímos. Para que ele substitua o df
e ocorra apenas a alteração sem termos dois df's,
escrevemos 'df = df.rename(columns={"antigo":"novo"})'.
"""

df = df.rename(columns={
                        "QtdePontos":"QtPontos",
                        "DescSistemaOrigem":"SistemaOrigem"
                        })
df.dtypes

# %% Renomear colunas (código mais legível)

renamed_columns = {
    "QtdePontos":"QtPontos",
    "DescSistemaOrigem":"SistemaOrigem"
}

df = df.rename(columns=renamed_columns)
df.dtypes

# %% Renomear colunas (sem precisar utilizar 'df = ')
"""
Para que não precisemos reatribuir com 'df = ' podemos
utilizar o parâmetro 'inplace=True', que altera o df
original, sem precisarmos reatribuir da forma que
vinhamos fazendo.
"""

renamed_columns = {
    "QtdePontos":"QtPontos",
    "DescSistemaOrigem":"SistemaOrigem"
}

df.rename(columns=renamed_columns , inplace=True)

df.dtypes

# %% Selecionando colunas em nosso df (errado)

df["IdCliente" ,"QtPontos"] #Retorna KeyError

"""
Não é possível passar dois ou mais 'valores' na consulta
dessa forma, pois retornará um erro de chave, pois o python
está lendo como uma tupla os dois ou mais valores passados.
Para contornar isso, utilizamos colchetes duplos "[[]]",
onde o que passamos como valor é uma lista, onde há dois
valores diferentes, sendo os valores os nomes de nossas
colunas a serem consultadas.
"""

# %% Selecionando colunas em nosso df (correto)

# SELECT IdCliente, QtPontos
# FROM df

df[["IdCliente" ,"QtPontos"]]

# %% Selecionando colunas em nosso df

# SELECT IdCliente, QtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "QtPontos"]].head(n=5) #5 primeiros
df[["IdCliente", "QtPontos"]].tail(n=5) #5 últimos
df[["IdCliente", "QtPontos"]].sample(n=5) #5 aleatórios

# %% Para reordenar as colunas

# SELECT IdCliente, IdTransacao, QtPontos
# FROM df
# LIMIT 5

df[['IdCliente', 'IdTransacao', 'QtPontos']].sample(n=5)

"""
A sequência que descrevemos na consulta do df é exatamente
a ordem que permanecerá no retorno que recebemos.
"""

# %% Ordem alfabética
"""
Primeiro selecionamos somente as colunas (df.columns) e transformamos
em uma lista (list(df.columns)).
Em segundo, ordenamos a lista de forma crescente com o método '.sort()'.
Terceiro e último, reatribuímos a sequência ao próprio df.
"""

colunas = list(df.columns)
colunas.sort() #Esse método ordena uma lista de forma crescente.
colunas #Aqui está a lista ordenada das colunas do df

df = df[colunas] #Atribuindo a lista ordenada ao próprio df
df