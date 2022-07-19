#PRACTICA 7
#7.1_ Vamos a crear  una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# -     Un constructor, donde los datos puedan estar vacíos.
# -     Los setters y getter para cada uno de los atributos. Hay que validar las entradas de datos.

#Crear los siguientes métodos:
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad
#class Persona:
#    
#    #Definimos el constructor
#    def __init__(self,nombre,edad,dni):
#        self.nombre = nombre
#        self.edad = edad
#        self.dni = dni
#    #definimos los setters y getters
#    
#    # Generar la instancia de nombre
#    
#    def setNombre(self,nombre):
#        self.nombre = nombre       
#    # Traer la instancia de edad
#    def getNombre(self):    
#        return self.nombre
#        
##setters para asignar edad
#    def setEdad(self,edad):
#        self.edad = edad
#    # Traer las instancias de edad
#    def getEdad(self):    
#        return self.edad
#        
#    #setters de DNI
#    def setDni(self,dni):
#        self.dni = dni
#    #traemos el DNI
#    def getDni(self):
#        return self.dni
#    #METODOS
#    def mostrar(x):
#        print ("El nombre de la persona es:", x.nombre)
#     #Usamos el staticmethod para crear funciones de utilidad   que no necesitan parametros para funcionar obligatoriamente
#    #@staticmethod ## Para checar si alguien es mayor de edad
#    def isAdult(self):
#        print( self.edad > 18)
        
#persona1=Persona('Edgar',22,19999)
#persona1.mostrar()
#persona1.isAdult()
        
#7.2_ Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
#El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# -     Un constructor, donde los datos puedan estar vacíos.
# -     Los setteres y getters para cada uno de los atributos. El atributo no se puede modificar directamente, solo ingresando o retirando dinero.
    #Crear los siguientes métodos:
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, nose hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Cuenta:
    #CONSTRUCTOR
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad= cantidad
    #SETTERS
    def setCantidad(self,titular):
        self.titular=titular
    def setCantidad(self,cantidad):
        self.cantidad=cantidad
    
    #GETTERS
    def getTitular(self, titular):
        return self.titular
    def getCantidad(self, cantidad):
        return self.cantidad
    #METODOS
    def mostrar(self):
        print ("El nombre del Titular es:"+ self.titular)
        print("La cantidad de la cuenta es %d"% (self.cantidad))
    
    def ingresar(self,):
        cant= float(input('Ingrese la cantidad que va a depositar: ')) 
        if cant <0:
            None
        else:
            self.cantidad += cant
        print('Se nuevo saldo es: ',self.cantidad)
    def retirar(self,):
        cant= float(input('Ingrese la cantidad que va a retirar: ')) 
        self.cantidad -= cant
        print('Se nuevo saldo es: ',self.cantidad)
            
usuario1=Cuenta('Aldo',1000)
usuario1.mostrar()
usuario1.ingresar()
usuario1.retirar()


#7.3_ VAmos a definir ahora una "Cuenta Joven", para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior.
#      Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará 
#      expresada en tanto´por ciento. Construye los siguientes métodos para la clase:
# -     Un constructor.
# -     Los setters y getters para el nuevo atributo.
# -     En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método 
#       es TitularValido() que devuelva verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# -     Además, la retirada de dinero sólo se podrá si el titular es válido.
# -     El método mostrar() debe devolver el mensaje de "Cuenta Joven" y la bonificación de la cuenta.
# -     Piensa los métodos heredados de la clase madre que hay que reescribir.

class CuentaJoven(Cuenta):
    
    
    def __init__(self,titular,cantidad):
        self.bonificacion = bonificacion
        #https://www.geeksforgeeks.org/getter-and-setter-in-python/
        
        
    
