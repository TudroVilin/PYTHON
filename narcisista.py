#Calculador de números narcisistas
def narcisistas():
    a=0
    print("Calculador números narcisistas.")
    print(" ")
    while(a==0):
        print("Introduzca un número:")
        n=input()
        if(n.isdigit()==False):
            print(" ")
            print("Lo introducido no es un número. Vuelva a probar.")
            print(" ")
        else:
            a=1
    l=len(n)
    s=0
    for i in range(l):
        c=n[i]
        c=int(c)
        s=s+(c**l)
        print(str(c)+"^"+str(l)+" = "+str(s))
    if(s==int(n)):
        print("El número es narcisista.")
        print(" ")
    else:
        print("El número no es narcisista.")
        print(" ")