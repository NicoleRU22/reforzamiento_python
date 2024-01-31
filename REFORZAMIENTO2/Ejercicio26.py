

departamentos = {
    "depa1": "Pisco",
    "depa2": "Ica",
    "depa3": "Arequipa",
    "depa4": "Chincha",
    "depa5": "Lima",
    "depa6": "Piura"
}

print("Diccionario antes de borrar:", departamentos)

del departamentos["depa3"]

print("Diccionario después de borrar:", departamentos)

borrar = "depa3"
if borrar in departamentos:
    print(f"El departamento {borrar} todavía existe en el diccionario.")
else:
    print(f"El departamento {borrar} ya no existe en el diccionario.")
