"""Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""

numeros_impares = [2 * i + 1 for i in range(15)]

numeros_impares.extend([float(numeros_impares[-2])] * 3)

numeros_impares.insert(3, "Cadena")

print("Mi lista antes de eliminar la cadena:", numeros_impares)

del numeros_impares[3]
print("Mi lista después de eliminar la cadena:", numeros_impares)
