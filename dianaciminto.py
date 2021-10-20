from math import trunc
d1=None
d2=None
d3=None
print("Ejercicio Día nacimiento")
print("Introduzca el día de su nacimiento:")
d=int(input())
print("Introduzca el mes de su nacimiento:")
m=int(input())
print("Introduzca el año de su nacimiento:")
a=int(input())
if(m==1):
    m=13
    a-=1
elif(m==2):
    m=14
    a+=1
d2=trunc((d+(m*2)+a+((m+1)*3/5)+(a/4)-(a/100)+(a/400)+2))
d3=trunc(d2/7)
d1=d2-(d3*7)
if(d1==1):
    print("Domingo")
elif(d1==2):
    print("Lunes")
elif(d1==3):
    print("Martes")
elif(d1==4):
    print("Miércoles")
elif(d1==5):
    print("Jueves")
elif(d1==6):
    print("Viernes")
elif(d1==0):
    print("Sábado")
else:
    print("ERROR")
print("Fin programa")
