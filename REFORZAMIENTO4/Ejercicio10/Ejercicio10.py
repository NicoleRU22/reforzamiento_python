
def guardar_usuario(nombre, apellido, edad):
    try:
        with open("agenda.txt", "a") as file:
            file.write(f"{nombre},{apellido},{edad}\n")
        print("Usuario guardado en agenda.txt correctamente.")
    except Exception as e:
        print(f"Error al guardar usuario en agenda.txt: {e}")

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
edad = input("Ingrese edad: ")

guardar_usuario(nombre, apellido, edad)
