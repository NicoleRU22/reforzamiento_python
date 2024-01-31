"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor
desalario en consola.

var[‘key’] = tuValor""" 

empleado = {
    "nombre": "Nicole Ramirez",
    "edad": 18,
    "salario": 5600
}

empleado["dni"] = "1234567890"
print(empleado)
print(empleado["salario"])
