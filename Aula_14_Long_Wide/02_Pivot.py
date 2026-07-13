"""
Conseguimos imaginar o '.pivot_table()' como se fosse uma tabela dinâmica
do excel. Conseguimos fazer agregações dos dados e escolher quais variáveis
queremos manter na tabela para analisarmos.
"""
# %%

import pandas as pd

df = pd.read_csv("../Aula_12_EmpilhandoDados/homicidios-consolidado.csv", sep=";")
df.head()

# %%

df_stack = (df.set_index(["nome", "período"])
              .stack()
              .reset_index())

df_stack.columns = ["nome", "período", "métrica", "total"]

# %% exemplo 1 pivot

df_stack.pivot_table(values="total",
                     index=["nome", "período"],
                     columns="métrica")

# %% exemplo 2 pivot

df_stack.pivot_table(values="total",
                     index="nome",
                     columns="métrica",
                     aggfunc='mean')

"""
Para analisarmos dessa forma, precisa haver alguma agregação dos nomes
em repetição. Isso acontece pois os nomes se repetem, visto que há uma
dimensão a mais de dados, que é a coluna 'período', que justifica essa
repetição. Então o que fazemos é representar todos os períodos num só
valor. Para isso, utilizamos formas de agregação de dados (soma, média, etc.).
 
No caso de '.pivot_table()', ele possui a agregação
padrão que é a média, mas podemos especificar através do parâmetro 'aggfunc='.
"""

# %% exemplo 3 pivot

df_stack.pivot_table(values="total",
                     index="nome",
                     columns="métrica",
                     aggfunc='sum')

# %%

(df_stack.pivot_table(values="total",
                     index=["nome", "período"],
                     columns="métrica")
        .stack()
        .reset_index())
# %%
