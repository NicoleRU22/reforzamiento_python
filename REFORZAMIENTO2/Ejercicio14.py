"""Elimina un elemento por dos índices existentes y ya no por el valor."""

lista = [12.14, True, 4.22, False, 1.5, True]

eliminar=lista.pop(2)
eliminar2=lista.pop(4)

print("Mi lista luego de eliminar un elemento: {}".format(lista))
