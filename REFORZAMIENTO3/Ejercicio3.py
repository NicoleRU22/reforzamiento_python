"""
Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos.
"""

numero = int(input("Ingrese un número: "))
def sumardigitos(numero):
    suma = 0
    numero_str = str(numero)
    for digito in numero_str:
        suma += int(digito)
    return suma

result = sumardigitos(numero)
print("La suma de los dígitos del número {} es: {}".format(numero,result))
