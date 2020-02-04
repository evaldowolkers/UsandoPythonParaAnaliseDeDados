import pandas as pd

cidade = 'Viana'
lista = pd.read_html('exemplo2.html', match=cidade, index_col=0)
print(lista)