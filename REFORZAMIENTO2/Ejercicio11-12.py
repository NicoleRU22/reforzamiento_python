"""Crear una lista (entre floats y booleanos, 6 elementos mínimo) donde imprimas el
penúltimo yúltimo valor (por índice)."""

lista = [12.14, True, 4.22, False, 1.5, True]

penultimo= lista[-2]
print("El penúltimo valor es:", penultimo)

ultimo = lista[-1]
print("El último valor es:", ultimo)

"""Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())"""

print("Tipo de elemento de {} es: {}".format(lista[1],type(lista[1])))
print("Tipo de elemento de {} es: {}".format(lista[4],type(lista[4])))