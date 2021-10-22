#Este es el menu para la práctica de 22-10-21
#Podremos calcular el año bisiesto y si un número es narcisista
from añosbisiestos import mbisiestos
from narcisista import *
from bisiesto import *
a=0
o=0
while(a==0):
    print(" ")
    print("Bienvenido al menu. Seleccione una opción:")
    print(" ")
    print("0.- Salir.")
    print("1.- Año bisiesto.")
    print("2.- Número narcisista.")
    print("3.- Introducir fecha de nacimiento.")
    print(" ")
    o=int(input())
    print(" ")
    if(o==0):
        print("Gracias por usar el programa.")
        a=1
    elif(o==1):
        bisiesto()
    elif(o==2):
        narcisistas()
    elif(o==3):
        mbisiestos()
    else:
        print("Error.")
