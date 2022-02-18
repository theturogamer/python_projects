from tkinter import * 
#creamos la raiz(la interfaz)
raiz= Tk()

#creamos el lienzo(va dentro de la interfaz)
lienzo=Frame()

#metemos el lienzo en la raiz
lienzo.pack()

#configuramos la raiz
raiz.title("titulo")
#raiz.geometry(tamaño) 
raiz.resizable(0,0)
#raiz.config(bg=color)
raiz.iconbitmap("imagenes\icono.ico")

#configuramos el lienzo
lienzo.config(bg="#20d090")
lienzo.config(width="600",height="420")

#creamos una etiqueta y delimitamos sus valores
etiqueta = Label(lienzo,text="calculadora",bg="#00b070").place(x=270,y=0)

global resultado
resultado=0
global numero1
numero1=0
global numero2
numero2=0
global operacion
operacion=0
global posicion
posicion=1
global posicion2
posicion2=1
l_numero1 = Label(lienzo,text=numero1,bg="#00b070").place(x=0,y=0)
l_numero2 = Label(lienzo,text=numero1,bg="#00b070").place(x=0,y=0)
l_posicion1= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)
l_posicion2= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

#creando las funciones de los botones
def igual():
    if operacion==1:
        resultado = numero1 + numero2

def suma():
    global operacion
    operacion=1

#def resta():

#def multi():

#def div():

#def delet():
    
def n1():
    global numero1
    global numero2
    global posicion
    global posicion2
    print(operacion)
    if operacion==0:
        numero1=numero1*10+1    
        posicion=posicion+1
        l_numero1 = Label(lienzo,text=numero1,bg="#00b070").place(x=0,y=0)
        l_posicion1= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)
    else:
        numero2=numero2*10+1
        posicion2=posicion2+1
        l_numero2 = Label(lienzo,text=numero2,bg="#00b070").place(x=0,y=50)
        l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)
'''
def n2():
    global resultado
    global posicion
    resultado=resultado*10+2   
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n3():
    global resultado
    global posicion
    resultado=resultado*10+3  
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n4():
    global resultado
    global posicion
    resultado=resultado*10+4    
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n5():
    global resultado
    global posicion
    resultado=resultado*10+5   
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n6():
    global resultado
    global posicion
    resultado=resultado*10+6    
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n7():
    global resultado
    global posicion
    resultado=resultado*10+7  
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n8():
    global resultado
    global posicion
    resultado=resultado*10+8    
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n9():
    global resultado
    global posicion
    resultado=resultado*10+9   
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)

def n0():
    global resultado
    global posicion
    resultado=resultado*10+0
    posicion=posicion+1
    l_igual = Label(lienzo,text=resultado,bg="#00b070").place(x=0,y=0)
    l_posicion= Label(lienzo,text=posicion,bg="#00b070").place(x=0,y=400)
'''
#creamos los botones
b_suma  = Button(lienzo,command=suma,text="suma",bg="#999999",width="11",height="2").place(x=500,y=245)
b_resta = Button(lienzo,text="resta",bg="#999999",width="11",height="2").place(x=500,y=285)
b_multi = Button(lienzo,text="multiplicación",bg="#999999",width="11",height="2").place(x=500,y=325)
b_div   = Button(lienzo,text="divición",bg="#999999",width="11",height="2").place(x=500,y=365)
b_n1    = Button(lienzo,command=n1,text="1",bg="#999999",width="5",height="2").place(x=360,y=245)
'''b_n2    = Button(lienzo,command=n2,text="2",bg="#999999",width="5",height="2").place(x=405,y=245)#2
b_n3    = Button(lienzo,command=n3,text="3",bg="#999999",width="5",height="2").place(x=450,y=245)
b_n4    = Button(lienzo,command=n4,text="4",bg="#999999",width="5",height="2").place(x=360,y=285)#4
b_n5    = Button(lienzo,command=n5,text="5",bg="#999999",width="5",height="2").place(x=405,y=285)
b_n6    = Button(lienzo,command=n6,text="6",bg="#999999",width="5",height="2").place(x=450,y=285)#6
b_n7    = Button(lienzo,command=n7,text="7",bg="#999999",width="5",height="2").place(x=360,y=325)
b_n8    = Button(lienzo,command=n8,text="8",bg="#999999",width="5",height="2").place(x=405,y=325)#8
b_n9    = Button(lienzo,command=n9,text="9",bg="#999999",width="5",height="2").place(x=450,y=325)
b_n0    = Button(lienzo,command=n0,text="0",bg="#999999",width="5",height="2").place(x=405,y=365)#0
b_c     = Button(lienzo,text="C",bg="#999999",width="5",height="2").place(x=360,y=365)
b_i     = Button(lienzo,command=igual,text="=",bg="#999999",width="5",height="2").place(x=450,y=365)
'''
#b_n0   = Button(lienzo,text="0",bg="#999999",width="5",height="2").place(x=405,y=365)

raiz.mainloop()
