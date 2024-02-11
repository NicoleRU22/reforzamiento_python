

import math

class Circulo:
    def __init__(self, radio):
        if isinstance(radio, (int, float)):
            if radio > 0:
                self.radio = radio
            else:
                raise ValueError("El radio del círculo debe ser mayor que cero.")

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    @classmethod
    def crear_circulo(cls):
        while True:
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                return cls(radio)
            except ValueError:
                print("Error")

circulo1 = Circulo.crear_circulo()
circulo2 = Circulo.crear_circulo()

print("El àrea del círculo 1:", circulo1.area())
print("El perímetro del círculo 1:", circulo1.perimetro())
print("El àrea del círculo 2:", circulo2.area())
print("El perímetro del círculo 2:", circulo2.perimetro())

