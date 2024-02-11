
class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota final: {self.nota_final}")

    def resultadoaprobado(self):
        if self.nota_final >= 11:
            return f"El alumno {self.nombre} ha aprobado con una nota final de {self.nota_final}."
        else:
            return f"El alumno {self.nombre} ha reprobado con una nota final de {self.nota_final}."

alumno1 = Alumno("Nicole", 18, 17)
alumno2 = Alumno("Alexandra", 22, 10)
alumno3 = Alumno("Carlos", 21, 14)

print("Información de alumno 1:")
alumno1.imprimir()
print(alumno1.resultadoaprobado())
print("********************************************************")
print("Información de alumno 2:")
alumno2.imprimir()
print(alumno2.resultadoaprobado())
print("*********************************************************")
print("Información de alumno 3:")
alumno3.imprimir()
print(alumno3.resultadoaprobado())
