#librerias

def sumar_matriz(ancho,alto,matriz1,matriz2,proceso1):
	matriz3 = []
	array=[]

	for fila in range(ancho):
		for columna in range(alto):
			suma = list_int(matriz1[fila][columna]) + list_int(matriz2[fila][columna])
			if proceso1==1:
				print( str(fila) + "\n" + str(columna) + "\n" + str(suma) + "\n\n\n\n")
			array.append(suma)
			if (columna + 1) == alto :
				matriz3.append(array)
				array = []
				print(matriz3)

	if proceso1==1:
		print (matriz1)
		print (matriz2)
		imprim_matr(ancho,alto,matriz3)
	return(matriz3)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def crear_matriz(columnas,filas,mostrar_proceso1):
	def add0(n):
		if n < 10:
			n = str(n)
			x = "00" + n
			return(x)
		elif n < 100:
			n = str(n)
			x = "0" + n
			return(x)

	def li0int(matriz):#[1]  #[11]
		aux=[]
		n=0
		intmatriz = 0
		smatriz=str(matriz)#"[1]" #"[11]"
		for x in (smatriz):#[,1,] #[,1,1,] 
			aux.append(x)
			n = n + 1
		for x in range(n-2):
			x = x + 1
			intmatriz=intmatriz * 10 + int(aux[x])
		return(intmatriz)

	import random as random
	array=[]
	matriz=[]
	for a in range(filas):
		for b in range(columnas):
			aux = random.randint(0,(filas*columnas))
			if mostrar_proceso1==1:
				print("\ninserte el numero en la pocicion numero [" + str(a) + "][" + str(b) + "] : " + str(aux))
			array.append([aux])
		matriz.append(array)
		array = []
	if mostrar_proceso1 == 1:
		for a in range(filas):
			print("\n\n", end="")
			for b in range(columnas):
				#print(li0int((matriz[a][b])))
				if (li0int((matriz[a][b]))) < 100:
					print(add0(li0int(matriz[a][b])), end= "   ")
				elif (li0int((matriz[a][b]))) < 10:
					print(add0(li0int(matriz[a][b])), end= "   ")
				else:
					print(li0int(matriz[a][b]), end= "   ")
	return(matriz)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def list_int(matriz):#[1]  #[11]
	aux=[]
	n=0
	intmatriz = 0
	smatriz=str(matriz)#"[1]" #"[11]"
	for x in (smatriz):#[,1,] #[,1,1,] 
		aux.append(x)
		n = n + 1
	for x in range(n-2):
		x = x + 1
		intmatriz=intmatriz * 10 + int(aux[x])
	return(intmatriz)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def imprim_matr(orizontal,vertical,matriz):
	for fila in range(orizontal): 
		print(" ")
		for columna in range(vertical):
			print(matriz[fila][columna], end=" ")
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def intrducir_matriz(columnas,filas):
	mostrar_proceso1=1
	def add0(n):
		if n < 10:
			n = str(n)
			x = "00" + n
			return(x)
		elif n < 100:
			n = str(n)
			x = "0" + n
			return(x)

	def li0int(matriz):#[1]  #[11]
		aux=[]
		n=0
		intmatriz = 0
		smatriz=str(matriz)#"[1]" #"[11]"
		for x in (smatriz):#[,1,] #[,1,1,] 
			aux.append(x)
			n = n + 1
		for x in range(n-2):
			x = x + 1
			intmatriz=intmatriz * 10 + int(aux[x])
		return(intmatriz)

	array=[]
	matriz=[]
	for a in range(filas):
		for b in range(columnas):
			print("\ninserte el numero en la pocicion numero [" + str(a) + "][" + str(b) + "] : ",end="")
			aux = int(input())
			array.append([aux])
		matriz.append(array)
		array = []
	if mostrar_proceso1 == 1:
		for a in range(filas):
			print("\n\n", end="")
			for b in range(columnas):
				#print(li0int((matriz[a][b])))
				if (li0int((matriz[a][b]))) < 100:
					print(add0(li0int(matriz[a][b])), end= "   ")
				elif (li0int((matriz[a][b]))) < 10:
					print(add0(li0int(matriz[a][b])), end= "   ")
				else:
					print(li0int(matriz[a][b]), end= "   ")
	return(matriz)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def formato_matriz(ancho,alto,matriz):
	def add0(n):
		if n < 10:
			n = str(n)
			x = "00" + n
			return(x)
		elif n < 100:
			n = str(n)
			x = "0" + n
			return(x)

	def li0int(matriz):#[1]  #[11]
		aux=[]
		n=0
		intmatriz = 0
		smatriz=str(matriz)#"[1]" #"[11]"
		for x in (smatriz):#[,1,] #[,1,1,] 
			aux.append(x)
			n = n + 1
		for x in range(n-2):
			x = x + 1
			intmatriz=intmatriz * 10 + int(aux[x])
		return(intmatriz)

	for a in range(ancho):
		print("\n\n", end="")
		for b in range(alto):
			if ((li0int(matriz[a][b]))) < 100:
				print(add0(li0int(matriz[a][b])), end= "   ")
			else:
				print(li0int(matriz[a][b]), end= "   ")
