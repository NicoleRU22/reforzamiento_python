

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("¡Buenos días!")
        resultado = funcion(*args, **kwargs)
        print("Hasta luego")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    return f"Soy {nombre}"

mensaje = saludar("Nicole")
print(mensaje)
