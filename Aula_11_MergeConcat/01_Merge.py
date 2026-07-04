"""
Trabalhando com duas bases de dados diferentes, simultaneamente.

Vamos explorar a base de transações e a base de clientes
para que possamos tirar alguns insights.

Inner Join => traz apenas os registros que existem nas duas tabelas.
Resumo: A ∩ B.

Left Join => traz todos os registros da tabela da esquerda,
mesmo sem correspondência. As linhas sem correspondência irão aparecer
com valores nulos para os não encotrados na tabela da direita.
Resumo: Todos de A + os que casarem em B.

Rigth Join => traz todos os registros da tabela da direita,
mesmo sem correspondência. As linhas sem correspondência irão aparecer
com valores nulos para os não encotrados na tabela da esquerda.
Resumo: Todos de B + os que casarem em A.

Full Join => Traz todos os registros das duas tabelas.
Resumo: A ∪ B (todo mundo).

"""
# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %% Realizando LEFT JOIN (Merge no python) nas bases. A chave estrangeira é o 'IdCliente'.

clientes = clientes.rename(columns={
    "idCliente" : "IdCliente",
    "qtdePontos" : "QtdePontos"
})
#Renomeamos para deixar o nome das colunas iguais.

transacoes.merge(right=clientes,
                 how='left',
                 on=["IdCliente"]).head()
#Aqui, as colunas que possuem o mesmo nome aparecem identificadas
#com '_x' e '_y' para cada respectiva coluna. Para alterar esse
#sufixo criado, podemos identifica-lo com o parâmetro 'suffixes='.

# %%

transacoes.merge(
    right=clientes,                    # Identificando a outra tabela
    how='left',                        # Tipo de Join
    on=["IdCliente"],                  # Chave estrangeira (chave em comum das tabelas)
    suffixes= ['Transacao', 'Cliente'] # Sufixos para nomear caso hajam colunas com nomes iguais mas que representem coisa diferentes.
).head()

# %%

