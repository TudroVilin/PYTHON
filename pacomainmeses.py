from pacomeses import Mes
import random
print("Manejando clases Mes.")
print("")
nombresmes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#Necesitamos crear 12 meses
meses=[]
#Quiero que cada mes ponga Mes 1, Mes 2...
for i in range (0,12):
    mimes=Mes()
    mimes.nombre=nombresmes[i]
    mimes.max=random.randint(1,40)
    mimes.min=random.randint(-40,0)
    mimes.getMedia
    meses.append(mimes)
    print(i)
print("Meses creados "+str(len(meses)))
#Recorremos todos los meses y vemos su contenido
for mes in meses:
    print(mes)
print("Fin de programa")