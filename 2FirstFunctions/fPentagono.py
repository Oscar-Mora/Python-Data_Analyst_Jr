# Crear una función
# Se definen usando la palabra calce def:

 #Construya un programa para calcular el área de un pentágono dado el lado  pentágono.
 # 𝐴 = (1/4) √(5(5 + 2√5)))(𝐿**2)
 #Se piden las entradas
def entrada_de_datos(mensaje):
    lado = float (input(mensaje))
    return lado
    
 #funcion para hacer calculo
def calculo_datos(lado):
    calculo = (1/4)*( (5 *(5+ (2*(5**(1/2) ) )* lado**2) ))**.5
    return calculo
        
#funcion de impresi+on de datos
def imprimir_resultado(mensaje, resultado):
    print(mensaje, resultado)
  
 #funcion PRINCIPAL
def run(): 
    #Entrada de Datos
    lado = entrada_de_datos('Ingrese el valor del lado de su pentagono: ')
    
    #Procesamiento de Datos
    calculo = calculo_datos(lado)
    
    #impresion de resultados
    imprimir_resultado(f"Su resultado es: ", calculo)
    
 
if __name__ == '__main__':
    run()
    