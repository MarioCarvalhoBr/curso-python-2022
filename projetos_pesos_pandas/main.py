import pandas as pd
import numpy as np

df_projetos = pd.read_excel('projetos_pesos_pandas/banco.xlsx', sheet_name="Planilha1")

# Usar a função loc pra pegar uma linha
pesos = df_projetos.loc[0][1:].to_numpy()

tam = len(df_projetos)

print("Linhas: ", tam)
valores = []
for index in range(1, tam):
    projeto = df_projetos.loc[index][1:].to_numpy()
    valores.append(projeto)

matriz = np.array(valores)

# Multiplicou o vetor pela matriz
resultado = matriz @ pesos

# Concatenando o zero a lista
escalar = np.array([0])
coluna = np.concatenate((escalar, resultado), axis=None)

# Criando uma coluna
df_projetos['resultados'] = coluna

df_projetos.to_excel('projetos_pesos_pandas/novo_banco.xlsx', sheet_name="Planilha1", index=False)
df_projetos.to_csv('projetos_pesos_pandas/novo_banco.csv', sep=";", index=False)
