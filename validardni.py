from math import trunc
print("Ejemplo validar DNI String")
print("Introduzca su número de DNI")
#Vamos a comprobar si es un número de verdad o no.
aux=input()
if(aux.isdigit()==False):
    #Si no es un número
    print("Debe introducir NUMEROS SOLAMENTE")
else:
    #Vamos a relizar el cálculo para el DNI
    #( nº DNI - (Entero(nº DNI / 23) * 23))
    dni=int(aux)
    dni=dni-(trunc(dni/23)*23)
    print(dni)
    #Si tuviéramos una "forma" de tener la tabla aquí bastaría con 
    #recuperar la posición 14...
    tabladni="TRWAGMYFPDXBNJZSQVHLCKET"
    letra=tabladni[dni]
    print("Su letra es: "+letra)
print("Fin de programa")