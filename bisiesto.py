#Calculador años bisiestos
def bisiesto():
    print("Calculador años bisiestos.")
    print(" ")
    print("Introduzca un año:")
    a=int(input())
    if((a%4==0)):
        if(a%400==0 or a%100!=0):
            print("El año "+str(a)+(" es bisiesto."))
        else:
            print("El año no es bisiesto.")
            print(" ")
    else:
        print("El año no es bisiesto.")
    print(" ")

