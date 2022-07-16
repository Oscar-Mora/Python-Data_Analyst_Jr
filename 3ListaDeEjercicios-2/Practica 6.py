#6.1.-Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de "Salir".
def crear_menu():
    menu = ''' 
        1)Elevar al cuadrado de un número
        2)Multiplicar 2 números
        3)Dividir 2 números
        4) Salir
    '''
    return int(input(menu))
    
def evaluar_op(op):
while True:
    #if op == 1:
    #    val=int(input('Ingresa el número que vamos a elevar al cuadrado: \n')
    #    while True:
    #    nn = val**val
    #    return nn
        
    if op == 2:
        num1= float(input('dame los dos numeros enteros a multiplicar'))
        num2= float(input('dame los dos numeros enteros a multiplicar'))
        multi = num1*num2
    return multi
    
    if op == 3:
        div1= float(input('dame los dos numeros enteros a multiplicar'))
        div2= float(input('dame los dos numeros enteros a multiplicar'))
        div = div1*div2
        return div 
    if  op == 4:
        break
    else:
        op = crear_menu()
def run():
    op = crear_menu()
    
    res = evaluar_op(op)
    print (res)
        
    
if __name__=='__main__':
    run()
   
##6.2.- Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
#def obtenerN_primos(msj):
#    num = int(input(msj))
#    return num
#def generar_primo(num):
#    while True:
#        temp = num          # asignamos el numero que nos dan a la variable que sumará los n primos
#        while True:
#            temp += 1        # Para validar si es primo asignamos temp en 1 para recorrer y aumentar el valor de temp
#            
#            contador = 1        # contador validará si contador % temp tiene divisores hasta llevar a temp%temp
#            contador_divisores = 0       # Para contar las divisiones con residuo 0 y validar primo
#            
#            while contador <= temp:      # contador arranca desde 1 hasta temp-valor temporal
#                if temp % contador == 0:         # verifica si tiene divisor
#                    contador_divisores += 1     #si sí. Se registra el divisor encontrado
#                    
#                if contador_divisores > 2:      #Si el contador de divisores es mayor a 2, rompemos ciclo
#                    break                       # porque NO ES PRIMO
#                contador +=1                    # Y aumentamos contador para seguir iterando
#                
#            if contador_divisores ==2:  # Si dentro del validador es primo (while contador <= temp:)
#                yield temp
#                numero = temp
#
##def crear_listaPrimos(n):
##    a=[]
##    for i in range(0,n):
##       a.append(i)
##    return a
#
#def run():
#    num =obtenerN_primos('Ingrese la cantidad de números primos que desea ver: ')
#    g = generar_primo(num)
#    
#    primos=[next(g) for n in range(num)]
#
#    print(primos)
#    
#        
#    
#if __name__=='__main__':
#    run()   
#
#
## 6.3.-Una persona adquirió un producto para pagar en 20 meses. 
## El primer mes pagó $10, el segundo$20, el tercero $40 y así sucesivamente. 
## Realizar un algoritmo para determinar cúanto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
#def get_pago():
#    print('Segun el problema el primer pago es $10.00')
#    pago = 10
#    return pago
#
#def abonos(pago):
#    count = 1
#    for i in range(count,21):
#        if count < 21:
#            print('El abono del mes: ', count,' es ',pago)
#        count = count + 1
#        pago = pago + pago
#    return pago
#def pago_total(msj, total):
#    print(msj,total)
#    
#def run():
#    pago = get_pago()
#    abono = abonos(pago)
#    total = pago_total('El pago total de la deuda durante 20 meses es de: ', (abono/2))
#if __name__=='__main__':
#    run()
#        
## 6.4.- Crea una aplicación que pida un número y calcule su factorial(El factorial de un número es el producto de todos los enteros entre1 y el propio número y se representa por el número seguido de un signo de exclamación
## Por ejemplo 5! = 1x2x3x4x5=120)
#
#print('6.4 Realiza un programa que pida un número entero y obtenga la factorial de este.')
#def obtener_numero():
#    fact = 'Ingrese el número que desea factorizar ! :'
#    return int(input(fact))
#def procesar_dato(fact):
#    acum = 1
#    for i in range(1,fact+1,1): # factorial de 5 es 120
#        if fact >=1:
#            acum = acum*i
#    return acum
#def salida(msj,resultado):
#    print(msj,resultado)
#
#def run():
#    fact = obtener_numero()
#    factorial = procesar_dato(fact)
#    salida(f"El factorial de {fact}!: ", factorial)
#
#if __name__=='__main__':
#    run()
