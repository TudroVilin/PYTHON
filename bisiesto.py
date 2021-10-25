#Calculador años bisiestos
def bisiesto():
    print("Calculador años bisiestos.")
    print(" ")
    print("Introduzca un año con el siguiente formato aaaa")
    b=0
    while(b==0):
        a=int(input())
        if(a.isdigit()==True):
            b=1
        else:
            print(" ")
            print("Lo introducido no es un año con un formato válido.")
            print(" ")
    if((a%4==0)):
        if(a%400==0 or a%100!=0):
            print("El año "+str(a)+(" es bisiesto."))
        else:
            print("El año no es bisiesto.")
            print(" ")
    else:
        print("El año no es bisiesto.")
    print(" ")