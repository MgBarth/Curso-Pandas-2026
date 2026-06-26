# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome" : ["Miguel", "Maria", "Eduardo", "Renato", "Maria", "Manoela", "Miguel"],
    "sobrenome" : ["Augusto", "Antonia", "Silva", "Silva", "Antonia", "Eduarda", "Augusto"],
    "salario" : [2132, 1423, 2132, 6523, 5341, 2134, 7540] 
})

df

# %% Ordenando dataset pelo salário de forma decrescente

df = df.sort_values("salario", ascending=False)
df

# %% Dropando duplicatas para determinadas colunas passadas como critério
"""
Aqui dropamos a duplicata de nomes com o maior salário, pois
nossos dados estão ordenados do maior para o menor salário.
"""

df.drop_duplicates(keep='last', subset=["nome", "sobrenome"])

# %% Muito comum ver escrito dessa forma no mercado
"""
Aqui passamos os métodos um atrás do outro em nosso df.
Sim, podemos passar dois métodos ao mesmo tempo em nossa
variável.
"""

df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep='last', subset=["nome", "sobrenome"]))

df

# %%

