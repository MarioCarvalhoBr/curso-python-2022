import math
def area_circulo(raio):
    area = round(math.pi * math.pow(raio, 2), 2)
    return area

def area_quadrado(lado):
    area = math.pow(lado, 2)
    return round(area, 2)