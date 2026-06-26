# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome" : ["Miguel", "Maria", "Eduardo", "Renato", "Maria", "Manoela", "Miguel"],
    "sobrenome" : ["Augusto", "Antonia", "Silva", "Silva", "Antonia", "Eduarda", "Augusto"]
})

df
# %% Dropando duplicatas

df.drop_duplicates() #Mantém a primeira linha das duplicatas
df.drop_duplicates(keep="last") #Mantém a última linha das duplicatas