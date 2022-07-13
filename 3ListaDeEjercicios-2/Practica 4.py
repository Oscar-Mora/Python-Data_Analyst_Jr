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
#    maximo=max(list)
#    return maximo
#def traer_Nmenor(list):
#    minimo=min(list)
#    return minimo
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
#Obtener Cantidad de Alumnos a Registrar
#def cant_alumnos(msj):
#    cantidad = int(input(msj))
#    return cantidad
#    
##Obtener Nombre del Alumno
#def obt_nombre(msj):
#        list = []
#        nombre = (input(msj))
#        list.append(nombre)
#        return list
#        
#        
#def obt_notas(msj):
#    list= []
#    nota= int(input(msj))
#    list.append(nota)
#    while nota >=0:
#        nota= int(input(msj))
#        list.append(nota)
#        if nota < 0 :
#           list.pop() 
#    return list
#
#
#def obt_Media(notas):
#    acum = 0
#    list=[]
#    for i in notas:
#        acum = acum + i
#        promedio = acum/len(notas)
#        list.append(promedio)
#    return list
#
#
#def objeto_Alumno(nombre,promedio,n):
#    registro = []
#    while True:
#        for i in range (0,n):
#            registro.append(dict({nombre:promedio}))
#        return registro    
#
#
#def run():
#    
#    nAlumnos=cant_alumnos('Ingrese la cantidad de alumnos que desea capturar: ')
#    
#    for i in range(0,nAlumnos):
#        nombre=obt_nombre('Ingrese el nombre del alumno: ')
#        notas = obt_notas('Después de cada nota, de ENTER y al finalizar escriba un # Negativo: \n')
#        promedio = obt_Media(notas)
#        registro = objeto_Alumno(tuple(nombre),tuple(promedio),nAlumnos)
#    
#    
#    print(registro)
#    print(nombre)
#    
#    print(notas)
#if __name__=='__main__':
#    run()




# 4.5 Crear una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, 
#     muestra el contenido de esa posición sino muestra un mensaje de error. 
#     El programa termina cuando el usuario introduce un cero.(1.2 puntos)
def l_meses():
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
    return meses


def traer_mes(msj,meses):
    mes = int(input(msj))
    if mes >=1 or mes<=12:
        i = meses[mes-1]
    elif mes<1 or mes >12:
        input('El número debe estar entre 1 y 12, ingrese el número: ')  
    print( i)


def run():
    meses = l_meses()
    m_elegido = traer_mes('Escriba el número del mes que desea ver: ',meses)
    

if __name__=='__main__':
    run()