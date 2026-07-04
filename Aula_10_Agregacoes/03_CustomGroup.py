"""
Criando um método/função de forma manual e aplicando em nosso agrupamento.
"""

# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
"""
Criando método/função para calcular a amplitude e a distância
da amplitude para a média, elevando esse valor ao quadrado
e depois tirando sua raíz.

sqrt( (amplitude - média) ** 2 )

Para usar o método 'sqrt', importamos o NumPy
"""

def diff_amp(x : pd.Series):
    
    amplitude = x.max() - x.min()
    media = x.mean()

    return np.sqrt((amplitude - media) ** 2)

def life_time(x: pd.Series):

    dt = pd.to_datetime(x)

    return (dt.max() - dt.min()).days

# %%

summary = (transacoes.groupby(by="IdCliente", as_index=False)
                    .agg({
                        "IdTransacao" : ["count"],
                        "QtdePontos" : ["sum", "mean", diff_amp],
                        "DtCriacao" : [life_time]
                    }))

summary

# %% Renomeando colunas para remover o MultiIndex

summary.columns = [
    "IdCliente",
    "QtdeTransacoes",
    "QtdePontos",
    "Pontos/Transacao",
    "DesvioPadrao",
    "LifeTime"
]

summary

# %%
