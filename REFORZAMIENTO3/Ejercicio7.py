"""7. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""


class ReviertaCadena:
    def revertir_cadena(self, cadena):
        palabras = cadena.split()
        palabrasrevertidas = palabras[::-1]
        return ' '.join(palabrasrevertidas)

revertidor = ReviertaCadena()

cadena= "Hola Pythonista, seguimos adelante"

result = revertidor.revertir_cadena(cadena)
print("Resultado 1:", result)

result2 = revertidor.revertir_cadena(cadena)
print("Resultado 2:", result2)
