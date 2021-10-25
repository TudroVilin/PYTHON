ciudades=[]
def mostrarCiudades():
    for c in ciudades:
        print(c)

#Tendremos un método para cargar las ciudades desde un archivo
def leerFile():
    #Primero debemos leer del fichero
    try:
        fichero=open("Ciudades.txt","r")
        #Leemos el contenido
        contenido=fichero.read()
        fichero.close()
        #Tenemos que convertir el string en list para que el programa
        #funcione.
        global ciudades #Esto sirve para decirle que la variable no es
        #nueva, sino que es la misma de antes.
        ciudades=contenido.split(sep="$")
    except FileNotFoundError:
        print("¡No hay datos a cargar!")
        guardarFile()


#Tendremos un método para guardar todas las ciudades en fichero
def guardarFile():
    #Convertimos la lista a string para el file
    respuesta="$".join(ciudades)
    fichero=open("Ciudades.txt","w+")
    fichero.write(respuesta)
    fichero.flush()
    fichero.close()
    print("Datos almacenados.")
#Tendremos otro método que insertará ciudades en la colección.
# El usuaria elegirá cuando guardarlo, leerlo o sobreescribirlo. 
def insertarCiudad():
    print("Introduzca una ciudad:")
    ciudad=input()
    ciudades.append(ciudad)

def mostrarMenu():
    print("0.- Salir")
    print("1.- Leer ciudades File.")
    print("2.- Guardar ciudades File.")
    print("3.- Nueva ciudad.")
    print("4.- Mostrar ciudades.")
    print("Seleccione una opción.")

print("Ejemplo con Files y listas")
opcion=-1
while(opcion!=0):
    mostrarMenu()
    opcion=int(input())
    if(opcion==1):
        leerFile()
    elif(opcion==2):
        guardarFile()
    elif(opcion==3):
        insertarCiudad()
    elif(opcion==4):
        mostrarCiudades()
    elif(opcion==0):
        print("Hasta luego cabeza.")
    else:
        print("Opción incorrecta")

print("Fin de programa")