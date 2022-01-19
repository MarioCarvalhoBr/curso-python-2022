import pandas

dados = {
  'carros': ["BMW", "Volvo", "Ford", "Ferrari", "Teste"],
  'preco': [300000, 500000, 400000, 1000000, 900000],
  'ano': [2019, 2014, 2020, 2022, 2028],
  'palca': ["Tat-224","asft-967","asf-235","asf-347", 'testet']
}
df_carros = pandas.DataFrame(dados)
descricao = df_carros['preco'][2]
print(type(df_carros['preco']))
for preco, carro in zip(df_carros['preco'], df_carros['carros'],):
    print(f"O valor do {carro} é  {preco}")

print("valor: ", df_carros.describe())
print(df_carros)