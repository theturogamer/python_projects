from tkinter import * 
#creamos la raiz(la interfaz)
raiz= Tk()

#creamos el lienzo(va dentro de la interfaz)
lienzo=Frame()

#metemos el lienzo en la raiz
lienzo.pack()

#configuramos la raiz

raiz.title("MCM y MCD")
#raiz.geometry(tamaño) 
raiz.resizable(0,0)
#raiz.config(bg=color)

#configuramos el lienzo
lienzo.config(bg="#5090f0")
lienzo.config(width="600",height="420")

etiqueta = Label(lienzo,text="INSERTA TUS DIGITOS",bg="#3070d0").place(x=30,y=20)

def insert():
    strnum1 = str(numero_1.get())
    if strnum1 == "":
        num1 = 0
    else:
        num1 = (int(strnum1))
    numero_1.set("")
    
    strnum2 = str(numero_2.get())
    if strnum2 == "":
        num2 = 0
    else:
        num2 = (int(strnum2))
    numero_2.set("")
    
    strnum3 = str(numero_3.get())
    if strnum3 == "":
        num3 = 0
    else:
        num3 = (int(strnum3))
    numero_3.set("")
    
    strnum4 = str(numero_4.get())
    if strnum4 == "":
        num4 = 0
    else:
        num4 = (int(strnum4))
    numero_4.set("")
    
    strnum5 = str(numero_5.get())
    if strnum5 == "":
        num5 = 0
    else:
        num5 = (int(strnum5))
    numero_5.set("")
    
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num5)
    print("")

        array=[num1]

        if num1 > num2:
            add 2 en el 2
            if num2 > num3:
                add 3 en el 3
                if num3 > num4:
                    add 4 en el 4
                    if num4 > num5:
                        add 5 en el 5
                    else:
                        add 5 en el 4
                else:
                    add 4 en el 3
                    if num3 > num5:
                        add 5 en el 5
                    else:
                        add 5 en el 4
            else:
                add 3 en el 2
                        
                        
        else:
            add 2 en el 1
            if num3 > num4:
                add 4 en el 4
                if num

# 5,4,5,3,2
# 5,5,4,

    cant_num = 0
    
    if num1 > 0:
        cant_num = cant_num +1
    if num2 > 0:
        cant_num = cant_num +1
    if num3 > 0:
        cant_num = cant_num +1
    if num4 > 0:
        cant_num = cant_num +1
    if num5 > 0:
        cant_num = cant_num +1

    print(cant_num)
    print("")
    print("")
    if cant_num > 0:
        divisoria1 = Label(lienzo,text=".   "+strnum1+"   .",bg="#3070d0").place(x=360,y=40)
        divisoria1_1 = Label(lienzo,text="------",bg="#3070d0").place(x=360,y=55)
    if cant_num > 1:
        divisoria2 = Label(lienzo,text=".   "+strnum2+"   .",bg="#3070d0").place(x=390,y=40)
        divisoria2_1 = Label(lienzo,text="------",bg="#3070d0").place(x=390,y=55)
    if cant_num > 2:
        divisoria3 = Label(lienzo,text=".   "+strnum3+"   .",bg="#3070d0").place(x=420,y=40)
        divisoria3_1 = Label(lienzo,text="------",bg="#3070d0").place(x=420,y=55)
    if cant_num > 3:
        divisoria4 = Label(lienzo,text=".   "+strnum4+"   .",bg="#3070d0").place(x=450,y=40)
        divisoria4_1 = Label(lienzo,text="------",bg="#3070d0").place(x=450,y=55)
    if cant_num > 4:
        divisoria5 = Label(lienzo,text=".   "+strnum5+"   .",bg="#3070d0").place(x=480,y=40)
        divisoria5_1 = Label(lienzo,text="------",bg="#3070d0").place(x=480,y=55)

    parar = 1
    while parar == 1:
        a=360

        if cant_num > 0:
            divisoria1_1 = Label(lienzo,text="------",bg="#3070d0").place(x=a,y=80)
            a = a+30

        if cant_num > 1:
            divisoria2_1 = Label(lienzo,text="------",bg="#3070d0").place(x=a,y=80)
            a = a+30

        if cant_num > 2:
            divisoria3_1 = Label(lienzo,text="------",bg="#3070d0").place(x=a,y=80)
            a = a+30

        if cant_num > 3:
            divisoria4_1 = Label(lienzo,text="------",bg="#3070d0").place(x=a,y=80)
            a = a+30
            
        if cant_num > 4:
            divisoria5_1 = Label(lienzo,text="------",bg="#3070d0").place(x=a,y=80)
            a = a+30
        parar = 0
    
numero_1 = StringVar()
numero_2 = StringVar()
numero_3 = StringVar()
numero_4 = StringVar()
numero_5 = StringVar()


ENTRADA_NUMERO_1 = Entry(lienzo,textvariable=numero_1, width="40").place(x=30,y=40)
ENTRADA_NUMERO_2 = Entry(lienzo,textvariable=numero_2, width="40").place(x=30,y=60)
ENTRADA_NUMERO_3 = Entry(lienzo,textvariable=numero_3, width="40").place(x=30,y=80)
ENTRADA_NUMERO_4 = Entry(lienzo,textvariable=numero_4, width="40").place(x=30,y=100)
ENTRADA_NUMERO_5 = Entry(lienzo,textvariable=numero_5,width="40").place(x=30,y=120)

INTRODUCIR_BOTON = Button(lienzo,command=insert,text="INSERTAR",bg="#3070d0",width="9",height="1").place(x=30,y=200)


raiz.mainloop()

exit()
