import Ejercicio14

nombre, apellido = Ejercicio14.nombre_apellido()
print("Su nombre completo:", nombre, apellido)

tipo_seguro = Ejercicio14.ingresar_tipo_seguro()
print("Su tipo de seguro es:", tipo_seguro)

es_mayor = Ejercicio14.mayor_edad()
if es_mayor:
    print("Usted es mayor de edad.")
else:
    print("No es mayor de edad.")
