# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual número ele
# deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input("Digite o número para gerar a tabuada: "))
if numero >= 1 and numero <= 10:
    # Processamento
    print("Tabuada de ", numero)
    for indece in range(1, 11):
        print(f"{numero} X {indece} == {numero * indece}")
else:
    print("Número inválido. Digite entre 1 e 10! ")