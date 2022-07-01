# Ciclos en Python
# En Python tenemos dos estructuras para crear ciclos
# • while
# • for
# Ciclo While
# Podemos ejecutar un conjunto de instrucciones siempre que una condición sea verdadera

i = 1
while i < 1000:
    print(i)
    i = i + 1
    
# Python cuenta con un tipo de datos especial que nos ayuda con el ciclo for, el cual nos 
# regresa una lista de [0,…,n-1]

a = list( range(1000) )
print( a )

# Ciclo for
# El ciclo for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un 
# diccionario, un conjunto o una cadena).

# Ejemplo 1
# Iterar en un rango(lista)
for i in range(1001):
    print(i)


# Ejemplo 2
# Iterar lista
frutas = ["manzana", "limon", "mango"]
for x in frutas:
    print(x)

#Ejemplo 3
# Iterar una cadena
for x in "manzana":
    print(x)