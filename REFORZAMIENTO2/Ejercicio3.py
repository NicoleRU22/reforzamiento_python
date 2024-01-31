
"Quita 2 elementos de tu nueva lista ítems por valor, no por índice."
cursos_universitarios = []

cursos_universitarios.append("Física 2")
cursos_universitarios.append("Poo")
cursos_universitarios.append("Investigaciòn operativa")
cursos_universitarios.append("Base de datos")

print("La lista de cursos universitarios actualizada es la siguiente: {}".format(cursos_universitarios))

cursos_universitarios.remove("Física 2")
cursos_universitarios.remove("Poo")

print("Lista de cursos universitarios actualizada después de quitar elementos por valor: {}".format(cursos_universitarios))
