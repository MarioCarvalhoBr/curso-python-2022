x = "Maravilhoso"

def imprimir():
  print("Python  é " + x)

def imprimir2():
  global x
  x = "Lindo"
  print("Python  é " + x)

imprimir2()
imprimir()
