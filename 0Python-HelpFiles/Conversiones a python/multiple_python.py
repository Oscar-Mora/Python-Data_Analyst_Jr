# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	selector = int()
	print("Seleccione una opción")
	print("1 - Hamburgesa")
	print("2 - Pizza")
	print("3 - Queso")
	print("4 - Leche")
	print("Cualquir número otra cosa")
	selector = int(input())
	if selector==1:
		print("Seleccionaste Hamburgesa")
	elif selector==2:
		print("Seleccionaste Pizza")
	elif selector==3:
		print("Seleccionaste Queso")
	elif selector==4:
		print("Seleccionaste Leche")
	else:
		print("Seleccionaste Otra cosa")

