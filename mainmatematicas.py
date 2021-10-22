from metodosexternosmatematicas import *
#Programa principal
print("<----------------MATEMATICAS---------------->")
print(" ")
print("Ejemplo matemáticas con métodos.")
print(" ")
#En este ejemplo, todos los métodos necesitan dos números. Por lo que
#pediremos al iniciar.
a=0
b=0
c=0
n1=None
n2=None
print("Introduzca dos números:")
n1=numero1()
n2=numero2()
b=1
while(a==0):
    while(b==0):
        print("¿Desea mantener los mismos números? s/n")
        resp=input()
        if(resp=="s"):
            b=1
            c=0
        elif(resp=="n"):
            b=1
            c=0
            n1=numero1()
            n2=numero2()
        else:
            print("Error")
    while(c==0):
        mostrarMenu()
        opcion=int(input())
        if(opcion==1):
            resultado=sumarNumeros(n1,n2)
            print("La suma es: "+str(resultado))
            c=1
            b=0
        elif(opcion==2):
            resultado=restarNumeros(n1,n2)
            print("La resta es: "+str(resultado))
            c=1
            b=0
        elif(opcion==3):
            resultado=sumarDividir(n1,n2)
            print("La división es: "+str(resultado))
            c=1
            b=0
        elif(opcion==4):
            resultado=multiplicarNumeros(n1,n2)
            print("La multiplicacion es: "+str(resultado))
            c=1
            b=0
        elif(opcion==0):
            print("Gracias por usar el programa.")
            b=1
            a=1
            c=1
        else:
            print("Error")
print("Fin del programa")