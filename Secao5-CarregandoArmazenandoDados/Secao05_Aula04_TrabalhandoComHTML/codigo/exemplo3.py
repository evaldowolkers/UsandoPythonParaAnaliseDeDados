import pandas as pd

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)
print(dfs)