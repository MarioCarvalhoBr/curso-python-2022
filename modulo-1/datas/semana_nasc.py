import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_br")

dia = int(input("Dia: \n"))
mes = int(input("Mês: \n"))
ano = int(input("Ano: \n"))

data = datetime.datetime(ano, mes, dia)
print(data.strftime("Você nas numa %A"))