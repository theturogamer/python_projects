from matplotlib import pyplot as plt
re=1
while re==1:
    print("\ncuanto es tu capital inicial?")
    ya=int(input())
    print("\nde cuantos dias sera tu inversion?")
    i=int (input () )
    i = (i+1)
    xm=[0]
    ym=[ya]
    xa=(0)
    print ("\nescribe tu porcentaje de intereses diarios")
    ad= float (input ())
    ad= ((ad/100) + 1)
    print ("\ndeseas ver el registro? (1=si 0 = no)")
    r=int (input ())
    while i>1 :
        xm.append (xa + 1)
        xa = (xa + 1)
        ym.append (ya * ad)
        ya = (ya * ad)
        i=(i-1)
        if r==1:
            
            print (xa)
            print (ya)
            
    print("\ndeseas una interacion mas? 1=si 0=no")
    re=int(input())

    plt.ion()
    plt.plot(xm,ym)

print("enter para ver resultados")
input()

plt.ion()
plt.plot(xm,ym)

