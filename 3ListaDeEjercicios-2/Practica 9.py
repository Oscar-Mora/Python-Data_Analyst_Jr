# practica 8
# 8.1_ Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, 
# y los valores sean los cuadrados de las claves.

#def run():
#    numero = int(input("Ingrese un número:"))
#    cuads = {}
#
#    for num in range(1,numero+1):
#        cuads[num] = num ** 2  # Asignamos el valor de la key al dicc "cuads"[] en este caso num y el VALUE la op de num**num
#    print('Se muestran los valores del 1 hasta ',numero,'Seguido de su valor al cuadrado:')
#    for num, valor in cuads.items(): #para cada key value IN CUADS.ITEMS() se imprime
#        print("%d -> %d" % (num,valor))
#
#if __name__ == '__main__':
#    run()
# 8.2_ Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
#def imprimir_items(dic):
#    for clave,valor in dic.items():
#        print (clave,"->",valor)
#def run():
#    dic = {}
#    cadena = input("Dame una cadena:")
#    for caracter in cadena:
#        if caracter in dic:
#            dic[caracter]+=1
#        else:
#            dic[caracter]=1	
#    
#    res= imprimir_items(dic)
#
#if __name__ == '__main__':
#    run()    
    
# 8.3_ Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta
#def run():
#    precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
#    while True:
#        fruta = input("Dime la fruta que has vendido:")
#        if fruta.lower() not in precios:
#            print("Fruta no existe.")
#        else:
#            cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
#            print("El precio final es de %f" % (cantidad * precios[fruta]))
#        opcion = input("¿Quieres vender otra fruta (s/n)")
#        while opcion.lower() != "s" and opcion.lower() != "n":
#            opcion = input("¿Quieres vender otra fruta (s/n)")
#        if opcion.lower() == "n":
#            break
#
#if __name__ == '__main__':
#    run()  
