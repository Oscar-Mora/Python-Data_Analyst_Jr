# 8. Genere tres números A, B y C aleatorios utilizando randind de la librería random, 
# construya un programa para escribir cual de estos números es el mayor.

#Obtener Datos
import random 
def rand():
    nRand = random.randint(1,100)
    return nRand


#Solucion calculo
def elMayor(A,B,C):#//a-10 b-5 c-2      //a-1 b-15 c-10   //a-2 b-3 c-10
    if A > B and A > C :
        return A
    elif B > C and B > A:
        return B
    elif C > A and C > B:
        return C
    else:
        print('Alguno es igual a otro')
        
#Imprimir datos
def imprime(msj,res):
    print(msj,res)

#Main function
def run():
    a=rand()
    b=rand()
    c=rand()
    imprime('El número A es: ',a)
    imprime('El número B es: ',b)
    imprime('El número C es: ',c)
    mayor=elMayor(a,b,c)
    salida=imprime('El mayor es: ',mayor)
if __name__ =='__main__':
    run()