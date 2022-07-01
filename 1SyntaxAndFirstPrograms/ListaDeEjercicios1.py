   #>>>1.- Construya un programa tal que dado los datos reales A y B, escriba el resultado de la siguiente expresión:
# varA= float(input('Ingrese el valor A: '))
# varB= float(input('Ingrese el valor B: '))
# print('se resolverá la siguiente operación: (3A + B)^3/(7B-(1/2 A))')
# resulAlgo =((3*varA)+varB)**3/((7*varB)-(varA*(1/2)))
# print('El resultado de sus números es: ', resulAlgo)
 

   #>>>2.- Construye un programa que, al recibir como datos el nombre del empleado y los 
   # seis primeros sueldos del año, calcule el ingreso total y el promedio, imprima el
   # nombre del empleado, el ingreso total y el promedio.

# nEmpleado = str(input('Ingrese su nombre Completo: '))
# s1 = float(input('Ingrese el monto de su 1er sueldo: '))
# s2 = float(input('Ingrese el monto de su 2do sueldo: '))
# s3 = float(input('Ingrese el monto de su 3er sueldo: '))
# s4 = float(input('Ingrese el monto de su 4to sueldo: '))
# s5 = float(input('Ingrese el monto de su 5to sueldo: '))
# s6 = float(input('Ingrese el monto de su 6to sueldo: '))
# total = (s1+s2+s3+s4+s5+s6)
# promedio = (total/6)
# print('El Ingreso total de los 6 periodos para',nEmpleado,' es: ',total)
# print('El Ingreso promedio para',nEmpleado,' es: ',promedio)

   #>>>3.- Desarrolla un algoritmo que calcule la edad de una persona con base en la obtención año de nacimiento.

# print('¡Hola, amig@!, adivinaré tu edad..')
# fchaY = int (input('Ingresa el número del Año en que naciste a 4 digitos, ej.. 1993: '))
# edad = 2022 - fchaY
# print ('Su edad es :',edad)

   #>>>4.- Construya un programa que dato a y b reales permita calcular e imprimir los
   #binomios: (a + b), (a + b)2 , (a + b)3 , (a + b)4 .

# print('En este ejercicio se resolverán los binomios: (a + b), (a + b)2 , (a + b)3 , (a + b)4')
# val1 = float(input('Ingrese el 1er valor de su Binomio: '))
# val2 = float(input('Ingrese el 2do valor de su Binomio: '))
# 
# bino1 = (val1 + val2)
# bino2 = (val1 + val2)**2
# bino3 = (val1 + val2)**3
# bino4 = (val1 + val2)**4
# 
# print(f'El valor del 1er binomio es: {bino1}!')
# print(f'El valor del 2do binomio es: {bino2}!')
# print(f'El valor del 3er binomio es: {bino3}!')
# print(f'El valor del 4to binomio es: {bino4}!')

   #>>>5.-Construya un programa para calcular el área de un pentágono dado el lado 
   #pentágono. 𝐴 = 1/4√5(5 + 2√5)𝐿2  
   ## >>>>>>>   CON FUNCIONES   <<<<<<<
#Funcion para obtener el valor del lado del pentagono
 def obtener_lado(mensaje):
    lado = float(input (mensaje))
    return (lado)
#Funcion para procesar el Area del Pentagono
 def area_pentagono(lado): 
    area = (1/4)*((1/2())



