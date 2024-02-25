

def decorador_contadorargumentos(funcion):
    def wrapper(*args, **kwargs):
        print(f"La cantidad de argumentos que tiene la función es: {len(args) + len(kwargs)}")
        resultado = funcion(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper

@decorador_contadorargumentos
def ejemplo_funcion(*args, **kwargs):
    print("Función ejecutada")
    print("Argumentos posicionales:", args)
    print("Argumentos de palabras clave:", kwargs)

# Ejemplo de uso
ejemplo_funcion(1, 2, 4, nombre="Nicole", edad=18)
