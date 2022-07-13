# Agregar función __init__()
# Hasta ahora hemos creado una clase secundaria que hereda las propiedades y métodos de su padre.

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def escribirNombreCompleto(self):
        print('Mi nombre completo es ' + self.nombre + ' ' +  self.apellido)

# Agreamos __init()__ a la clase Estudiante
# Cuando agrega la __init__()función, la clase secundaria ya no heredará la __init__()función principal.
class Estudiante(Persona):
    def __init__(self, nombre, apellido):
        # Agregar propiades aqui
        pass


