# Modificar propieadades de objetos

from tokenize import PseudoExtras


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creando el objeto
persona1 = Persona('Edgar Erik', 26)

# Modificando objeto
persona1.edad = 73

# Eliminar propieadad de un objeto
del persona1.edad

# Eliminar objeto
del persona1