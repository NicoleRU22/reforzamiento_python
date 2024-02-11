"""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

def sumatoria_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

numero1 = int(input("Ingrese el primer número positivo: "))
numero2 = int(input("Ingrese el segundo número positivo: "))

sumadigitos1 = sumatoria_digitos(numero1)
sumadigitos2 = sumatoria_digitos(numero2)

print("Sumatoria de dígitos del primer número:", sumadigitos1)
print("Sumatoria de dígitos del segundo número:", sumadigitos2)

mayorsumatoria = max(sumadigitos1, sumadigitos2)
if mayorsumatoria == sumadigitos1:
    print("El número con la mayor sumatoria de dígitos es:", numero1)
elif mayorsumatoria == sumadigitos2:
    print("El número con la mayor sumatoria de dígitos es:", numero2)

if sumadigitos1 < 10:
    print("El primer número cumple con la condición.")
if sumadigitos2 < 10:
    print("El segundo número cumple con la condición.")
