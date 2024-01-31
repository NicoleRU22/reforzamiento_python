"""Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola."""
empleado = {
    "nombre": "Nicole Ramirez",
    "edad": 18,
    "salario": 5600
}

lista_empleado = list(empleado.values())
print(type(lista_empleado))

