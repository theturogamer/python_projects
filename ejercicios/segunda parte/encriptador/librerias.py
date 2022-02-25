import os 

def añadir_a_registro(nombre_del_registro,informacion_a_añadir):

	registro = open(nombre_del_registro, "a")

	dato = informacion_a_añadir[0]
	registro.write(str(dato))

	registro.write(",")

	dato = informacion_a_añadir[1]
	registro.write(str(dato))
	
	registro.write("\n")

	registro.close()

	registro = open(nombre_del_registro)
	print(registro.read())
	registro.close()


def leer_registro(nombre_del_registro):
	registro = open(nombre_del_registro)
	print(registro.read())
	registro.close()