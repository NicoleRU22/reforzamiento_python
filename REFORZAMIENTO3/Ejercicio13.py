"""
13. Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto.
"""

class Persona:
    def __init__(self):
        self.nombre = str(input("Ingrese su numbre: "))
        self.edad = int(input("Ingrese su edad: "))

class empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def impuesto(self):
        if self.sueldo >= 4000:
            return self.sueldo*0.1
        else:
            return 0

empleado = empleado()

print(f"Sueldo del empleado: {empleado.sueldo}")
impuestos = empleado.impuesto()
print(f"Impuestos a pagar: {impuestos}")