# La función __init__()
# Los ejemplos anteriores son clases y objetos en su forma más simple y no son realmente útiles en aplicaciones de la vida real.
# Para comprender el significado de las clases, debemos comprender la función __init__() incorporada.
# Todas las clases tienen una función llamada __init__(), que siempre se ejecuta cuando se inicia la clase.
# Use la función __init__() para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# La __init__()función se llama automáticamente cada vez que la clase se usa para crear un nuevo objeto.
persona1 = Persona('Edgar Erik', 26)

print(persona1.nombre)
print(persona1.edad)