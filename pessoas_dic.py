pessoas = {
  "nome": "Mário",
  "sobrenome": "Carvalho",
  "endereco": "Campo Grande",
  "ano_nasc": 1997,
  "cores": ["red", "white", "blue"]
}

pessoa2 = {
  "nome": "Pedro",
  "sobrenome": "Campos",
  "endereco": "Buriticupu-MA",
  "ano_nasc": 1994,
  "cores": ["red", "white", "blue"]
}
print(pessoa2.keys())
print(pessoa2.values())


print(pessoas.get("cores"))
pessoas["nome"] = "Janaina"

print(pessoas)