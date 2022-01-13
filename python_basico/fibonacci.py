N = int(input("Digite o número N pra gerar Fibonacci "))

# Processamento
anterior = 1
atual = 1
lista_fib = []
lista_fib.append(anterior)
lista_fib.append(atual)

antigo_atual = 0
for indece in range(N):
    antigo_atual = atual
    atual = atual + anterior
    anterior = antigo_atual

    lista_fib.append(atual)

print(lista_fib)