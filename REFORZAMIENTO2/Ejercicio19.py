"""Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista."""

lista = [0] * 10

for i in range(10):
    lista[i] = float(input("Ingrese el valor para la posición {}:".format(i+1)))

suma = sum(lista)
media = suma / 10

print(f"La suma de los números ingresados: {suma}")
print(f"La media de los números ingresados: {media}")
