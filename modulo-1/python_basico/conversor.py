from brcurrency.dolar import Dolar

dolar =  Dolar() # Cria o objeto conversor
cotacao = dolar.get_cotacao() # Pega a cotação atual do Dólar
print("Cotação do dolar:  ", cotacao)

# Conversão de dólares para reais
valor = float(input("Digite o valor em dólares: "))

reais = valor*cotacao

print("O valor convertido para reais é ",reais)
