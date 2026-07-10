"""
Comandos para rodar query pelo VScode:

Ctrl + Shift + P -> Digite 'sqlite: Open Database' -> Selecionar a opção de DataBase desejada (arquivo .db)

Ctrl + Shift + Q -> Rodar query
"""
# %%

import pandas as pd
import sqlalchemy

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

# %% 