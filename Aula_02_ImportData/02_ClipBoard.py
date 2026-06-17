"""
ClipBoard irá ler o que está salvo no 'ctrl + c' do
computador, gerando um dataframe do texto salvo.

É utilizado como algo mais experimental/investigativo.
Não é algo utilizado de forma produtiva (gerando valor).
"""
# %%

import pandas as pd

df = pd.read_clipboard(sep=";")
df