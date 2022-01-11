N = int(input("Digite o número N pra gerar Fibonacci "))

# Processamento
anterior = 1
atual = 1
lista_fib = []
lista_fib.append(anterior)
lista_fib.append(atual)

antigo_atual = 0
i = 1
while i <= N:
    antigo_atual = atual
    atual = atual + anterior
    anterior = antigo_atual

    lista_fib.append(atual)
    i += 1  # i = i + 1
else: 
    print("Saiu do laço")
print(lista_fib)
