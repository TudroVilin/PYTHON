def divNum():
    try:
        #CODIGO QUE PODRÍA DAR UNA EXCEPCIÓN
        print("Introduzca un número 1:")
        n1=int(input())
        print("Introduzca un número 2:")
        n2=int(input())
        print("El doble es: "+str(n1/n2))
    except ValueError:
        print("Error, debes introducir un número.")
        divNum()
    except ZeroDivisionError:
        print("No puedes dividir entre 0.")
        divNum()
    except:
        print("Error general.")
    finally:
        print("Siempre entro en ejecución.")

print("Programa principal control de errores.")
#Podemos poner el control de errores en el programa principal
#por si algún método de los que llamamos da excepción
divNum()