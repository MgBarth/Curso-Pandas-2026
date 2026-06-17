"""
Acessando dados de páginas web.

Site: https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil

Neste caso, utilizamos headers para 'burlar' o acesso
ao site, pois estava retornando o erro 'HTTP Error 403: Forbidden'.
O pandas de forma tradicional, manda uma requisição
com identificação de User-Agent genérica, que o servidor
recusa por segurança, pois representa uma requisição
automatizada. Por conta disso, simulamos um navegador
real através do 'headers'.
"""
# %%

import pandas as pd
import requests

# %% Requisição ao site para acesso aos dados

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {"User-Agent":"Mozilla/5.0"}

resposta = requests.get(url, headers=headers)

# %% Lendo arquivo HTML com pandas
"""
Aqui, o pandas retorna como sendo cada lista um arquivo
que está indexado no site.
"""

df = pd.read_html(resposta.text)
df

# %% Acessando a tabela separadamente
"""
Podemos acessar separadamente através dos índices de
nossa variável, identificando cada arquivo de dados, até
chegar na tabela desejada.
"""

df_uf = df[1]
df_uf
# %% Salvando como .csv

df_uf.to_csv("uf.csv", sep=";", index=False)

# %%
