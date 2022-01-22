import pandas as pd

df = pd.reat_txt('pandas/novo_dados1.csv', sep=";")
print(df.info()) 

# df.to_csv('pandas/planilha_novo_novo_banco.csv', sep=";", index=False)
#print(df) 
#print(df.describe())