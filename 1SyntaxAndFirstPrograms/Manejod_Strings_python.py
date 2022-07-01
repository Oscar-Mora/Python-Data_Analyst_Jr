Ejemplo de cadenas de caracteres en Python
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
Ejemplo 2
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 1
print( nombre.upper() )
Ejemplo 2
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 2
print( nombre.capitalize() )
Ejemplo 3
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 3 Recuperar valor del método
nombre2 = nombre.capitalize()
print(nombre2)
Ejemplo 4
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 4 
print( nombre.strip() )
Ejemplo 5
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 5
print( nombre.lower() )
Ejemplo 6
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 6
print( nombre.replace('e', 'x') )
Ejemplo 7
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Acceder a caracter especifico
# Regrsa el valor si no hay variable no se guardara
print( nombre[0] )
print( nombre[3] )
Ejemplo 8
# Cadenas de caracteres
nombre = input("¿Cuál es tu nombre?: ")
print( nombre )
# Metodo 7
print( len( nombre ) )
Slices en Python
#En Python, los slices, traducidos al español como “rebanadas”, nos permiten dividir los 
#caracteres de un string de múltiples formas.

#Ejemplo 1
nombre = "Edgar Erik"
# Slices
print( nombre[0] )# E
print( nombre[4] )# r

#Ejemplo 2 muestra desde inicio hasta uno antes[3]
nombre = "Edgar Erik"
# Slices 2
print( nombre[0:3] ) # ---> Edg 

#Ejemplo 3
nombre = "Edgar Erik"
# Slices 3 muestra de inicio hasta uno antes [3]
print( nombre[:3] ) #--> Edg

#Ejemplo 4 muestra desde el [3] hasta final
nombre = "Edgar Erik"
# Slices 4
print( nombre[3:]) #--->ar Erik

#Ejemplo 5 muestra desde el [1] hasta 1 antes [7]
nombre = "Edgar Erik"
# Slices 5
print( nombre[1:7] ) #--> dgar E

#Ejemplo 6 desde indice 1 hasta uno antes 7 en ciclos de 2 como es numero impar ya no muestra el 4 valor sería d,a," ".
nombre = "Edgar Erik"
# Slices 6
print( nombre[1:7:2] )#---> da

#Ejemplo 7 sin poner donde inicia y donde termina, como no pusimos el ciclo en que queremos que vaya tomando y mostrando valores, inicia del principio a fin
nombre = "Edgar Erik"
# Slices 7
print( nombre[::] ) #-->Edgar Erik

#Ejemplo 8 empezando en el indice[1], me muestra valores, contando despues de [1] 3 posiciones y devolviendo valores hasta terminar
nombre = "Edgar Erik"
# Slices 8
print( nombre[1::3] )#--->drr

#Ejemplo 9  sin poner de donde inicio y donde termino hara en ciclos de -1 lo cual mostrará el string a la inversa
nombre = "Edgar Erik"
# Slices 9
print( nombre[::-1] )#--->kirE ragdE