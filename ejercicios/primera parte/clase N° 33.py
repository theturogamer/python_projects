inicial_loop = 1
while inicial_loop==1:

	print("cuantos numeros deseas insertar?")

	cantidad_numeros = int(input())
	array = []
	
	print("inserta los numeros: ")
	
	for x in range(cantidad_numeros):
		array.append(int(input()))	
	#inserto cada uno de los numeros segun la cantidad decidida con anterioridad


	array_2 = []
	cantidada = []
	cantidad = 0
	
	for z in array:
		cantidad += 1
		cantidada.append(cantidad)
	
	for y in cantidada:
		array_2.append(int(array[(y-1)])*2)
	print(array_2)
	print("inserta 1 para continuar")
	inicial_loop = int(input())
