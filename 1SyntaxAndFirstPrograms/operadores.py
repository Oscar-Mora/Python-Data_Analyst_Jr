import math
#ejemplo sqrt raíz cuadrada
#print(math.sqrt(9))
#ejemplo sqrt raíz cuadrada con decimal
#print(math.sqrt(11.11))

#Datos primitivos en python
#Integers : Números  Enteros
#Floats: Números de punto flotante(decimales)
#Strings : Cadenas de caracteres
#Boolean:  Verdadero o Falso

##REALIZA OPERACIONES DE + - * / % **

num1 = float (input('Ingrese un número: '))
num2 = float (input('Ingrese otro número: '))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2  #Division con decimales
divInt = num1 // num2  # División sin  decimales
mod = num1 % num2  
expp = num1 ** num2
print(' La suma de sus números es: ',suma)
print(' La resta de sus números es: ',resta)
print(' La multiplicación de sus números es: ',multi)
print(' La división de sus números es: ',div)
print(' La división Entera de sus números es: ',divInt)
print(' El residuo de sus números es: ',mod)
print( num1,' Elevado a ',num2,' es ',expp)


