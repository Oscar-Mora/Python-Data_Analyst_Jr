# Herencia de Python

# La herencia nos permite definir una clase que hereda 
# todos los métodos y propiedades de otra clase.

# La clase principal es la clase de la que se hereda, 
# también llamada clase base.

# La clase secundaria es la clase que hereda de otra clase, 
# también llamada clase derivada.

# Creando una clase principal
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def escribirNombreCompleto(self):
        print('Mi nombre completo es ' + self.nombre + ' ' +  self.apellido)

# Probamos la clase 
sujeto = Persona('Edgar Erik', 'Andrés Urbano')
sujeto.escribirNombreCompleto()

# Creando clase secundario
# Para crear una clase que herede la funcionalidad de otra clase, 
# envíe la clase principal como parámetro al crear la clase secundaria:

class Estudiante(Persona):
    pass # utilice la passpalabra clave cuando no desee agregar otras propiedades o métodos a la clase.

# Ahora la clase Estudiante tiene las mismas propiedades y métodos que la clase Persona.
sujeto2 = Estudiante('Guillermo', 'Santiago')
sujeto2.escribirNombreCompleto()
