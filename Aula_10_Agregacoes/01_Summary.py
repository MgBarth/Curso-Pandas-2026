# %%

import pandas as pd

idades = [22, 44, 55, 23, 36, 54, 60, 71, 51, 21]
idades = pd.Series(idades)
idades

"""
Podemos ver as agregações como uma forma de 'espremer'
nosso conjunto de dados.

Podemos dizer também como:
Calcular uma estatística de nossos dados.

Sumarização:
Sumarização de dados é o processo de agrupar, condensar
e simplificar grandes volumes de informações.
O objetivo é transformar dados brutos e complexos em resumos
estruturados e fáceis de entender, focando apenas nos pontos
essenciais para facilitar análises e tomadas de decisão rápidas.
"""
# %% Retorna uma lista de estatísticas de uma serie (Sumarização)

idades.describe()

# %%
"""
Trabalhando com os dataset's de exemplo
"""

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %% Estatísticas

clientes["flTwitch"].sum() #Total de usuários da Twitch em nosso dataset

clientes["flTwitch"].mean() #Nesse caso, representa a proporção de clientes que usam twitch

# %% Calculando a proporção de usuários de cada rede social na nossa base de clientes (nesse caso a média representa a proporção por ser 0's e 1's)
"""
Importante entender, quando solicitamos uma agregação de uma
serie, ele retorna o valor da serie.
Se solicitamos uma agregação de um DataFrame, ele retorna a
agregação de cada coluna do DataFrame separadamente, como o
caso abaixo.

Isso pode agilizar muitos processos.
"""

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].mean()

# %% Como filtrar as colunas que não são numéricas para tirar estatísticas
"""
Passo-a-passo do raciocíonio da filtragem para chegarmos na
lista de colunas que são valores calculáveis.
"""

clientes.dtypes == "object" #-> Filtro

clientes.dtypes[(clientes.dtypes == "object")] #Retorna apenas as colunas do tipo object

clientes.dtypes[~(clientes.dtypes == "object")] #O '~' nega o (clientes.dtypes == "object"), como um 'if not'.

clientes.dtypes[~(clientes.dtypes == "object")].index #Retorna os índices da serie (nesse caso, as próprias colunas)

clientes.dtypes[~(clientes.dtypes == "object")].index.to_list() #Retorna a lista que queremos, pois acima está retornando uma variável do tipo 'index'.


# %%

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.to_list()

clientes[num_columns].mean()

# %% .describe() em mais de uma coluna:

clientes[num_columns].describe()