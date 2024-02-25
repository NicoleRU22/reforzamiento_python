

def suma_numeros_y_texto():
    try:
        suma = 80 + "Hola Pythonista"
        print("La suma es:", suma)
    except TypeError as e:
        print("Se produjo un error de tipo:", e)
        print("Asegúrate de sumar solo números.")


print(suma_numeros_y_texto())
