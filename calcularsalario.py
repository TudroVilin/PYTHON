print("Calcular salario trabajadores")
print("Introduzca número de horas trabajadas:")
nh=int(input())
print("Introduzca precio horas trabajadas:")
ph=int(input())
print("Introduzca número de kilómetros:")
k=int(input())
#Debemos calcular las horas extras, el salario base y el extra.
he=None
sb=None
se=None
#d serán las dietas
d=""
#st = salario total
st=None
#rt = retencion
rt=None
if(nh>36):
    #Tenemos horas extra
    he=nh-36
    sb=ph*36
    se=he*(ph+2)
else:
    #No tenemos horas extra
    he=0
    se=0
    sb=nh*ph
#Calculamos el precio para las dietas de KM
if(k<=100):
    d="Dieta Internacional"
elif(k>=101 and k<=500):
    d="Dieta Nacional"
else:
    d="Dieta Internacional"
#Calculamos si tenemos retencion
st=sb+se
if(st<=250):
    rt="No tiene retencion"
elif(st>=251 and st<=800):
    rt="Retención del 20%"
else:
    rt="Retención del 40%"
print("Numero de horas: "+str(nh))
print("Precio horas: "+str(ph))
print("Kilómetros: "+str(k))
print("Horas extra: "+str(he))
print("Salario extra: "+str(se))
print("Salario base: "+str(sb))
print("Salario total: "+str(st))
print(d)
print(rt)
print("Fin del programa")