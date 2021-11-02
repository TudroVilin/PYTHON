import pyodbc
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
conexion=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="+servidor
+"; DATABASE="+bbdd+";UID="+usuario+";PWD="+password)
cursor=conexion.cursor()
print("Conexión exitosa...")
print("")
sqlenfermos="select apellido, inscripcion from enfermo"
cursor.execute(sqlenfermos)
print("Apellido___Número inscripción")
for apellido, inscripcion in cursor:
    print(apellido+", "+inscripcion)
print("")
print()
print("")
respuesta=input("¿Desea eliminar un enfermo? y/n: ")
if(respuesta=="y"):
    print("")
    print("Introduzca el número de enfermo:")
    enfermo=int(input())
    print("")
    sqlborrar="delete from enfermo where inscripcion=?"
    cursor.execute(sqlborrar,(enfermo))
    sqlactualizado="select apellido, inscripcion from enfermo"
    cursor.execute(sqlactualizado)
    for apellido, inscripcion in cursor:
        print(apellido+", "+inscripcion)
    print("")
else:
    print("Cerrando el programa.")
cursor.close()
conexion.close()
print("Desconexión con éxito...")
print("Fin del programa.")