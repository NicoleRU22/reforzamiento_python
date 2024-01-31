
"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""
empleado = {
    "nombre": "Nicole Ramirez",
    "edad": 18,
    "salario": 5600
}

lista_empleado = list(empleado.items())

print(lista_empleado)
print(type(lista_empleado))