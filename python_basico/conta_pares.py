conta_pares = 0
conta_impares = 0
for x in range(1, 11):
    if (x % 2) == 0:
        print("Encontrou um número par: ", x)
        conta_pares += 1  # conta_pares = conta_pares + 1
    else: 
       conta_impares += 1 
print("conta_pares: ", conta_pares)
print("conta_impares: ", conta_impares)
print("Soma: ", conta_pares + conta_impares)
