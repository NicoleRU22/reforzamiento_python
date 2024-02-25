
def acceder_lista():
    lista = [2, 6, 10, 4, 5, 23, 1]
    try:
        elemento = lista[10]
        print("El elemento es:", elemento)
    except IndexError as e:
        print("Se produjo un error de índice:", e)
        print("Asegúrate de acceder a un índice dentro del rango de la lista.")


print(acceder_lista())