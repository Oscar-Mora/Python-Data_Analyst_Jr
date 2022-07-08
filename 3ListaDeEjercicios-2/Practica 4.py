#Practica 4

# 4.1 Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo(1.2 puntos) 
#import random
#def crear_lista():
#    list = []
#    for i in range (0,10):
#        nRand = random.randint(1,10)
#        list.append(nRand)
#    return list 
#    
#def calcular_cuadrado(list):
#    a = []
#    for i in range (0,10): 
#        val = int(list[i])**2
#        a.append(val)
#    return a
#
#def calcular_cubo(list):
#    a = []
#    for i in range (0,10): 
#        val = int(list[i])**3
#        a.append(int(val))
#    return a
#    
#def run():
#    list = crear_lista()
#    print('La lista de números aleatorios es: ',list)
#    array_x_cuadrado = calcular_cuadrado(list)
#    print('Sus cuadrados son: ',array_x_cuadrado)
#    array_x_cubo = calcular_cubo(list)
#    print('Sus cubos son: ',array_x_cubo)
#    for i in range (0,10):
#        print(f"Para el valor {list[i]}, elevando al cuadrado da: {array_x_cuadrado[i]}, elevado al cubo es: {array_x_cubo[i]}")
#        
#if __name__ == '__main__':
#    run()
    
    
# 4.2 Crear una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista, 
# pero en orden inverso, y muestra sus elementos por la pantalla (1.2 puntos) 
#def obtener_5strings(msj):
#    str5= []
#    for i in range (0,5):
#        i = [input(msj)]
#        str5.append(i)
#    return str5
#
#def run():
#    palabras = obtener_5strings('Ingrese 5 palabras, pulsa ENTER al ingresar cada una: ')
#    palabras2 = palabras[::-1]
#    print(f"La lista de palabras es: {palabras}")
#    print(f"La lista de palabras al reves es: {palabras2}")
#if __name__=='__main__':
#    run()

# 4.3 Se requiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno(comprendidas entre 0 y 10). 
#     A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor (1.2 puntos)
#def obtener_notas(msj):
#    list=[]
#    for i in range(0,5):
#        n = int(input(msj))
#        list.append(n)
#    return list
#    
#def traer_Nmedia(list):
#    contador=0
#    for i in list:
#        contador = contador + i 
#    return contador
#    
#def traer_Nmayor(list):
#    list.sort()
#    return list[-1]
#def traer_Nmenor(list):
#    list.sort()
#    return list[0]
#def run():
#    notas= obtener_notas('Ingrese sus 5 notas, pulsa ENTER despues de cada nota ingresada: ')
#    media = traer_Nmedia(notas)/len(notas)
#    mayor=traer_Nmayor(notas)
#    menor= traer_Nmenor(notas)
#    print(f"Sus notas son: {notas}")
#    print(f"La notas media es: {media}")
#    print('La nota mayor es: ',mayor)
#    print('La nota menor es: ',menor)
#if __name__ =='__main__':
#    run()

# 4.4 Codifica un programa en python que nos permita guardar los nombre de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
#     Guarda la información en un diccionario cuyas claves serán los nombre de los alumnos y los valores serán listados con las notas de cada alumno.
#     El programa pedirá el número de alumnos que vamos a introducir, pedira su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 
#     Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
#     Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará error. (1.2 puntos)
def cantidad_alumnos():#define cantidad de alumnos
    cantidad=int(input('Ingrese la cantidad de alumnos a registrar: '))
    return cantidad
    
def obtener_nombre():
    nombre = str(input('Ingrese el nombre completo del alumno: '))
    return nombre
    
def obtener_notas():#distinta cantidad de notas hasta introducir numero negativo
    count = 0
    while True:
        nota = float(input('Introduzca su nota y de enter para ingresar la siguiente nota: '))
        count = count + nota
        if nota < 0:
            break
    return count
    
def promedio(notas):
    count = 0
    promedio = 0
    while True:
        for nota in notas:
            count = count+nota
            return count
    
    promedio = count/len(notas)
    return promedio
    
def creando_alumnos(): #Claves nombre y valores de las notas la funcion debe ser como un constructor
    alumnos= {}
    for nombre,notas in alumnos.items():
        nombre = nombre
        notas = notas
        alumnos = {nombre : nombre for alumno in alumnos}
    return  alumnos
#En main devuelve nombre de alumno y promedio
def run():
    
    cantidadDeAlumnos = cantidad_alumnos()
    nombre = obtener_nombre()
    notas = obtener_notas()
    
    lista=alumnos(cantidadDeAlumnos,'oscar',[5,6,7,8,9])
    
    
if __name__=='__main__':
    run()




# 4.5 Crear una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. 
#     El programa termina cuando el usuario introduce un cero.(1.2 puntos)