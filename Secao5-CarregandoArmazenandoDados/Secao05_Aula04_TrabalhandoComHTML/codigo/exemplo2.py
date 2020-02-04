import pandas as pd


tabela = pd.read_html('exemplo2.html')
print("============================")
print(tabela[0])
print("============================")
print(tabela[1])
print("============================")