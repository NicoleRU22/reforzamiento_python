def division():
    string = "Hello Pythonista"
    try:
        result= string / 0
        print(result)
    except TypeError as e:
        print("Se produjo un error de tipo:", e)
    except ZeroDivisionError as e:
        print("Se produjo un error de división por cero:", e)
        print("No es posible dividir un string por cero")

division()