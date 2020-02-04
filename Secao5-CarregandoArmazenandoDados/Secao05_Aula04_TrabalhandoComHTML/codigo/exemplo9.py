import pandas as pd

lista1 = pd.read_html('exemplo3.html', attrs={'id': 'tabela1'})
lista2 = pd.read_html('exemplo3.html', attrs={'style': 'width:100%'})
print(lista1)
print("=================================")
print(lista2)