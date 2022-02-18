def cambiar_orden(array):
	cantidad = 0
	for x in array:
		cantidad += 1
	array_i = []
	cant = cantidad
	for y in range(cantidad):
		cant = cant - 1
		array_i.append(array[cant])
	return (array_i)


inicial_loop = 1
while inicial_loop==1:

	print("cuantos numeros deseas insertar?")

	cantidad_numeros = int(input())
	array = []
	print("inserta los numeros: ")
	for x in range(cantidad_numeros):
		array.append(int(input()))

	print(array)
	print(cambiar_orden(array))
	print("inserta 1 para continuar")
	inicial_loop = int(input())