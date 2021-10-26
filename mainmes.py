from mes import Mes
print("Temperatura máx. mín. y media para 12 meses")
print("")
lista=[]
for i in range(1,12):
    mes=Mes()
    max=mes.max()
    min=mes.min()
    med=mes.med()
    lista.append(str(i)+".-Mes "+str(mes)+(": ")+"Tªmax: "+str(max)+" TªMín: "+str(min)+" TªMed: "+str(med))
for i in range(1,12):
    print(lista[i])