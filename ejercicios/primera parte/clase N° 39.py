import librerias as li
print("\nAntes de iniciar el programa... ¿Desea ver el registro de los procesos? (0=no,1=si)")
proceso1 = int(input())
ret=1
while ret==1:

	print("\nBienvenido:\n¿Cual es el tamaño de las matrices que deseas sumar?...\n    -el tamaño de mis matrices es de (ancho,alto) :  ",end=" ")
	ancho=int(input())
	print("                                                      " , end="")
	alto= int(input())
	print("¡¡Perfecto!!, ahora inserte sus matrices.\nSi lo decea, puede utilizar matrices aleatorias\n\n-¿¿Usar matrices aleatorias??-   (0=no,1=si)\n\n")
	aleatorias = int(input())
	if aleatorias==1:
		matriz1 = li.crear_matriz(ancho,alto,proceso1)
		matriz2 = li.crear_matriz(ancho,alto,proceso1)
	else:
		print("Introduzca sus matrices dando *INTRO* tras cada numero")
		matriz1 = li.intrducir_matriz(ancho,alto)
		matriz2 = li.intrducir_matriz(ancho,alto)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("\n\n\n\n\n\n\nMatriz numero 1: \n\n\n")
	li.imprim_matr(ancho,alto,matriz1)
	print("\n\n\n\n\n\n\nMatriz numero 2: \n\n\n")
	li.imprim_matr(ancho,alto,matriz2)
	print("\n\n\n\n\n\n\nSuma de las matrices: \n\n\n")
	li.imprim_matr(ancho,alto,li.sumar_matriz(ancho,alto,matriz1,matriz2,0))

	ret=int(input())
