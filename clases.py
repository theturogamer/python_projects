#creo la clase espada,con las propiedades tipo y daño
class Espada():
    def ho(x):
        print('hola, soy una espada de ')
    def tipo(x,mt):
        print (mt)
    def dmg(x,dam):
        print (dam)
#declaro la espada de piedra una espada
Swrd_cob = Espada()
#doy los parametros de una espada

def espada_de_piedra():
    Swrd_cob.ho()
    Swrd_cob.tipo('piedra')
    Swrd_cob.dmg('hago \n5pts de daño')

def espada_de_madera():
    Swrd_cob.ho()
    Swrd_cob.tipo('madera')
    Swrd_cob.dmg('hago \n3pts de daño')
salir = 1
while salir==1:
    print ("introduce 0 para piedra 1 para madera") 
    qs = int(input())

    if qs == 0:
        espada_de_piedra()
    elif qs == 1:
        espada_de_madera()
    else:
        print("numero no valido")
    print("inserta 0 para salir inserta 1 para continuar")
    salir = int(input())


