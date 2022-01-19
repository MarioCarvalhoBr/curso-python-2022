import pandas as pd
import numpy as np
dados = {
  "nome": ["Maça", "Maça", "Banana", "Uva"],
  "calorias": [420,50,  50, 390],
  "duracao": [50, 50, 40, 45]
}

df_frutas = pd.DataFrame(dados)
#print(df_frutas.loc[0])
#print(df_frutas.loc[[0, 1]])
print(df_frutas["nome"].get("Banana"))


array_calorias = df_frutas["calorias"].to_numpy()
array_calorias = df_frutas["calorias"].values
##print(df_frutas) 