#Practica 4

# 4.1 Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo(1.2 puntos) 
import random
        
#def calcular_cubo(arr=[a,b,c,d,e,f,g,h,i,j]):
#    acum = 0
#    for i in range (1,10):
def crear_lista(p=[a, b, c, d,e, f, g, h,i,j]):
    list = []
    for i in range (0,9):
        nRand = random.randint(1,10)
        list.append(nRand)
    return list 
def calcular_cuadrado(list):
    a = []
    for i in range (0,9): 
        val = int(p[i])**2
        a = a.append(val)
        print(a)

def calcular_cubo(p ):
    
    for i in range (0,10): 
        a = []
        contador = 0
        val = int(p[i])**3
        a = a.append(int(val))
        print (a)
        
        
def run():
    a = rand()
    b = rand()
    c = rand()
    d = rand()
    e = rand()
    f = rand()
    g = rand()
    h = rand()
    i = rand()
    j = rand()
    p = [a,b,c,d,e,f,g,h,i,j]
    #arr = crear_lista(p)
    print(p)
    array_x_cuadrado = calcular_cuadrado(p)
    print(array_x_cuadrado)
    array_x_cubo = calcular_cubo(p)
    print(array_x_cubo)
        
if __name__ == '__main__':
    run()
    
    
# 4.2 Crear una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista, pero en orden inverso, y muestra sus elementos por la pantalla (1.2 puntos) 



# 4.3 Se requiere realizar un progra,a que lea por teclado loas 5 notas obtenidas por un alumno(comprendidas entre 0 y 10). 
#     A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor (1.2 puntos)



# 4.4 Codifica un programa en python que nos permita guardar los nombre de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
#     Guarda la información en un diccionario cuyas claves serán los nombre de los alumnos y los valores serán listados con las notas de cada alumno.
#     El programa pedirá el número de alumnos que vamos a introducir, pedira su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 
#     Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
#     Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará error. (1.2 puntos)
import math
def obtener_numRegistros():
    n = int(input('Ingrese la cantidad de registros que desea hacer: '))
    return n
def obtener_nombre():
    nombres=[]
    nombre = str(input('Ingrese el nombre del alumno: '))
    nombres.append(nombre)
    return nombres
def obtener_notas():
    lista=[]
    while True:
        nota = float(input('Ingrese la calificación y pulsa ENTER para ingresar la siguiente: '))
        lista.append(str(nota))
        if nota < 0:
            break 
    return lista
def sacar_pomedio(lista):
    n=len(lista)
    while True:
        acum=0
        for i in (0,n):
          acum = acum + lista[i]
        return acum
    prom = acum/len(lista)
    return acum
        
    
def lista_alumnos(nombre,promedio):
    dict_from_list = dict(zip(nombre, promedio))
    return dict_from_list
def run():
    n = obtener_numRegistros()
    for i in range (0,n):
        nombre = obtener_nombre()
        notas = obtener_notas()
        print(len(notas))
        print(notas[:-1])
        promedio = sacar_pomedio(notas) 
        print(promedio)
        lista=lista_alumnos(nombre,promedio)
    return lista
    
    
    
if __name__=='__main__':
    run()



# 4.5 Crear una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. 
#     El programa termina cuando el usuario introduce un cero.(1.2 puntos)
