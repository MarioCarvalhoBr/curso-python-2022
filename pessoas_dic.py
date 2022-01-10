pessoas = {
  "nome": "Mário",
  "sobrenome": "Carvalho",
  "endereco": "Campo Grande",
  "ano_nasc": 1997,
  "cores": ["red", "white", "blue"]
}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.get("cores"))
pessoas["nome"] = "Janaina"

print(pessoas)