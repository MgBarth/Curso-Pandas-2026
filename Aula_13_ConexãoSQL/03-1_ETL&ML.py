"""
Gerando um pseudo modelo de ML para mostrar como exemplo
de como devolvemos um modelo para o banco de dados, para
que possa ser utilizado.
"""
# %%

import pandas as pd
import sqlalchemy

from sklearn import cluster

# %% Para não misturar código SQL com Python, separamos dessa forma:

# Aqui chamamos a query para o Python
with open("03_ETL.sql") as open_file:
    query = open_file.read()

print(query)

# %% Realizando a query através do Python

# Nesse caso, o Python está agindo como orquestrador do SQL.
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

df_query = pd.read_sql_query(query, con=engine)
df_query

# %% Modelo de ML

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df_query[['totalRevenue', 'qtdeSalles']])

df_query["cluster"] = kmean.labels_
df_query

# %% Enviando para o banco de dados:

"""
"sellers_cluster" -> Nome da tabela nova

.to_sql -> Envia um DataFrame para o nosso banco de dados.

'if_exist="replace"' -> Analisa a condição de existência da tabela.
Caso ela já exista, irá excluir a existente e salvar a nova.
Usado para atualizar a tabela, toda a vez que o script for rodado.
Sem o 'if_exist="replace"' o código quebraria, pois já existiria
uma tabela com o mesmo nome, quando fosse atualizar.
"""

df_query.to_sql("sellers_cluster",
                con=engine,
                index=False,
                if_exists="replace")