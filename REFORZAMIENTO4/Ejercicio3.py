def obtener_profesion():
    persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
    try:
        profesion = persona['profesion']
        print("La profesión es:", profesion)
    except KeyError as e:
        print("Se produjo un error de clave:", e)
        print("La clave 'profesion' no existe en el diccionario 'persona'.")

obtener_profesion()