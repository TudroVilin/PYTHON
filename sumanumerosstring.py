print("Ejemplo sumando números de String")
print("Introzuca un valor numérico")
suma=0
n=input()
#Necesitamos acceder caracter a caracter a cada número del String
#Hay que recorrer toda la cadena de String
longitud=len(n)
for i in range(longitud):
    #Recuperamos cada caracter en la cadena
    caracter=n[i]
    #Convertimos cada caracter a int
    caracter=int(caracter)
    #Realizamos la suma
    suma=suma+caracter
    #La suma hay que dibujarla fuera del bucle.
print("La suma es: "+str(suma))
print(" ")
print("Fin de programa")