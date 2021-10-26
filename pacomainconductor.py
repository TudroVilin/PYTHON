from pacocoche import Coche
from deportivo import Deportivo
print("Conduciendo mi coche.")
#Construimos nuestro coche
car=Coche()
print("Marca del coche:")
car.marca=input()
print("Modelo del coche:")
car.modelo=input()
supercar=Deportivo()
#Damos una marca al deportivo
supercar.marca="Ferrari"
supercar.modelo="F40"
opc=-1
while(opc!=0):
    print("MENU")
    print("0.- Salir.")
    print("1.- Arrancar.")
    print("2.- Acelerar.")
    print("3.- Frenar.")
    print("4.- Detener.")
    opc=int(input())
    if(opc==1):
        car.arrancar()
    elif(opc==2):
        car.acelerar()
        supercar.acelerar()
    elif(opc==3):
        car.frenar()
    elif(opc==4):
        car.detener()
    elif(opc==0):
        print("Hasta luego")
print("Fin de programa")
