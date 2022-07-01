Proceso multiple_python
	Definir selector Como Entero;
	Escribir "Seleccione una opción";
	Escribir "1 - Hamburgesa";
	Escribir "2 - Pizza";
	Escribir "3 - Queso";
	Escribir "4 - Leche";
	Escribir "Cualquir número otra cosa";
	
	Leer selector;
	
	Segun selector Hacer
		1:
			Escribir "Seleccionaste Hamburgesa";
		2:
			Escribir "Seleccionaste Pizza";
		3:
			Escribir "Seleccionaste Queso";
		4:
			Escribir "Seleccionaste Leche";
		De Otro Modo:
			Escribir "Seleccionaste Otra cosa";
	FinSegun
	
FinProceso
