print("MENU")
print("1. Agua")
print("2. Refrigerante")
print("3. Suco")

# Entrada
opcao = int(input("Digite o numero da bebida que você quer: "))

if opcao == 1:
    print("Você escolheu Agua")
elif opcao == 2:
    print("Você escolheu Refrigerante")
elif opcao == 3:
    print("Você escolheu Suco")
else:
    print("Opção inválida. Opção disponíveis: (1, 2 ou 3)")