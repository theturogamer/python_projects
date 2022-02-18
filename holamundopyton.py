salir = 0
print ("CALCULADORA")
while salir == 0:
    print ("esctibe un numero")
    numero_1 = int (input ())
    print ("escribe otro numero")
    numero_2 = int (input ())
    print ("escribe un operador aritmetico")
    print ("1=suma, 2=resta, 3=multiplicacion, 4=divicion")
    operador = int (input ())
    if   operador == 1:
        resultado = numero_1 + numero_2
    elif operador == 2:
        resultado = numero_1 - numero_2
    elif operador == 3:
        resultado = numero_1 * numero_2
    else:
        resultado = numero_1 / numero_2
    Resultado = str (resultado)
    print ("este es el resultado: " + Resultado)
    print ()
    print ("desea seguir utilizando?")
    print ("0=si, 1=no")
    salir = int (input ())

print ("gracias")
