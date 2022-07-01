# Escriba un programa, dado como datos el nombre de un animal, su peso y longitud, expresados estos dos últimos en libras y pies respectivamente, escriba el nombre del 
#animal su peso expresado en kilogramos y su longitud expresada en metros.
#• 1 libra es a 0.4536 kilogramo 
#• 1 pie es a 0.3048 metros

## ENTRADA DE DATOS
##--->>>>SIEMPRE RETORNAR DATO<<<<---
def obt_dat_str(mensaje):
    animal = str(input(mensaje))
    return animal
## --->>>>SIEMPRE RETORNAR DATO<<<<---    
def obt_dat_num(mensaje):    
    dato = float (input(mensaje))
    return dato
    
## PROCESAMIENTO DE DATOS --->>>>SIEMPRE RETORNAR DATO<<<<---
def proc_Peso(peso):
    peso_libras = (peso * 0.4536)
    return peso_libras
## --->>>>SIEMPRE RETORNAR DATO<<<<---
def proc_Long(long):
    long_pies = (long * 0.3048)
    return long_pies

## IMPRESION DE RESULTADOS
def imp(m1,animal,m2,peso,m3,long,m4):
    #print(m1,animal,m2,peso,m3,long,m4)
    print(m1,animal,m2,peso,m3,long,m4)


## FUNCION PRINCIPAL
def run():
    print('Se busca generar una Descripcion de animales por Nombre, Peso, Longitud')
    #ENTRADAS
    animal = obt_dat_str('Ingrese el nombre de su animal: ')
    peso = obt_dat_num('Ingrese el peso de su animal el Kgs :')
    long = obt_dat_num('Ingrese la long de su animal el mts :')
    
    #PROCESAMIENTO
    c_peso = proc_Peso(peso)
    c_long = proc_Long(long)
    
    #SALIDAS
    imp('Las características de su ',animal,'son: \n   Peso: ',c_peso,'Libras \n   Longitud: ',c_long,'Pies')
    
    
    
if __name__ =='__main__':
    run()