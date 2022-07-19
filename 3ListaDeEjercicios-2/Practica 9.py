#Practica 9 
# 9.1_ Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no 
# (en caso que la respuesta sea incorrecta el programa debe indicar cúal es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos

#def run():
#    import random
#    aciertos = 0
#    for indice in range(10):
#        # Genero dos números aleatorios
#        num1 = random.randint(2,10)
#        num2 = random.randint(2,10)
#        # Calculo la multiplicación
#        resultado = num1*num2
#        # Mostramos la operación de multiplicar y pedimos al usuario que
#        # indique el resultado.
#        print("Multiplicación ",indice)
#        print(num1," * ",num2," = ")
#        num_usuario = int(input())
#        # Si acierta incrementamos el número de aciertos.
#        if num_usuario == resultado:
#            aciertos +=1
#        else:
#            # Si no acierta muestro la respuesta correcta.
#            print("No has acertado. La respuesta es ",resultado)
#        # Mostramos el número de aciertos
#        print("Tu nota ha sido: ",aciertos)
#
#if __name__=='__main__':
#    run()

#9.3_ Obtener la cantidad de elementos mayores a 5 en la tupla.                 ###INCOMPLETO
#def run():
#    tupla0 =(5,2,6,7,8,10,77,55,2,1,30,4,2,3)   
#       
#    for i in tupla0:
#        major_five = list(filter(lambda x: x > 5, tupla0))
#   
#    print('Los valores de la tupla son: ',tupla0)
#    print('Los valores mayores a 5 en la tupla son: ',major_five)
#    
#if __name__=='__main__':
#    run()
#
##9.4_ Obtener la suma de todos los elemento de la lista
#def run():    
#    lista = [1,2,3,4,5,6,7,8,9,10]
#    lista1= lista.sum()
#    print(lista1)
#if __name__=='__main__':
#    run()
