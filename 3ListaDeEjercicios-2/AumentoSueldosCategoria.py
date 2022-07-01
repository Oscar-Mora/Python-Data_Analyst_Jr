# Construya un programa tal que, dado como datos la categoría y el sueldo de un 
# trabajador, calcule el aumento correspondiente teniendo en cuenta la siguiente tabla. 
# Imprima la categoría del trabajador y su nuevo sueldo. (Colocar categoría no validad 
# si se está fuera del rango)
# Categoría Aumento
# 1         15.5%
# 2         10.7%
# 3         8.3%
# 4         7.2%

if __name__ == '__main__':
    selector = int()
    print("Seleccione una Categoría")
    print("1 - 15.5%")
    print("2 - 10.7%")
    print("3 - 8.3%")
    print("4 - 7.2%")
    selector = int(input())
    sueldo = float(input('Ingrese el monto de su sueldo: '))
    if selector==1:
        sueldof = sueldo+(sueldo * .155)
        print(f"Su Sueldo con Aumento de Categoría 1 es {sueldof} pesos")
    elif selector==2:                                    
        sueldof = sueldo+(sueldo * .107)                 
        print(f"Su Sueldo con Aumento de Categoría 2 es {sueldof} pesos")
    elif selector==3:                                    
        sueldof = sueldo+(sueldo * .083)                 
        print(f"Su Sueldo con Aumento de Categoría 3 es {sueldof} pesos")
    elif selector==4:                                    
        sueldof = sueldo+(sueldo * .072)                 
        print(f"Su Sueldo con Aumento de Categoría 4 es {sueldof} pesos")
    else:
        print('La opción indicada no existe')

