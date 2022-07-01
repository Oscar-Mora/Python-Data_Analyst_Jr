#Creando una lista
lista = ['manzana', 'platano', 'Fresa']
print(lista)
#Características de las listas
#• Los elementos de la lista están ordenados, se pueden cambiar y permiten valores 
#duplicados
#• Los elementos de la lista están indexados, el primer elemento tiene [0], el 
#segundo [1], etc

#Permitir duplicados
#Dado que las listas están indexadas, las listas pueden tener elementos con el mismo 
#valor.
lista = ['manzana', 'platano', 'fresa', 'manzana', 'fresa']
print(lista)

#Longitud de una lista
#Para determinar el número de elementos de una lista utilizamos la función len().
lista = ['manzana', 'platano', 'fresa', 'coco']
print( len( lista ) ) # -> 4

# Los elementos de una lista
# Los elementos de la lista pueden ser de cualquier tipo de datos.
lista1 = ['manzana', 'platano', 'fresa']
lista2 = [1, 5, 7, 6, 9]
lista3 = [True, False, False]

#Una lista puede contener diferentes tipos de datos.
lista4 = ['abc', 34, True, 40, 'edgar']

#Acceder a un elemento de la lista
#Los elementos de la lista están indexados y se puede acceder consultando el número de 
#índice. (El primer elemento tiene índice 0)
lista = ['manzana', 'banana', 'fresa']
print( lista[1] ) # -> 'banana'

#Indexación negativa
#La indexación negativa significa comenzar desde el final
#-1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc
lista = ['manzana', 'banana', 'fresa']
print( lista[-1] ) # -> 'fresa'

#Rango de índices
#Puede especificar un rango de índices especificando dónde comenzar y donde terminar.
lista = ['manzana', 'banana', 'fresa', 'naranja', 'kiwi', 'melon', 'mango']
print( lista[2:5] ) # -> ['fresa', 'naranja', 'kiwi']

#Comenzará en el índice 2 (incluido) y terminará en el índice 5 (no incluido).
#Omitir valor inicial
lista = ['manzana', 'banana', 'fresa', 'naranja', 'kiwi', 'melon', 'mango']
print( lista[:4] ) # -> ['manzana', 'banana', 'fresa', 'naranja']

#Omitir valor final
lista = ['manzana', 'banana', 'fresa', 'naranja', 'kiwi', 'melon', 'mango']
print( lista[2:] ) # -> ['fresa', 'naranja', 'kiwi', 'melon', 'mango']

#Rango de índices negativos
lista = ['manzana', 'banana', 'fresa', 'naranja', 'kiwi', 'melon', 'mango']
print( lista[-4:-1] ) # -> ['naranja', 'kiwi', 'melon']

#Comprobar si el articulo existe
#Para determinar si un elemento está presente en una lista.
lista = ['manzana', 'banana', 'fresa', 'naranja']
if 'fresa' in lista:
print('La fresa esta en la lista')

#Cambiar elemento de una lista
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista[1] = 'mango'
print(lista) # -> ['manzana', 'mango', 'fresa', 'naranja']
#Cambiar un rango de valores
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista[1:3] = ['mango', 'sandia']
print(lista) # -> ['manzana', 'mango', 'sandia', 'naranja']

#Si se inserta más elementos de los que se reemplaza, los elementos restantes se moverán 
#en consecuencia.
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista[1:2] = ['mango', 'sandia']
print(lista) # -> ['manzana', 'mango', 'sandia', 'fresa', 'naranja']

#Si se inserta menos elementos de los que reemplaza, se eliminar los demás.
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista[1:4] = ['mango']
print(lista) # -> ['manzana', 'mango']

#Método insert()
#Para insertar un nuevo elemento de lista, sin reemplazar ninguno de los valores 
#existentes, podemos usar el método insert().
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista.insert( 2, 'melon' )
print(lista) # -> ['manzana', 'banana', 'melon', 'fresa', 'naranja']

# Método append()
# Agregar un elemento al final de la lista.
lista = ['manzana', 'banana', 'fresa', 'naranja']
lista.append('sandia')
print(lista) # -> ['manzana', 'banana', 'fresa', 'naranja', 'sandia']

# Extender una lista
# Para agregar elementos de una lista a otra lista actual, utilizamos el método extend().
lista = ['manzana', 'banana', 'fresa']
lista2 = ['naranja', 'mango', 'piña']
lista.extend(lista2)
print(lista) # -> ['manzana', 'banana', 'fresa', 'naranja', 'mango', 'piña']

# Remover un elemento de la lista
lista = ['manzana', 'banana', 'fresa']
lista.remove('banana')
print(lista) # -> ['manzana', 'fresa']

# Remover un elemento especifico
lista = ['manzana', 'banana', 'fresa', 'melon']
lista.pop(2)
print(lista) # -> ['manzana', 'banana', 'melon']

# Si no especificamos el índice, pop() removerá el ultimo ítem
lista = ['manzana', 'banana', 'fresa', 'melon']
lista.pop()
print(lista) # -> ['manzana', 'banana', 'fresa']

# Uso de la palabra del para eliminar elementos
lista = ['manzana', 'banana', 'fresa', 'melon']
del lista[0]
print(lista) # -> ['banana', 'fresa', 'melon']

# Del también pude eliminar una lista por completo.
lista = ['manzana', 'banana', 'fresa', 'melon']
del lista

# Método clear()
# El clear() método, vacía la lista.
# La lista aún permanece, pero no tiene contenido.
lista = ['manzana', 'banana', 'fresa']
lista.clear()
print(lista) # -> []