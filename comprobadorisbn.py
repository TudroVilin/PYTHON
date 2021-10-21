print("Comprobador números ISBN")
print("Introduzca el número:")
n=input()
if(n.isdigit()!=True):
    print("Lo introducido NO es número")
elif(len(n)<10 or len(n)>10):
    print("El número no es correcto")
else:
    l=len(n)
    suma=0
    for i in range(l):
        p=n[i]
        p=int(p)
        suma=suma+(p*(i+1))
    if(suma%11==0):
        print("El ISBN es correcto")
    else:
        print("El ISBN es incorrecto")
print("Fin de programa")