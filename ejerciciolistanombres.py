from os import path
#ESTE ES EL MENÚ CON EL QUE EL USUARIO SELECCIONARÁ LA ELECCIÓN QUE
#REALIZARÁ EL PROGRAMA
def menuPrin():
    print("")
    print("-------------MENU-------------")
    print("0.- Salir")
    print("1.- Nuevo nombre")
    print("2.- Eliminar nombre (posición)")
    print("3.- Comenzar de nuevo")
    print("")
    #EL TRY ES POR SI EL USUARIO NO INTRODUCE UNA OPCIÓN VÁLIDA DEL
    #MENÚ.
    try:
        a=int(input())
    except ValueError:
        print("")
        print("Introduzca un valor de los mostrados en el menú.")
        menuPrin()
    return a
#ESTE ES EL MÓDULO QUE PERMITE AÑADIR NUEVOS NOMBRES A LA LISTA 
#PRINCIPAL, AÑADIÉNDOLOS AL FINAL DE LA MISMA HASTA QUE EL USUARIO
#INTRODUZCA OK
def nombre():
    r=0
    while(r==0):
        print("")
        print("Introduzca el nuevo nombre:")
        n=input()
        lista.append(n)
        if(n.isdigit()==True):
            print("")
            print("Lo introducido no es un nombre.")
            print("Pruebe de nuevo.")
            print("")
            nombre()
        elif(n.upper()=="OK"):
            r=1
            lista.remove("ok")
#ESTE ES EL MÓDULO QUE ELIMINA EL NOMBRE QUE SE LE DIGA ESPECIFICANDO
#SU POSICIÓN EN LA LISTA.
def eliminanombre():
    print("")
    print("Introduzca el nombre que desea eliminar especificando su posición")
    print("")
    try:
        p=int(input())
    except ValueError:
        print("")
        print("Lo introducido no es un número, pruebe de nuevo.")
        eliminanombre
    return p
#ESTE ES EL MÓDULO QUE SIRVE PARA MOSTRAR LA LISTA DE NOMBRES INTRODUCIDOS
#Y QUE INDICA ADEMÁS EL NÚMERO DE LA LISTA ASOCIADO CON EL NOMBRE
#LO QUE AYUDARÁ AL USUARIO A ELIMINAR LOS NOMBRES QUE DESEE
def mostrarlista():
    l=len(lista)
    i=0
    for i in range(l):
        name=lista[i]
        print(str(i)+".- "+name)
        print("")
#PROGRAMA PRINCIPAL
lista=[]
a=0
while(a==0):
    opc=menuPrin()
    if(opc==1):
        print("")
        nombre()
        print("")
        mostrarlista()
        opc=-1
    elif(opc==2):
        p=eliminanombre()
        try:
            lista.pop(p)
        except:
            print("")
            print("Se ha introducido un valor no válido.")
        print("")
        print("Lista:")
        print("")
        if(lista==[]):
            print("VACIA")
        else:
            mostrarlista()
        opc=-1
    elif(opc==3):
        print("")
        print("Eliminando la lista actual:")
        mostrarlista()
        print("")
        lista.clear()
        if(lista==[]):
            print("Lista:")
            print("")
            print("VACIA")
            print("")
        opc=-1
    elif(opc==0):
        print("Fin del programa.")
        a=1
print("")
print("RTV")