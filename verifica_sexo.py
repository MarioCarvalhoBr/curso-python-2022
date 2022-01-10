# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

letra = input("Digite seu sexo (F ou M): ")
if (letra == "F" or letra == "f"):
    print("F - Feminino")
elif (letra == "M" or letra == "m"):
    print("M - Masculino")
else:
    print("Sexo Inválido")