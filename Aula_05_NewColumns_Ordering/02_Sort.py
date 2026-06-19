# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

# %% Ordenando valores

df["qtdePontos"].sort_values() #Ordena a serie de 'qtdePontos'

# %% Selecionando os 5 clientes (idCliente) com mais pontos
"""
Aqui o '.sort_values()' está ordenando o dataframe todo a
partir da coluna que passamos como argumento no 'by='.
Logo, retorna o df todo, e não apenas a serie da variável
ordenada.

O 'by=' coloca pelo que deve ser ordenado nosso dataframe,
pois diferente da célula acima, o retorno é o dataframe ordenado,
e não apenas a serie da variável.

'ascending=False' faz com que a ordem seja decrescente e não
crescente.

O '.sort_values()' gera um NOVO dataframe!!
"""

df.sort_values(by='qtdePontos', ascending=False).head(n=5)

# %% Selecionando apenas os id's

top_5 = ( df.sort_values(by='qtdePontos', ascending=False)
            .head(n=5)['idCliente'] )

top_5
# %% Ordenando por uma variável e tornando outra como critério de desempate

brinquedo = pd.DataFrame(
    {
        "nome" : ["Miguel" , "Ana" , "José", "Renato"],
        "idade" : [24 , 26 , 22, 29],
        "salario" : [1200 , 2400 , 7000, 2400]
    }

)

brinquedo
# %%Ordenando por uma variável e tornando outra como critério de desempate
"""
Aqui, ordenamos primeiramente pelo salário. Caso hajam salários
iguais, o critério de desempate será a idade, pois segue a ordem
de prioridade colocada no 'by=[]'.
"""

brinquedo.sort_values(by=["salario" , "idade"],
                      ascending=False)

# %%
"""
E se quiséssemos que o salário fosse considerado do maior
para o menor e a idade do menor para o maior?
"""

brinquedo.sort_values(by=["salario" , "idade"],
                        ascending=[False , True])