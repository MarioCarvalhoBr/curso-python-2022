# Entrada
# Declarando as variáveis
nome = "Mário" # Tipo texto
ano_nascimento = 1997 # Tipo número inteiro (1,3,4,5,4,3 ...)
ano_atual = 2021 # Tipo número inteiro (1,3,4,5,4,3, ...)
peso = 93.53 # Tipo número decimal (1.3, 4.5, 6.6, ...)
sobrenome = "Carvalho"# Tipo texto
nome_completo = nome + sobrenome # "Somando"(Soma para tipo número se chama concatenação) de dois textos 
endereco = "Campo Grande, MS, Brasil." # Tipo texto

# Processamento
'''
Na linha de código abaixo é criada a variável idade, e ela contém o resultado
da subtracao do valor da variavel ano_atual(2021) com a varivável ano_nascimento(1997)
'''
idade = ano_atual - ano_nascimento # 2021 - 1997 

# Saída
# Imprime na tela as variáveis
print("Nome: ", nome)
print("Nome completo: ", nome_completo)
print("Peso: ", peso, "KG") # Você pode adicionar quantos valores quiser pelo print, basta usar virgula
print("Ano atual: ", ano_atual)
print("Ano nascimento: ", ano_nascimento)
print("Idade: ", idade)
print("Endereço: ", endereco)
