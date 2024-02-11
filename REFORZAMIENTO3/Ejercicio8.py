"""
8. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""

class Datos:
    def __init__(self):
        self.datos = {}

    def nombreapellido(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        self.datos['nombre'] = nombre
        self.datos['apellido'] = apellido

    def ingresaredad(self):
        edad = input("Ingrese su edad: ")
        self.datos['edad'] = edad

    def imprimir(self):
        print("Datos de la persona:")
        for key, value in self.datos.items():
            print(f"{key.capitalize()}: {value}")

persona = Datos()

persona.nombreapellido()

persona.ingresaredad()

persona.imprimir()
