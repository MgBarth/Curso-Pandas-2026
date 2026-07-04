"""
Quem teve mais transação de Streak?

Streak => No caso é o nome de um produto ('Presença Streak')
"""
# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%

transacoes_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacoes_produto.head()

# %%

produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()

# %%

transacoes_total = transacoes.merge(
    right=transacoes_produto,
    left_on="IdTransacao", right_on="IdTransacao",
    how='inner',
    suffixes=["Transacao", "TransacaoProduto"]
)
transacoes_total

# %%

transacoes_total = transacoes_total[[
    'IdTransacao',
    'IdCliente',
    'IdProduto',
    'QtdeProduto'
]]

transacoes_total.head()

# %%

df_merge = transacoes_total.merge(
    right=produtos,
    left_on="IdProduto", right_on="IdProduto",
    how='inner'
)

df_merge = df_merge[[
    'IdTransacao',
    'IdCliente',
    'IdProduto',
    'QtdeProduto',
    'DescNomeProduto',
]]

df_merge

# %%

filtro = (df_merge["DescNomeProduto"] == "Presença Streak")
df_merge = df_merge[filtro]
df_merge

# %%

df_streak = (df_merge.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]]
                     .count()
                     .sort_values(by="IdTransacao", ascending=False)
)

df_streak