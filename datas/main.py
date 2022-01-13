import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_br")


data_atual = datetime.datetime.now()

data_setada = datetime.datetime(2002, 10, 11)

print("data_setada: ", data_setada)
print("Dia da semana: ", data_setada.strftime("%A"))
print("Nome do mês: ", data_setada.strftime("%B"))

print("data_atual: ", data_atual)
ano_atual = data_atual.year

ano_nasc = int(input("Digite seu ano de nascimento: "))

idade = ano_atual - ano_nasc

print("Idade: ", idade)

print(data_atual.strftime("Data atual %A -  %d - %B - %Y"))