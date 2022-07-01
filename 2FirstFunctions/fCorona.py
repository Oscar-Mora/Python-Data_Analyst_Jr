# Construya un programa para calcular el área de una corona circular dados el radio mayor y radio menor.
# 𝐴 = 𝜋(𝑅2 − 𝑟2)

#ENTRADA DE DATOS
def obtener_dato(mensaje):
    rMm = float(input(mensaje))
    return rMm

#PROCESAMIENTO DE DATOS
def process_datos(rMay, rMen):
    PI = 3.1416
    A = PI * (rMay - rMen)
    return A

#IMPRESION DE RESULTADOS
def imprimir(mensaje, resultado):
    print(mensaje,resultado)

#>>>>>>>>>>>>>_**SIEMPRE EMPEZAR CON LA FUNCION PRINCIPAL**_<<<((((((((((
def run():
    #Entrada de Datos
    rMay = obtener_dato('Ingrese el valor del Radio Mayor de su Corona: ')
    rMen = obtener_dato('Ingrese el valor del Radio Menor de su Corona: ')
    #Procesamiento de Datos
    calculo = process_datos(rMay, rMen)
    
    #impresion de resultados
    imprimir(f"Su resultado es: ", calculo)
    
    
if __name__ =='__main__':
    run()

    