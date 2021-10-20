# Realizar una aplicación que nos pedirá tres números.
# Mostraremos el número mayor, número menor y la suma de los tres.
print("Introduzca tres núemros:")
n1=int(input())
n2=int(input())
n3=int(input())
#s será la suma
s=n1+n2+n3
if(n1>n2 and n1>n3):
    if(n2>n3):
        print("Número mayor: "+str(n1)+" Número intermedio: "+str(n2)+" Número menor: "+str(n3))
        print("La suma es: "+str(s))
    elif(n2<n3):
        print("Número mayor: "+str(n1)+" Número intermedio: "+str(n3)+" Número menor: "+str(n2))
        print("La suma es: "+str(s))
    elif(n2==n3):
        print("Número mayor: "+str(n1)+" Números menores: "+str(n2)+" "+str(n3))
elif(n2>n1 and n2>n3):
    if(n1>n3):
        print("Número mayor: "+str(n2)+" Número intermedio: "+str(n1)+" Número menor: "+str(n3))
        print("La suma es: "+str(s))
    elif(n1<n3):
        print("Número mayor: "+str(n2)+" Número intermedio: "+str(n3)+" Número menor: "+str(n1))
        print("La suma es: "+str(s))
    elif(n1==n3):
        print("Número mayor: "+str(n2)+" Números menores: "+str(n1)+" "+str(n3))
elif(n3>n1 and n3>n2):
    if(n1>n2):
        print("Número mayor: "+str(n3)+" Número intermedio: "+str(n1)+" Número menor: "+str(n2))
        print("La suma es: "+str(s))
    elif(n1<n2):
        print("Número mayor: "+str(n3)+" Número intermedio: "+str(n2)+" Número menor: "+str(n1))
        print("La suma es: "+str(s))
    elif(n1==n2):
        print("Número mayor: "+str(n3)+" Números menores: "+str(n1)+" "+str(n2))
elif(n1==n2 and n2==n1 and n1==n3):
    print("Los tres números son iguales")
    print("La suma es: "+str(s))