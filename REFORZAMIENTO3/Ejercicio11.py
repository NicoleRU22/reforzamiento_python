"""11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrardatos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo: {self.sueldo}")

    def mayoredad(self):
        if self.edad >=18:
            return f"{self.nombre} es mayor de edad"
        else:
            return f"{self.nombre} no es mayor de edad"

    def bonificacion(self):
        return self.sueldo*0.20

per1=Persona("Nicole",15,2600)
per2=Persona("Alexandra",20,3000)

print("Datos de la persona 1: ")
per1.mostrardatos()
print(per1.mayoredad())
print(f"La Bonificaciòn de {per1.nombre} es: {per1.bonificacion()}")
print("****************************************************************")
print("Datos de la persona 2: ")
per2.mostrardatos()
print(per2.mayoredad())
print(f"La Bonificaciòn de {per2.nombre} es: {per2.bonificacion()}")

