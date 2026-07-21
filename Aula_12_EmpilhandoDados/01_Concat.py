"""
Entendendo como funciona o 'pd.concat()':

Quando chamamos esse comando, ele espera que passemos uma
LISTA de DataFrames.

Com o 'axis=0' (ou não especificado) ele irá simplesmente
empilhar os dados um em cima do outro.

Com o 'axis=1' ele irá concatenar os dados de forma horizontal
(semelhante a um merge/join), associando os valores através
dos ÍNDICES!! Só será pela ordem do df se resetarmos os índices
através do '.reset_index()' diretamente no df.
"""
# %%

import pandas as pd

# %% df's

df1 = pd.DataFrame({
    "Nome" : ["Miguel", "Ronaldo", "Eduarda", "Jeferson"],
    "Idade" : [24 , 15, 27, 16],
    "UF" : ["SC" , "RJ", "SP", "SP"]
})

df2 = pd.DataFrame({
    "Nome" : ["Francisco", "Augusto", "Lô"],
    "Idade" : [32, 47, 51]
})

# %%
# SELECT * FROM df1
# UNION ALL
# SELECT * FROM df2

pd.concat([df1, df2]) #Retorna um DataFrame com os dados empilhados, e com os índices mantidos.

pd.concat([df1, df2], ignore_index=True) #Ignora os índices originais do segundo df passado na lista.

# %% df com nova coluna

df3 = pd.DataFrame({
    "Salário": [2550, 5300, 1100]
})

# %%

pd.concat([df2, df3]) #Retorna somente os dados empilhados

pd.concat([df2, df3], axis=1) #Retorna um df com os valores combinados (como se fosse um join/merge)

# %% O concat com axis=1 segue o índice e não a ordem do df

df3 = df3.sort_values(by='Salário')

pd.concat([df2, df3], axis=1) #Fica igual ao concat anterior, pois segue os índices e não a ordenação do df.

# %% Para seguir a ordem do df precisamos reatribuir os índices

df3 = df3.sort_values(by='Salário').reset_index(drop=True) #O 'drop=True' faz com que não crie uma coluna nova com os índices antigos

pd.concat([df2, df3], axis=1)