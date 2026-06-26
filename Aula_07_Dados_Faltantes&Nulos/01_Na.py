# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %% Replace dos dados para passar a função 'pd.to_datetime()'

replace = {
    "0000-00-00 00:00:00.000" : "2024-02-01 00:00:00.000"
}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
df["DtCriacao"]

# %% Primeira forma de lidar:
"""
Podemos simplesmente remover toda e qualquer linha que possua
pelo menos um valor como 'Na' com o método '.dropna',
ou podemos remover as linhas que possuam TODAS as células
com valores nulos (Na).
"""

df = df.dropna()
df = df.dropna(how="any") #Igual ao de cima, desconsidera linhas que possuam pelo menos uma célular Na
df = df.dropna(how="all") #Desconsidera somente as linhas que possuem todos os valores como Na.

# %% Exemplo com outro DataFrame

brinquedo = pd.DataFrame(
    {
        "nome" : ["Miguel" , "Ana" , "José", None],
        "idade" : [24 , None , 22, 29],
        "salario" : [1200 , 2400 , None, 2400]
    }
)
brinquedo

# %% Testando diferentes formas de '.dropna()'
"""
Dropa as linhas com os nulos do dataframe baseando-se
apenas na coluna 'nome'.
"""

brinquedo.dropna(how="all", subset="nome")

# %%
"""
Dropa as linhas com os nulos do dataframe baseando-se
nas colunas 'nome' e 'idade', tendo um valor nulo em algumas
das colunas a linha já é dropada.
"""

brinquedo.dropna(how="any", subset=["nome", "idade"])

# %% FillNa:
"""
Método usado para preencher as células que estão com valor nulo (Na)
"""

brinquedo["idade"] = brinquedo["idade"].fillna(0)
#Substitui os valores nulos por 0

brinquedo["idade"] = brinquedo["idade"].fillna(brinquedo["idade"].mean())
#Substitui os valores nulos pela média

brinquedo

# %% Preenchendo diferentes colunas com diferentes valores

brinquedo = brinquedo.fillna({
    "nome" : "alguém",
    "idade" : 0,
    "salario" : 0
    }
)

brinquedo

# %% Preenchendo pela média da coluna
"""
Nesse caso, preenchendo pela média nós não estamos alterando a
média dos dados preenchendo os nulos pela média.
Estamos alterando o desvio padrão, do qual será reduzido.

Ou seja, utilizando esse método em nossos dados estariamos
subestimando nosso desvio padrão (bem como a variância e coeficiente
de variação).+

Há outras estratégias que podem ser mais interessantes, porém
a depender do caso pode servir para nossa análise, em última
instância.
"""

media = brinquedo[["idade", "salario"]].mean()
brinquedo = brinquedo.fillna(media)
brinquedo