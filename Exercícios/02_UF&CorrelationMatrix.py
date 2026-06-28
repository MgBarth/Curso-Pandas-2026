# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {"User-Agent":"Mozilla/5.0"}

resposta = requests.get(url , headers=headers)
resposta.text

dfs = pd.read_html(resposta.text)
uf = dfs[1]
uf.head()

# %% Verificando os tipos de variável de cada coluna

uf.dtypes

# %% Alterando uf[["Área (km²)", "PIB (2015)", "PIB per capita (R$) (2015)"]] para float
"""
Montando o que precisamos usar para criar a função, para uma 'célula'

numero_exemplo = "164 122,2"
numero = float(numero_exemplo.replace(" " , "")
                             .replace("," , "."))
"""
# %% Função str_to_float
"""
Tentamos rodar a função porém retornou que não estava dando
para transformar para float por haver um caractere especial
"\xa0" que fazia o espaço entre os números. Por isso está
adicionado o último replace na função. Identificamos através
do erro que a função retornou quando rodamos ela.
"""

def str_to_float(x:str):
    
    x = float(x.replace(" " , "")
               .replace("," , ".")
               .replace("\xa0" , ""))
    
    return(x)

# %% .apply(str_to_float)

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)

uf.head()

# %% Tratando uf["Alfabetização (2016)" , "Mortalidade infantil (2016)"]

uf = uf.rename(columns={
    "Alfabetização (2016)" : "Alfabetização (2016) (%)",
    "Mortalidade infantil (2016)" : "Mortalidade infantil (2016) (‰)"
})
# Renomeamos para adicionar a 'unidade' na descrição da coluna

# %% Função str&percent|perthousand_to_float

def str_percent_to_float(x:str):

    x = float(x.replace("," , ".")
               .replace("%" , "")
               .replace("‰" , ""))
    
    return(x)

# %% .apply(str_percent_to_float)

uf["Alfabetização (2016) (%)"] = uf["Alfabetização (2016) (%)"].apply(str_percent_to_float)
uf["Mortalidade infantil (2016) (‰)"] = uf["Mortalidade infantil (2016) (‰)"].apply(str_percent_to_float)

# %% Tratando uf["Expectativa de vida (2016)"]

uf = uf.rename(columns={
    "Expectativa de vida (2016)" : "Expectativa de vida (2016) (Em anos)"
})

# %% Função str_year_to_float

def str_year_to_float(x:str):

    x = float(x.replace("," , ".")
               .replace(" anos" , ""))
    
    return(x)

# %% .apply(str_year_to_float)

uf["Expectativa de vida (2016) (Em anos)"] = uf["Expectativa de vida (2016) (Em anos)"].apply(str_year_to_float)

# %% Criando coluna com região de cada estado. A informação das regiões puxamos de fora do dataset

def uf_to_region(uf):

    if uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return("Nordeste")

    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return("Norte")
    
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return("Sudeste")
    
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return("Sul")
    
    elif uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return("Centro-Oeste")

"""
Copiamos essa lista da wikipedia:

"Nordeste" => ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]
"Norte" => ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]
"Sudeste" => ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]
"Sul" => ["Paraná", "Rio Grande do Sul", "Santa Catarina"]
"Centro-Oeste" => ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]
"""

# %% .apply(uf_to_region) criando uma nova coluna

uf["Região"] = uf["Unidade federativa"].apply(uf_to_region)
uf

# %% Acessando lista de colunas

uf.columns

# %% Reordenando colunas

uf = uf[['Bandeira', 'Unidade federativa', 'Abreviação', 'Sede de governo',
       'Região', 'Área (km²)', 'População (Censo 2022)', 'Densidade (2005)',
       'PIB (2015)', '(% total) (2015)', 'PIB per capita (R$) (2015)',
       'IDH (2010)', 'Alfabetização (2016) (%)',
       'Mortalidade infantil (2016) (‰)',
       'Expectativa de vida (2016) (Em anos)']]

uf.head()

# %% Ordenando por PIB per capita

uf_resume = uf.drop(["Bandeira", "Abreviação", "Sede de governo"], axis=1)
uf_resume.sort_values("IDH (2010)", ascending=True)

# %% Plotando matriz de correlações

import matplotlib.pyplot as plt
import seaborn as sns

uf_correlation = uf.drop(["Bandeira", "Unidade federativa",
                          "Abreviação", "Sede de governo", "Região"], axis=1)
#Removemos as colunas do tipo str

correlation_matrix = uf_correlation.corr().round(2)
#Aqui calculamos a correlação das variáveis. '.round(2)' determina duas casas decimais.

fig, ax = plt.subplots(figsize=(12,10))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax, cmap="coolwarm")