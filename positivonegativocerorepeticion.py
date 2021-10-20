#Pide números y dice si son positivos, negativos o cero hasta que le
#digamos que queremos parar
i=None
sn=None
while(i==None):
    sn=None
    print("Introduzca un número:")
    n=int(input())
    if(n>0):
        print(" ")
        print("El número: "+str(n)+" es positivo")
    elif(n<0):
        print(" ")
        print("El número: "+str(n)+" es negativo")
    else:
        print(" ")
        print("El número: "+str(n)+" es cero")
    print("")
    while(sn==None):
        print("¿Desea continuar?(s/n)")
        sn=str(input())
        if(sn=="s"):
            print(" ")
            sn=1
        elif(sn=="n"):
            print("Gracias por usar el programa.")
            sn=1
            i=1
        else:
            print("Error, repita su respuesta")
            print(" ")
            sn=None
print("Fin del programa")