import pandas as pd

lista = [1985, 2000, 3000]

serie = pd.Series(lista)
print(serie)


for dado in serie:
    print(dado)

print(serie.describe())