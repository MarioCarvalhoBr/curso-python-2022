import os

# os.mkdir("arquivos/pasta")

if os.path.exists("arquivos/pasta/alunos.txt"):
    f = open("arquivos/pasta/alunos.txt", "r",  encoding="utf-8")
    for i in f:
        print(i)
    f.close

    f = open("arquivos/pasta/alunos.txt", "a",  encoding="utf-8")
    nome = input("Digite seu nome: ")
    f.write("\n"+nome)
    f.close
else:
  f = open("arquivos/pasta/alunos.txt", "a",  encoding="utf-8")
  nome = input("Digite seu nome: ")
  f.write("\n"+nome)
  f.close