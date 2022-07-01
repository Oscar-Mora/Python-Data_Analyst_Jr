# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	bandera = bool()
	print("Operador Y (Conjunción)")
	bandera = (5<10) and (5>=6)
	print("Y : ",bandera)
	print(" ")
	print("Operador O (Disyunción)")
	bandera = (7==7) or (7<0)
	print("O : ",bandera)
	print(" ")
	print("Operador NO (Negación)")
	bandera = not (2<5)
	print("No : ",bandera)
	print(" ")

