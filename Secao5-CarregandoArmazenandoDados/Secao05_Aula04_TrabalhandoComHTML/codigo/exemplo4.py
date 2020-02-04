import pandas as pd

cidade = 'Viana'
lista = pd.read_html('exemplo2.html', match=cidade)
print(lista)