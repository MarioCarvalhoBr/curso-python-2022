# Problema incial: Arrumar a casa - Problema grande 
# Quebra o problema maior em problemas pequenos: 
# 1 - Lavar a louça
# 1.1 - Separa a louça entre vidro, pastico, alumino...
# 2 - Fazer a comida
# 3 - Varrer a casa
# 4 - Encher as garrafas

while True:
    # Entrada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Processamento
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print(f"{num1} + {num2} == {soma}")
    print(f"{num1} - {num2} == {sub}")
    print(f"{num1} * {num2} == {mult}")
    print(f"{num1} / {num2} == {div}")