try:
    print(x)
    y = x / 0
    lista = []
    lista[9] = 7
except NameError:
  print("Variavel não está definida")
except ZeroDivisionError:
  print("Não é possível dividir por zero!")
except IndexError:
  print("Você tentou acessar uma posição da lista que não existe!")
except IndentationError:
  print("Seu código está mal identado!")
except:
  print("Qualquer outro problema!")
