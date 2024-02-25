def cargar():
    try:
        numero = int(input("Por favor, ingresa un número entero: "))
        return numero
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

def sumar(num1, num2):
    return num1 + num2