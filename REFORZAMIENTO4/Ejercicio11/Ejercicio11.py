def guardar_calificacion(nombre, nota1, nota2):
    promedio = (nota1 + nota2) / 2

    with open("calificaciones.txt", "a") as file:
        file.write(f"{nombre},{nota1},{nota2},{promedio}\n")

def verificar_aprobacion(nombre_alumno):
    # Leer el archivo calificaciones.txt
    with open("calificaciones.txt", "r") as file:
        for linea in file:
            datos = linea.strip().split(",")
            nombre = datos[0]
            promedio = float(datos[3])
            if nombre == nombre_alumno:
                if promedio >= 10:
                    print(f"Alumno {nombre_alumno}, aprobado.")
                else:
                    print(f"Alumno {nombre_alumno}, desaprobado.")
                return
        print(f"No se encontraron calificaciones para el alumno {nombre_alumno}.")

# Ejemplo de uso
guardar_calificacion("Nicole Ramirez", 18, 16)
guardar_calificacion("Mariana Medina", 12, 8)

verificar_aprobacion("Nicole Ramirez")
verificar_aprobacion("Mariana Medina")
