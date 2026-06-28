"""
Nesse caso, imagine que precisamos pegar apenas uma parte
do IdCliente, sendo ela a última parte (dividida pelo hífen).

Id_Exemplo = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"
Parte_de_Interesse = "b586ed1c709a"

O método '.apply(function)' serve para realizarmos operações
linha a linha de uma determinada coluna.
"""

# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%

Id_Exemplo = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

Id_Exemplo.split("-") #É uma lista com os itens separados pelo hífen.
Id_Exemplo.split("-")[-1] #Acessa o último item da lista.

# %% Função para aplicar nos itens

def last_CodId(x):
    return(x.split("-")[-1])

# %% Laço de repetição para aplicar em toda coluna

novo_Id = []

for i in df["idCliente"]:
    novo_Id.append( last_CodId(i) )

novo_Id

"""
Criamos uma nova coluna (ou seja, é uma serie) e adicionamos
a chave, os valores da variável 'novo_Id', que é uma lista de int's.
"""

df["NovoId"] = novo_Id
df

# %%Fazendo com .apply, simplificando todo o processo

df["NovoId"] = df["idCliente"].apply(last_CodId)
df.head()
