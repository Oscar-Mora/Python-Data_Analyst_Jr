# self parámetro
# El self parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase.

# No tiene que ser nombrado self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función en la clase

class Persona:
    def __init__(yo_mismo, nombre, edad):
        yo_mismo.nombre = nombre
        yo_mismo = edad

    def decirHola(yo):
        print('Hola mi nombre es ' + yo.nombre)
    
sujeto = Persona('Edgar Erik', 26)
sujeto.decirHola()