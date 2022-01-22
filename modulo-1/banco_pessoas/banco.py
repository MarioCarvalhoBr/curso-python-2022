global banco_contatos
banco_contatos = []

# Cria o arquivo se não existir
arquivo = open("./agenda.csv", "a+")
arquivo.close()

# Abre pra leitura
arquivo = open("./agenda.csv", "r+")
aux_banco = arquivo.readlines()
arquivo.close()

# Fazendo uma limpeza no banco pra poder pegar somente os dados que são 
# contatos
for i in aux_banco:
    if (i != '\n'):
        # Limpeza da string
        i = i.replace("\n","")
        banco_contatos.append(i)
    
def inserir():
    print("\nInsira os dados do contato:\n")
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    curso = input("Digite o curso: ")
    data_nasc = input("Digite o data_nasc: ")

    pessoa = cpf + ";" + nome + ";" + sobrenome  + ";" +  email + ";" +  telefone + ";" +  curso + ";" + data_nasc
    banco_contatos.append(pessoa)
    # Salvo apos inserir
    salvar()
    return None

def listar_agenda():
    print("Lista de contatos: ")
    for pessoa in banco_contatos:
        pessoa_limpa = pessoa.replace("\n", "")
        lista = pessoa_limpa.split(";")
        print(f"CPF: {lista[0]}, nome: {lista[1]}, sobrenome: {lista[2]}")
    return None

def remover_contato_cpf(cpf):
    for pessoa in banco_contatos:
        # Limpa o \n no final da string
        pessoa_limpa = pessoa.replace("\n", "")
        # Transforma a string em uma lista, divindo no símbolo ;
        lista = pessoa_limpa.split(";")
        if str(cpf) == lista[0]:
            print("Pessoa removida: ")
            print(f"CPF: {lista[0]}, nome: {lista[1]}, sobrenome: {lista[2]}")
            banco_contatos.remove(pessoa)
            break
    # Salvo apos remover
    salvar()
    return None

def buscar_contato_cpf(cpf):
    for pessoa in banco_contatos:
        pessoa_limpa = pessoa.replace("\n", "")
        lista = pessoa_limpa.split(";")
        print("Resultado da busca: ")
        if str(cpf) == lista[0]:
            print("Pessoa encontrada: ")
            print(f"CPF: {lista[0]}, nome: {lista[1]}, sobrenome: {lista[2]}")
            break
    return None

def salvar():
    print("Salvando os contatos em um arquivo .csv")
    # Salvar em arquivo a lista de contatos
    arq = open("./agenda.csv", "w")
    tam = len(banco_contatos) 
    for i in range(tam):
        # limpa a string
        if str(banco_contatos[i]) != "\n":
            arq.write(str(banco_contatos[i]) + "\n")

    arq.close()
    return None