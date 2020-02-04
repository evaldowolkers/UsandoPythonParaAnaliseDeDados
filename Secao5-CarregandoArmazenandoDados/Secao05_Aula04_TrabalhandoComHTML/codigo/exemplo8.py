import pandas as pd

cidade = 'Viana'
lista1 = pd.read_html('exemplo3.html', match='Viana')
lista2 = pd.read_html('exemplo3.html', match='Viana', keep_default_na=False)
print(lista1)
print(lista2)