# Construya un programa que resuelva el problema que tienen en una gasolinera. Los 
# surtidores de esta registran lo que “surten” en galones, pero el precio de la 
# Gasolina esta fija en litros. El diagrama de flujo debe calcular e imprimir lo que hay que cobrarle al cliente. (El precio del litro es $22.80)
# 1 galón es 3.785 litros

#ENTRADAS
def obt_datos(mensaje):
    gal = float(input(mensaje))
    return gal

#PROCESAMIENTO
def calcular(gal):
    convert = gal * 3.785
    return convert
    
#SALIDA
def salida(msj,resul, msj2):
    print(msj,resul, msj2)
    
#MAIN
def run():
    #entradas
    gal = obt_datos('Ingrese la cantidad de Galones que registró Hoy: ')
    
    #procesamiento
    lts = calcular(gal)
    
    #salida
    salida('Los galones registrados equivale a ',lts, 'Litros' )
    
if __name__=='__main__':
    run()