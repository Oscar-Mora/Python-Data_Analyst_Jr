   #A. Imprimir los números enteros del 1 al 100. (contador)
#   print('A. Imprimir los números enteros del 1 al 100. (contador)')
#   for i in range(1,101):
#       print(i)


    #B. Sumar los números enteros del 1 al 100 e imprimir el resultado. (acumulador)
#   print('B. Sumar los números enteros del 1 al 100 e imprimir el resultado. (acumulador)')
#   acum = 0
#   for i in range (1,101):
#       acum = acum + i
#   
#   print(acum) #para imprimir el resultado final me salgo del ciclo y lo imprimo

   # C. Diseñe un programa que reciba una cantidad arbitraria de números reales y calcule su promedio, dejar de 
   # recibir números cuando se introduzca -1 . (bandera o centinela)
#   print('C. Diseñe un programa que reciba una cantidad arbitraria de números reales y calcule su promedio, dejar de \n recibir números cuando se introduzca -1 . (bandera o centinela)')
#   
#   acum = 0
#   cont = 0
#   avg = 0 
#   while True:
#       num= float(input('Ingrese un numero: '))    
#       if num == -1:
#           break
#       else:
#           acum = acum + num
#           cont = cont +1
#   avg = acum/ cont
#   print('El promedio de sus números es: ', avg)

   # 1. Realiza un programa, que muestre los primeros 100 números de forma inversa, es decir, del 100 al 1.
#   print('1. Realiza un programa, que muestre los primeros 100 números de forma inversa, es decir, del 100 al 1.')
#   for  i in range (100,0,-1):
#       print(i)
    

   # 2. Realiza un programa, que muestre únicamente, los números pares en el rango del 1 al 1000.
#   print('2. Realiza un programa, que muestre únicamente, los números pares en el rango del 1 al 1000.')
#   for i in range(0,1001,2):
#           print(i)

   # 3. Realiza un programa que muestre la suma de los números impares del 1 al 100.
#   print('3. Realiza un programa que muestre la suma de los números impares del 1 al 100.')
#   for i in range(1,101,2):
#       print(i)

   # 4. Realiza un programa que pida dos números enteros e imprima los números que existen entre estos dos.
#   print('4. Realiza un programa que pida dos números enteros e imprima los números que existen entre estos dos.')
#   n1 = int(input('Ingrese el primer núm: '))
#   n2 = int(input('Ingrese el segundo núm:'))
#   for i in range(n1,n2,1):
#       print(i)
#   print(f"Los números intermedios entre {n1} y {n2} son: ", i)

   # 5. Realiza un programa que pida un número e imprima la tabla de multiplicar de ese número.
#   print('5. Realiza un programa que pida un número e imprima la tabla de multiplicar de ese número.')
#   cont = 11
#   nMult = int(input('Ingrese el número de la Tabla de Múltiplicar que desee ver: '))
#   for i in range(1,cont,1):
#       print(f"{nMult}*{i} = ", nMult*i)

   # 6. Realiza un programa que pida un número entero y obtenga la factorial de este.
#   print('6. Realiza un programa que pida un número entero y obtenga la factorial de este.')
#   fact = int(input('Ingrese el número que desea factorizar ! :'))
#   acum = 1
#   for i in range(1,fact+1,1): # factorial de 5 es 120
#       if fact >=1:
#           acum = acum*i
#   print(f"El factorial de {fact}!: ", acum)
    
    
   # 7. Realizar un programa, que muestre un menú en pantalla con las opciones:
   # 1) Sumar
   # 2) Restar
   # 3) Multiplicar
   # 4) Dividir
   # 5) Salir
   # El usuario debe seleccionar una opción y a continuación, el programa debe solicitar el ingreso de dos números 
   # reales, para realizar operación, la ejecución debe realizarse una y otra vez, hasta que el usuario selección la 
   # opción salir.
op = int(input(f"\n    'Seleccione una opción': \n    1) Sumar \n    2) Restar \n    3) Multiplicar \n    4) Dividir \n    5) Salir \n Su opción:"))
num1 = float(input(''))
num2 = float(input(''))