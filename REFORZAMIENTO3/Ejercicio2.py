"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""


def mostrarcuadrados(num1, num2):
    num_inicio = min(num1, num2)
    num_fin = max(num1, num2)

    print(f"Cuadrados entre {num_inicio} y {num_fin}:")
    for i in range(num_inicio + 1, num_fin):
        print(i ** 2)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mostrarcuadrados(num1, num2)
