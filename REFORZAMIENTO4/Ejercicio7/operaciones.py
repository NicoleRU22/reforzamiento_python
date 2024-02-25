

import random

def aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(30)]
    print("La lista de 30 números enteros aleatorios entre 0 y 100 es:")
    print(numeros_aleatorios)
    return numeros_aleatorios

def ordenarlista(lista):
    lista_ordenada = sorted(lista)
    print("La lista ordenada:")
    print(lista_ordenada)
    return lista_ordenada