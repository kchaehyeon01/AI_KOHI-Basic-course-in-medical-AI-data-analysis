import pandas as pd

unarr = pd.read_csv('./data_tree_data.csv')
print(unarr)

arr = unarr.sort_values('height', ascending=False)
print(arr[:5])
print(arr.head(5))