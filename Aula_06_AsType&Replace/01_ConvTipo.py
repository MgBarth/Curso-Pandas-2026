# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %% Convertendo o tipo de uma variável

df["qtdePontos"].astype(float) #Converte para float. Retorna uma serie.
df["qtdePontos"].astype(str)   #Converte para string. Retorna uma serie.
df["qtdePontos"].astype(bool)  ##Converte para booleano. Retorna uma serie.

# %% Alterando linhas com valores 'inválidos'
"""
Utilizamos o método '.replace()' para alterar um valor recorrente que possa
estar errado ou atrapalhando nossa análise, tratamento ou limpeza de dados.

Passamos um dicionário dentro dele onde a chave é o dado que está nos
atrapalhando e o valor é pelo que queremos substituí-lo em nosso df.

Nesse caso, o problema estava sendo gerado quando tentávamos passar a
função 'pd.to_datetime()' para formatar as datas em nosso df. As linhas
com valor de '0000-00-00 00:00:00.000' estavam retornando erro, pois é
um valor inválido para a data. O ERRO NÃO ESTAVA NOS VALORES NULOS, E
SIM NESSE VALOR EM ESPECÍFICO.

O dataset que baixamos já estava com este problema resolvido, por isso
deixei apenas como exemplo para ficar claro.
"""

df["DtCriacao"] = df["DtCriacao"].replace(
    {
        "0000-00-00 00:00:00.000" : "2024-02-01 00:00:00.000"
    }
)

# %%
"""
Depois de tratarmos a data na célula anterior, conseguimos
rodar o método 'pd.to_datetime()'.

Assim transformamos o tipo de variável presente na serie de
'object' para 'datetime64[ns]'.
"""

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
df["DtCriacao"]

# %% Como é comum de ser feito no mercado:
"""
Aqui, escrevemos de forma resumida, clara e otimizada o que fizemos
nas duas célular anteriores.

1. Na variável 'replace' que criamos adicionamos todos os valores que
queremos alterar.

2. Aplicamos o replace (a alteração dos valores) dentro da função
'pd.to_datetime'.

3. Passamos o replace dentro da função para converter a variável para o
formato de data.

4. Reatribuímos em nossa serie de data.
"""

replace = {"0000-00-00 00:00:00.000" : "2024-02-01 00:00:00.000"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

# %% Por que é interessante o '.to_datetime':

df["DtCriacao"].dt.date() #Retorna só a data, sem a hora
df["DtCriacao"].dt.day_of_week #Retorna o dia da semana
df["DtCriacao"].dt.year() #Retorna só o ano
df["DtCriacao"].dt.month() #Retorna só o número do mês
df["DtCriacao"].dt.month_name() #Retorna só o nome do mês
df["DtCriacao"].dt.day() #Retorna só o dia

# Entre outros!!!

"""
Transformar a coluna para o tipo de 'datetime' faz com que seja possível
utilizar o atributo '.dt', que nos permite trabalhar de uma forma muito
simples com a data.
"""