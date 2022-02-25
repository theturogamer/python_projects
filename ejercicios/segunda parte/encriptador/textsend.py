#Programa para enviar mensajes V 0.1.0
import librerias as lib
import sys

loop = 1
while loop == 1:
	
	#bienvenida*
	print( "\n\n\n\n\n--::Bienvenido al programa::--\n¿que decesa hacer?" )
	print( "\n\n(1) --  ver chats\n\n(2) --  nuevo chat\n\n(3) --  eliminar chats\n\n" )
	
	#seleccion de opciones*
	opcion = int(input())

	#operacion de opciones*
	if opcion == 1:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		
		#mostrar registro con chats
		lib.leer_registro("chats.csv")

	elif opcion == 2:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		
		#ingresar nuevo chat
		
		N_chat = []
		nombre = ""
		numero = 0

		print( "introduce los datos que deceas agregar:_ \n\n-- nombre del chat:  ")
		nombre = input()

		print( "\n\n--numero telefonico:  ")
		numero = int(input())

		N_chat.append(nombre)
		N_chat.append(numero)

		lib.añadir_a_registro("chats.csv",N_chat)

		N_chat = ""

	elif opcion == 3:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

	else:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print( "\n\n -/-/-/- seleccione una opcion valida ----" )



	print("n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print( "para salir, seleccione 0; para seguir, seleccione 1; ")
	loop = int(input())
sys.exit(0)
