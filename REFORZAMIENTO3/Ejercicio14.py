"""
Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)
"""
def nombre_apellido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido

def ingresar_tipo_seguro():
    tipo_seguro = input("Ingrese el tipo de seguro que tiene: ")
    return tipo_seguro

def mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        return True
    else:
        return False
