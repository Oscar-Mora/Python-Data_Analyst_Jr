# Construya un programa tal que el precio de un producto importado, incremente 11.2% 
# si el producto tiene un costo inferior a $1500 8.8% en caso contrario y además escriba 
# el nuevo precio del producto.
precio = float(input('Ingrese el precio de su producto: '))
if precio > 1500:
    preciof = precio+(precio * .112)
    print(f"El Precio final de su productos es {preciof} pesos")
else:
    preciof = precio+(precio * .088)
    print(f"El Precio final de su productos es {preciof} pesos")

