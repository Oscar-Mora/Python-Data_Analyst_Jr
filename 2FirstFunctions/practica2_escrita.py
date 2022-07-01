# Escriba un programa que convierta un valor dado en grado Farenheit a grados Celsius. 
# Recordar que la fórmula para conversión es: °C = (°F - 32) / 1.8

fVar = float (input('Indique su temperatura en Grados farenheit: '))
conver = (fVar - 32)/1.8
cVar = conver
print('La conversión de la Temperatura ingresada es: ',cVar,' °C')

#Dados dos números, mostrar la suma. resta. división y multiplicación de ambos
print('')
print('Se realizarán las 4 operaciones básicas con 2 números dados')
numA = float(input('Indique el valor de su 1er Número: '))
numB = float(input('Indique el valor de su 2do Número: '))
suma = numA+numB
rest = numA-numB
div = numA/numB
mult = numA*numB
print(f"La Suma de {numA} y {numB} es: {suma}")
print(f"La Resta de {numA} y {numB} es: {rest}")
print(f"La División de {numA} y {numB} es: {div}")
print(f"La Multiplicación de {numA} y {numB} es: {mult}")

#Calcular el perimetro y área de un rectangulo dada su base y su altura
print('')
print('Se calculará el perimetro y el área de un rectangulo')
base = float(input('Indique la longitud de la BASE de su rectangulo: '))
altura = float(input('Indique la longitud de la ALTURA de su rectangulo: '))
peri = (base*2)+(altura*2)
area = base*altura
print(f"El perimetro de su Rectángulo es {peri} centimetros, \n El Área de su Rectángulo es {area} cm2")

#Calcular la medida de tres números pedidos por teclado
print('')
print('Se calculará la media de 3 números dados por usted')
n1 = float(input('Indique el valor de su 1er Número: '))
n2 = float(input('Indique el valor de su 2do Número: '))
n3 = float(input('Indique el valor de su 3er Número: '))
avrg = (n1+n2+n3)/3
print(f"La media de sus 3 números es {avrg}")
