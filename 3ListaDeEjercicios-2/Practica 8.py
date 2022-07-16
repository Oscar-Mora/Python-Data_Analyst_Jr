# practica 8
# 8.1_ Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, 
# y los valores sean los cuadrados de las claves.

def run():
    numero = int(input("Ingrese un número:"))
    cuads = {}

    for num in range(1,numero+1):
        cuads[num] = num ** 2  # Asignamos el valor de la key al dicc "cuads"[] en este caso num y el VALUE la op de num**num
    for num, valor in cuads.items(): #para cada key value IN CUADS.ITEMS() se imprime
        print("%d -> %d" % (num,valor))

if __name__ == '__main__':
    run()
# 8.2_ Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
#def pedir_palabra(msj):  
#    palabra = input(msj)
#    return palabra
#def destruir_palabra(palabra):
#    
#    contar=0
#    letras = {}
#    for letra in palabra:
#        if letra.isalpha():
#            letras[letra]=[contar]
#    return letras
#def checar_letra(palabra):
#    pass
#    
#def run():
#    palabra = pedir_palabra('Ingrese la palabra que desea: \n ')
#    contar =destruir_palabra(palabra)
#
#    print (contar)
#    
#if __name__=='__main__':
#    run()
    
    
# 8.3_ Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta
#def obtener_fruta():
#    registro_fruta = {}
#    fruta = input('Ingrese el Nombre de la Frtua y su precio separado por ":" \n')
#    datos = data.split(':') registro_fruta(datos[0]) = int(datos[1]) 
#    return registro_fruta
#def run():
#    fruta = obtener_fruta()
#    print(fruta)
#if __name__ == '__main__':
#    run()