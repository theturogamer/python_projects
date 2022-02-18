import librerias as li

def preguntas():
	print("cuantas columnas y filas quieres?")
	columnas=int(input())
	filas= int(input())
	li.crear_matriz(columnas,filas,0)

n=1
while n==1:
	preguntas()
	n=int(input())

