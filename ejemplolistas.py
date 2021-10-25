nombres=["Ana","Adrián","Lucía","Carlos","Pedro","Rodrigo","Ana"]

def mostrarNombres():
    l=len(nombres)
    for i in range(l):
        name=nombres[i]
        print(str(i)+".- "+name)

print("Ejemplo de listas:")
#AÑADIMOS UN NUEVO NOMBRE
nombres.append("El nuevo.")
#Insertamos un elemento en el medio.
nombres.insert(3, "El del medio")
#Eliminamos al elemento Ana.
#Remove está bien, pero en realidad puede llevarnos a errores de lógica,
#porque a lo mejor el usuario quería eliminar el útilmo elemento Ana
nombres.remove("Ana")
#Eliminamos utilizando el INDICE
nombres.pop(6)
mostrarNombres()
#Borramos todo el contenido de la lista
nombres.clear()
print("El clear va después:")
mostrarNombres()
# print("LISTA DE NUMEROS ENTEROS")
# numeros=[20,14,55,99,77]
# #ORDENAR NUMEROS
# numeros.sort()
# print("Numero ordenados.")
# numeros.sort(reverse=True)
# print("Numeros ordenados mayor a menor.")
# for num in numeros:
#     print(num)
# #PARA RECUPERAR UN VALOR, SE UTILIZA UN ÍNDICE
# print("Primer número de la lista: "+str(numeros[0]))
# print("LISTA DE STRINGS")
# mostrarNombres()

