print("Número incial: ")
n1=int(input())
print("Número final: ")
n2=int(input())
#Realizamos el bucle por rango
for i in range(n1,n2+1):
    #Preguntamos si el número es par
    if(i%2==0):
        #Tenemos número par
        print(i)
print("Fin del programa")