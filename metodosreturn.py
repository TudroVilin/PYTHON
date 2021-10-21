def convertirTexto(texto):
    #Devolvemos el texto en mayusculas
    return texto.upper()
def sumarNumeros(num1,num2):
    suma=num1+num2
    return suma
#Programa principal
print("Métodos return")
#Aquí enviamos un texto en minúsculas
#Debemos tener una variable para almacenar el valor devuelto por el
#método
valor=convertirTexto("soy un texto en minúsculas")
print(valor)
print("Introduzca dos números")
n1=int(input())
n2=int(input())
resultado=sumarNumeros(n1,n2)
print("La suma es :"+str(resultado))
print("Fin del programa")