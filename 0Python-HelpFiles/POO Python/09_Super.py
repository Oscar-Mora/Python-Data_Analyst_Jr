# Usar la función super()
# Python también tiene una super() función que hará que la clase 
# secundaria herede todos los métodos y propiedades de su padre

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def escribirNombreCompleto(self):
        print('Mi nombre completo es ' + self.nombre + ' ' +  self.apellido)

# Agreamos __init()__ a la clase Estudiante
# Cuando agrega la __init__()función, la clase secundaria ya no heredará la __init__()función principal.
class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_graduacion):
        super().__init__(nombre, apellido)
        self.fecha_graduacion = 2020

    # Agregando un nuevo metodo a la clase estudiante
    def escribirFechaGraduacion(self):
        print('Hola soy ' + self.nombre + ' ' + self.apellido + ' ' + 'y me gradua en ' + str(self.fecha_graduacion) )


edgar = Estudiante('Edgar Erik', 'Andrés Urbano', 2020)
edgar.escribirNombreCompleto()
edgar.escribirFechaGraduacion()

