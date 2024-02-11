"""Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""


class CalculadoraCuboCuadrado:
    def __init__(self):
        self.resultado = 0

    def ingresarnumero(self):
        numero = input("Ingrese un número entero: ")
        if numero.isdigit():
            self.resultado = int(numero)
        else:
            print("Ingrese un numero entero")

    def cubo(self):
        return self.resultado ** 3

    def cuadradodecubo(self):
        return self.cubo() ** 2


calculadora = CalculadoraCuboCuadrado()
calculadora.ingresarnumero()

cubo_resultado = calculadora.cubo()
print("El cubo del número ingresado es:", cubo_resultado)

cuadradocuboresultado = calculadora.cuadradodecubo()
print("El cuadrado del cubo del número ingresado es:", cuadradocuboresultado)
