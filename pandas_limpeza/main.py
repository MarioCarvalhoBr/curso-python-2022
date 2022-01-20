import pandas as pd
import matplotlib.pyplot as plt

df_sujo = pd.read_csv("pandas_limpeza/dirtydata.csv", sep=",")
# print("Informações: ", df_sujo.info())

df_limpo = df_sujo.dropna()

df_sujo['Calories'].fillna(0 ,  inplace = True)
df_sujo['Date'].fillna("2020/01/01" ,  inplace = True)
df_sujo['Date'] = pd.to_datetime(df_sujo['Date'])
df_sujo['Calories'] = pd.to_numeric(df_sujo['Calories'])

# df_sujo.loc[7, 'Duration'] = 45
"""
for x in df_sujo.index:
  if df_sujo.loc[x, "Duration"] > 61:
    df_sujo.loc[x, "Duration"] = 45
"""
for x in df_sujo.index:
  if df_sujo.loc[x, "Duration"] > 120:
    df_sujo.drop(x, inplace = True)

df_sujo.drop_duplicates(inplace = True)

#print(df_sujo.head(50))

##print(df_sujo.duplicated())

#print(df_sujo.corr())
##print(df_sujo.to_string())

# prepara pra plotar 
df_sujo.plot(kind = 'bar', x = 'Calories', y = 'Pulse')

# Plota e mostra
plt.show()