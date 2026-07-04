"""
Fazendo de forma mais performática o exercício '03_Merge.py'.
"""
# %%

import pandas as pd

# %% Puxando dataset's

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

transacoes_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacoes_produto.head()

produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()

# %% Filtrando df de produtos e realizando dois merge's e um group by ao mesmo tempo

produtos = produtos[(produtos["DescNomeProduto"] == "Presença Streak")]

df_streak = (transacoes.merge(transacoes_produto ,on="IdTransacao",how='inner')
                       .merge(produtos, on="IdProduto", how='inner')
                       .groupby(by="IdCliente", as_index=False)["IdTransacao"]
                       .count()
                       .sort_values(by="IdTransacao", ascending=False)
)

df_streak

# %%
"""
Passamos primeiro pelo filtro para captarmos o produto
que queremos analisar, depois realizamos os merge's para
juntar as informações que precisamos, e por fim agrupamos
para identificar nosso cliente com maior número de
transações em Streak's.
"""