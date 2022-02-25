inicial_loop = 1
while inicial_loop==1:
	print("cuantos numeros quieres introducir?")
	cantidad_n=int(input())
	array_1 = []
	print("inserta los numeros uno por uno")
	for x in range(cantidad_n):
		array_1.append(int(input()))
		
	final = 1
	for i in array_1:
		final = final * i
	print(final)
	print("inserta 1 para continuar")
	inicial_loop = int(input())
