"""
Não costuma ser bom realizarmos conexões com uma tabela inteira,
pois a tabela pode ter milhares ou milhões de linhas e a memória
pode ser esgotada, ou a rede pode ser superaquecida, ou o próprio
banco pode travar por ter que escanear toda a tabela.
"""
# %%

import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%

query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100
