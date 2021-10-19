print("Introduzca el primer número:")
n1=int(input())
print("Introduzca el segundo valor:")
n2=int(input())
if(n1>n2):
    print(str(n1)+" es mayor que "+str(n2))
elif(n1==n2):
    print(str(n1)+" y "+str(n2)+" son iguales")
else:
    print(str(n2)+" es mayor que "+str(n1))
print("Fin de programa")