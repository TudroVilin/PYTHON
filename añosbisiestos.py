#Mostrador de años bisiestos
from bisiesto import bisiesto


def mbisiestos():
    from datetime import date
    print("Vamos a mostrar los años bisiestos desde su cumpleaños.")
    print("Introduzca el año de nacimiento:")
    n=int(input())
    f=date.today()
    f=f.year
    print(" ")
    print("Los años bisiestos son:")
    for i in range(n,f):
        if(i%4==0):
            if(i%100!=0 or i%400==0):
                print(" ")
                print("-"+str(i))
        