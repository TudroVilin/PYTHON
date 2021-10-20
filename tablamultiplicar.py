#Tabla de multiplicar
print("Introduzca un número para saber su tabla de multiplicar: ")
n=int(input())
for i in range(0,11):
    print(str(n)+" * "+str(i)+(" = ")+str(n*i))
print("Fin programa")