PI = 3.14
# Definindo as funções de cada operação
def soma (n1, n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mult (n1,n2):
    return n1 * n2

def div (n1, n2):
    if n2 != 0:
        resultado = n1 / n2
        return round(resultado, 2)
    else:
        print("Não é possível dividir por zero")
        return None

def div2 (n1, n2):
    try:
        resultado = n1 / n2
        return round(resultado, 2)
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
        return None
    except:
        print("Deu erro na operação de divisão!")
        return None