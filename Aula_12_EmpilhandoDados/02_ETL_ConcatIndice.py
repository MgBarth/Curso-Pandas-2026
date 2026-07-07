"""
Aqui vamos entender com mais clareza como podemos utilizar
o '.concat' com 'axis=1', enquanto manipulamos o que será
utilzado como índice para concaternarmos de maneira correta
diferentes bases de dados que possam ser relacionadas
(pelo ano e local, por exemplo).

No exemplo vamos utilizar, queremos que o índice seja as
colunas 'nome' e 'período' dos nossos dataset's, pois é o
que podemos cruzar de dados.
Para fazer isso, utilizamos o método '.set_index(["nome", "período"])'
"""
# %%

import pandas as pd

#%% Esse código é apenas explicativos, não rodamos.

# Passo-a-passo lógico para o tratamento necessário em cada dataset:

df_geral = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df_geral = df_geral.rename(columns={ "valor" : "homicidios"})
df_geral = df_geral.set_index(["nome", "período"])
df_geral = df_geral.drop("cod", axis=1)
df_geral.head()

# %% Começamos a solução a partir daqui

# Criando uma função para aplicar isso em cada um dos dataset's,
# para automatizar:

def read_file(file_name:str):

    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep=";")
            .rename(columns={ "valor" : file_name})
            .set_index(["nome", "período"])
            .drop("cod", axis=1))

    return df

# %%
"""
Para não precisar passar documento por documento anexando
em uma variável para aplicar a função, podemos fazer com
a biblioteca 'os' com o método '.listdir()', da seguinte forma:
"""

import os

file_names = os.listdir("../data/ipea/") #Lista todos os arquivos dentro da pasta que endereçamos.

dfs = []
for i in file_names:

    file_name = i.split(".")[0] #Para separar o '.csv' e selecionar apenas o nome sem o tipo de arquivo

    dfs.append(read_file(file_name))

# Aqui criamos uma lista com todos os dataframes. Agora, basta concatenar.

# %%

pd.concat(dfs, axis=1)

# Utilizamos o '.reset_index()' para fazer com que o 'nome' e 'período'
# voltem a ser colunas, para que possamos ordenar através deles.

df_final = (pd.concat(dfs, axis=1).reset_index()
              .sort_values(['período', 'nome']))

df_final.to_csv("homicidios-consolidado.csv", index=False, sep=";") #Salvando planilha final.
