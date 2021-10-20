#Conjetura de Collatz
print("Introduzca un número: ")
n=int(input())
while n!=1:
    if(n%2==0):
        #El int en la división es para que sea entero
        n=int(n/2)
        print(n)
    else:
        n=(n*3)+1
        print(n)
print("Fin programa")