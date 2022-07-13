# Métodos de objetos
# Los objetos también pueden contener métodos. Los métodos en los objetos son funciones que pertenecen al objeto.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def decirHola(self):
        print('Hola mi nombre es ' + self.nombre)

persona1 = Persona('Edgar Erik', 26)
persona1.decirHola()

# El self parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase.