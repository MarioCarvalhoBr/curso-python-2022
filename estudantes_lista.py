# Criação da lista vazia
estudates = []

# Inserindo novos elementos no final da lista
estudates.append("Mario")
estudates.append("Karol")
estudates.append("Hévilla")
estudates.append("Lucas")
estudates.append("Elisa")

#Inserir no posição especificada
estudates.insert(2, "Manu")
print("Lista antes da alteração: ", estudates)
# Alterando elementos
estudates[2] = "Janaina"

#imprimindo
print("Lista final: ", estudates)

estudates.remove("Mario")
estudates.pop(1)

print("Lista após a remoção: ", estudates)
