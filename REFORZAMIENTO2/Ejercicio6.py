"""Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista."""

cursos = ["Matemáticas 2", "Física", "Poo", "Matemáticas","Poo"]

curso_contar = "Poo"

repeticiones = cursos.count(curso_contar)

print("El curso {} se repite {} veces en la lista.".format(curso_contar,repeticiones))

