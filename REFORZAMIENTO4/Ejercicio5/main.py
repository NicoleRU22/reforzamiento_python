

# Archivo: main.py
import validar

nombre_usuario = input("Ingrese el nombre de usuario: ")

resultado= validar.validarusuario(nombre_usuario)

if resultado is True:
    print("El nombre de usuario es válido.")
else:
    print(resultado)
