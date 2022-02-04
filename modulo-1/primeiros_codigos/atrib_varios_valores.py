# Entrada
peso, altura, imc = 0, 0, 0
peso = altura = imc = 0

print(f"{peso}, {altura}, {imc}")
peso = float(input("Peso: "))
altura = float(input("Altura: "))

# Processamento
imc = peso / (altura * altura)

# Saída
print(f"Seu IMC é: {imc}")
print(f"{peso}, {altura}, {imc}")
