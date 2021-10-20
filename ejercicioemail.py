# Necesitamos un programa para validar un email.
# El programa me dirá si el email está bien o tiene algún fallo.
# Me dirá el fallo que tiene.
# A comprobar:
# - Que el mail tenga @
# - Que el mail no comience ni finalice con @
# - Que el mail solo tenga una @
# - Que tengamos solo un punto
# - Un punto después de la @
# - Y que el dominio (.com) tenga de 2 a 4 caracteres
print("Comprobador de direcciones email")
print("Introduzca el email que desee:")
print(" ")
#La variable a comprobará que sea texto, no números
a=input()
#Primero vamos a comprobar toda la casuística de la arroba
if(a.find("@")!=-1):
    if(a.startswith("@")!=False):
        print("El correo empieza por @.")
    elif(a.endswith("@")!=False):
        print("El correo termina con @.")
    # b será el contador de @
    else:
        b=a.find("@")
        if(a.find("@",b+1)!=-1):
            print("El correo contiene dos @.")
        else:
             # Ahora, seguiremos con el punto, buscandolo después de la @
            p=a.find(".")
            if(a.find(".",b+1)==-1):
                print("El correo no contiene punto.")
            elif(a.find(".",p+1)!=-1):
                print("El correo contiene dos puntos.")
            #Ahora tocará comprobar el dominio
            else:
                d=a[p+1:]
                dd=len(d)
                if((dd>4 or dd<2)):
                    print("El dominio es incorrecto.")
                else:
                    print("El correo es correcto.")
else:
    print("El correo no contiene @.")
print(" ")
print("Fin del programa.")