import pandas as pd

df = pd.read_excel('pandas/dados1.xlsx', sheet_name="JAN")
df['municipios'][0]='CARUARU'
print(df.head(5)) 
#print(df.describe()) 

df.to_excel('pandas/novo_dados1.xlsx', sheet_name="JAN-alterado", index=False)
