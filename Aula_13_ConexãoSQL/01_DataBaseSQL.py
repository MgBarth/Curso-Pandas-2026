# %%

import pandas as pd
import sqlalchemy #Biblioteca usada para conexão com banco de dados e também para ORM.

# %%
"""
Aqui definimos a engine para termos acesso ao nosso banco de
dados. No nosso caso, podemos passar somente o caminho em que
se encontra nosso arquivo (o caminho deve ser antecedido por
'sqlite:///').

Caso fosse um arquivo MySQL, precisaríamos passar o endereço do
banco de dados, o usuário, a senha, a porta e o database
para conseguir a conexão.

Então para cada banco de dados nós utilizamos uma string de conexão
diferente (ou como também chamamos, utilizamos a 'url').

Para sabermos as tabelas presentes no banco de dados, podemos
solicitar pelo terminal 'bash' rodando o arquivo da seguinte forma:

sqlite3 nome_do_arquivo *enter*

.tables *enter*
"""

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%
"""
Aqui, estamos passando o nome da tabela em nosso database ('table_name=')
e a conexão com o banco ('base='), para acessar essa tabela.
"""

clientes = pd.read_sql_table(table_name="tb_customers", con=engine)
clientes.shape