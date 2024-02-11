"""
12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:

Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)
"""
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadircontacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)

    def mostrarcontactos(self):
        print("Contactos en la agenda:")
        for contacto in self.contactos:
            print("Nombre:", contacto['nombre'])
            print("Teléfono:", contacto['telefono'])
            print("Email:", contacto['email'])
            print("DNI:", contacto['dni'])
            print("----------------------")

    def buscarcontacto(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni:
                print("Contacto encontrado:")
                print("Nombre:", contacto['nombre'])
                print("Teléfono:", contacto['telefono'])
                print("Email:", contacto['email'])
                print("DNI:", contacto['dni'])
                return
        print("No se encontró ningún contacto con ese DNI.")

mi_agenda = Agenda()

mi_agenda.añadircontacto("Nicole", "975982364", "nicole@gmail.com", "45685467")
mi_agenda.añadircontacto("Alexandra", "956523626", "alexandra@gmail.com", "87654321")
mi_agenda.añadircontacto("Pedro", "917964376", "pedro@gmail.com", "65432198")

mi_agenda.mostrarcontactos()

mi_agenda.buscarcontacto("45685467")

