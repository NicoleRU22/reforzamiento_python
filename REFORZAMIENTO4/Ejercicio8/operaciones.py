

import math

def cargarvalor():
    try:
        valor = int(input("Por favor, ingresa un valor entero: "))
        return valor
    except ValueError:
        print("Error: Debes ingresar un valor entero válido.")

def raiz_cuadrada(valor):
    raiz_cuadrada = math.sqrt(valor)
    print(f"La raíz cuadrada de {valor} es: {raiz_cuadrada}")

def cuadrado_y_cubo(valor):
    cuadrado = valor ** 2
    cubo = valor ** 3
    print(f"{valor} elevado al cuadrado es: {cuadrado}")
    print(f"{valor} elevado al cubo es: {cubo}")