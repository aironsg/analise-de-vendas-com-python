
import pandas as pd
import json 


file  = open('data/vendas.json', 'r')
data  = json.load(file)

df = pd.DataFrame.from_dict(data)
df['Data da Compra']  = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')


file.close()