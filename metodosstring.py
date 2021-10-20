print("Ejemplo con métodos de String")
texto="primer python";
#En este ejemplo, solamente vamos a ir escribiendo los métodos y viendo
#qué devuelven.
print("Texto: "+texto)
print("Mayusculas: "+texto.upper())
print("Replace o por @: "+texto.replace("o","@"))
print("Primera letra: "+texto[0])
#A len() hay que ponerlo como str() porque nos devolvería un valor
#numérico entero.
print("Longitud del texto: "+str(len(texto)))
#Si el .find nos devuelve -1 significa que no lo ha encontrado y
#0 si sí lo ha encontrado. Es KEYSENSITIVE.
print("Buscar la letra P: "+str(texto.find("P")))
print("Buscar la letra P: "+str(texto.find("p")))
#Buscará a partir de la siguiente posición a 0 hasta encontrar la
#letra que le hayamos puesto.
print("Buscar la siguiente letra p: "+str(texto.find("p",1)))
#La siguiente variable es posición.
p=texto.find("p")
#Buscamos la letra p a partir de la posición inicial.
print("Buscar la siguiente letra p: "+str(texto.find("p",p+1)))
#Las posiciones no cambian, da igual cómo busquemos o lo que hagamos
#Podemos buscar desde el final de la cadena
print("Letra p desde el final: "+str(texto.rfind("p")))
print("Texto inciando con A: "+str(texto.startswith("A")))
print("Texto finalizando con n: "+str(texto.endswith("n")))
print("Texto de números: "+str(texto.isdigit()))
print("Texto de letras: "+str(texto.isalpha()))
#Vamos a ver SLICING o SUBSTRING
#Subcadena va a ser la variable sc
#Queremos la cadena desde la posición 2 en adelante:
sc=texto[2:]
print("Posición 2 en adelante: "+sc)
#También podemos decirle que queremos desde una posición a otra:
sc2=texto[2:5]
print("Posición 2 a la 5: "+sc2)
#Tenemos la posibilidad (conocemos FOR) de reccorer todos los
#caracteres del texto uno a uno.
#Variable longitud = l
l=len(texto)
for i in range(l):
    #Capturamos cada letra con la variable ll
    ll=texto[i]
    print(str(i)+" : "+ll)
print("Fin del programa")
#Averiguar si es un número lo que nos ha dado el usuario
print("Introduzca un número:")
#El truco es almacenar el valor en un String
#Preguntar con isdigit() si es un número y ya hacer lo que queramos
aux=input()
if(aux.isdigit()):
    print("Es un número")
else:
    print("No es un número")
print("Fin del programa")

