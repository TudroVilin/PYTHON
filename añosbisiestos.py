def mbisiestos():
    from datetime import date
    print("Vamos a mostrar los años bisiestos desde su cumpleaños.")
    print("Introduzca el año de nacimiento con el siguiente formato dd/mm/aaaa o dd-mm-aaaa")
    a=0
    while(a==0):
        n=input()
        if(n.isdigit()==True):
            print(" ")
            print("El valor introducido no es una fecha. Vuelva a probar")
            print(" ")
        else:
            if(n.find("/")!=-1 or n.find("/")!=-1):
                print(" ")
                print("Fecha correcta, procesando.")
                print(" ")
            else:
                print(" ")
                print("La fecha introducida no cumple el formato especificado.")
                print(" ")
    #Si la fecha la introduce como 01/01/1990 o 01-01-1990
    #Tendremos que decirle al programa que coja el año
    #Primero vamos a sustituir el caracter / o - por cualquier otro
    if(n.find("/")!=-1):
        #Tenemos una barra, la sustituimos.
        a=n.replace("/","@")
    elif(n.find("-")!=-1):
        #Tenemos guones, los sustituimos.
        a=n.replace("-","@")
    else:
        print("Error")
    #Ya tenemos que buscar la última @ para coger el año
    ultarrb=a.rfind("@")
    #Con substring, decimos que queremos recuperar desde la última 
    #@ en adelante, ese será nuestro año.
    b=a[ultarrb+1:]
    #De esta manera ya tenemos el año
    print(str(b))
    f=date.today()
    f=f.year
    print(" ")
    print("Los años bisiestos son:")
    for i in range(int(b),f):
        if(i%4==0):
            if(i%100!=0 or i%400==0):
                print(" ")
                print("-"+str(i))