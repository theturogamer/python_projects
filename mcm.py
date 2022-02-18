print ('selecciona entre 1 y 5 numeros')
print ('1-5')
verificacion = 0

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0

while (verificacion == 0):
    verificacion = 1

    cant_num = int(input())

    if (cant_num <= 0):
        print ('elija un numero mas grande')
        verificacion = 0
    
    if (cant_num >= 6):
        print ('elige un numero mas pequeño')
        verificacion = 0

#con lo anterior confirmamos que el numero entra en los estandares de el programa

if (cant_num > 0):
    print('escoge tu primer numero:')
    num_1 = int(input())
    if (cant_num > 1):
        print ('escuge tu segundo numero ')
        num_2 = int(input())
        if (cant_num > 2):
            print ('escoge tu tercer numero')
            num_3 = int(input())
            if (cant_num > 3):
                print ('escoge tu cuarto numero')
                num_4 = int(input())
                if (cant_num > 4):
                    print ('escoge tu quinto numero')
                    num_5 = int(input())

#con lo anterior damos valor a cada uno de los numeros que utilisaremos
array = [2,3,5,7,11,13,17,19]
resultado = 0 
primo = 0
mcda = 0
mmcd = 0
mcd=1
while (resultado == 0):

    if (cant_num > 0):
        aux = num_1 % array[primo]
        mmcd = mmcd + 1
        if (aux == 0):
            mcda ++i
            
    if (cant_num > 1):
        mmcd ++i
        aux = num_1 % array[primo]
        if (aux == 0):
            mcda ++i

    if (cant_num > 2):
        mmcd ++i
        aux = num_1 % array[primo]
        if (aux == 0):
            mcda ++i

    if (cant_num > 3):
        mmcd ++i
        aux = num_1 % array[primo]
        if (aux == 0):
            mcda ++i

    if (cant_num > 4):
        aux = num_1 % array[primo]
        mmcd ++i
        if (aux == 0):
            mcda ++i

    if (mmcd == mcda):
        mcd = mcd * array[primo]
print(mcd)
print(mcda)
print(mmcd)
exit()



















