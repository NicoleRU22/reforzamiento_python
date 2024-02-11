"""
Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada.
"""


def contarpalabras(oracion):
    palabras=oracion.split()
    cantpalabras=len(palabras)
    return cantpalabras


while True:
    oracion = input("Ingrese una oracion con un mìnimo de 3 palabras: ")

    if contarpalabras(oracion) >= 3:
        break
    else:
        print("La oración ingresada no tiene 3 palabras. Inngrese otra oraciòn")

resultado = contarpalabras(oracion)
print("La oración ingresada tiene {} palabras.".format(resultado))
