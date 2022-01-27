class Circulo():
    def __init__(self, raio):
        self.pi = 3.14
        self.raio = raio

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def valida(self):
        if self.base <= 0 or self.altura <=0:
            return False
        else: 
            return True

    def area(self):
        area_rec = self.base  *  self.altura
        return area_rec
        
    def perimetro(self):
        perimetro_rec = (2*self.base)  +  (2*self.altura)
        return perimetro_rec
    
    def __str__(self) -> str:
        texto = f"-----------\nBase: {self.base}\nAltura: {self.altura}\nArea: {self.area()}\nPerimetro: {self.perimetro()}\nValido: {self.valida()}\n-----------"
        return texto

ret1 = Retangulo(10,5)
area = ret1.area()
print(f"VALOR ESPERADO:{str(50)}")
print(f"VALOR RETORNADO:{str(area)}")

