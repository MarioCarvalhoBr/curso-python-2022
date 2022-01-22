import os

f = open("arquivos/alunos.txt", "r") # a- insere no final.  w-sobrescreve tudo
# Escrita
# f.write("\nPedro Motta")
# Somente imprime o texto do arquivo
# estudantes = f.readlines()

for x in f.readlines():
    print(x)

#print(estudantes[0])
# Fechar o arquivo
f.close()

# os.remove("arquivos/alunos.txt")

