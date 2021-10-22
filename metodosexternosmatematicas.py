def mostrarMenu():
    print("0.-Salir")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Dividir")
    print("4.-Multiplicar")
    print("Seleccione una opción:")
#Tendremos métodos que nos devolverán un valor con la ecuación que sea
def sumarNumeros(num1,num2):
    suma=num1+num2
    return suma
def restarNumeros(num1,num2):
    resta=num1-num2
    return resta
def sumarDividir(num1,num2):
    div=num1/num2
    return div
def multiplicarNumeros(num1,num2):
    mult=num1*num2
    return mult
def numero1():
    print("Introduzca el número 1:")
    n1=int(input())
    return n1
def numero2():
    print("Introduzca el número 2:")
    n2=int(input())
    return n2