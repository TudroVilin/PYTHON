import pyodbc
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
conexion=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="+servidor
+"; DATABASE="+bbdd+";UID="+usuario+";PWD="+password)
cursor=conexion.cursor() #Con esto hacemos que el cursor se conecte a
# la BBDD para poder ir añadiendo nuestras líneas de comando.
print("Conexión exitosa...")
print("")
print("Mostrando empleados y oficios:")
print("")
sqlempleadosyoficios="select apellido, oficio, salario from emp"
cursor.execute(sqlempleadosyoficios) #Aquí le estamos asignando al SQL
# su primera línea de comandos que queremos que ejecute.
print("APELLIDOS___OFICIO___SALARIO")
for row in cursor:
    print(row.apellido+", "+row.oficio+", "+str(row.salario)) #Mostramos
    # los datos antes de que puedan ser actualizados para que el usuario
    # elija el salario de qué oficio desea actualizar.
oficio=input("Introduca el nombre del oficio deseado: ")
sueldo=int(input("Introduzca el incremento de salario en %: "))
sueldo/=100 #Como he querido que el incremento sea en %, necesito saber
# cuánto quiero que aumente el salario.
sqlsueldoporoficio="update emp set salario*="+str(sueldo)+" where oficio='"+oficio+"'"
sqlactualizado="select apellido, oficio, salario from emp"
cursor.execute(sqlsueldoporoficio) #Con esto ejecutamos el cursor para
# que nos actualice la tabla tal y como hemos escogido.
cursor.execute(sqlactualizado) #Con este cursor lo que hacemos es que
# el cursor se actualice de forma que podamos después mostrar lo que
# acabamos de actualizar.
print("APELLIDO___OFICIO___SALARIO")
for row in cursor: #Aquí le estamos diciendo que para cada fila nos
    # muestre lo que tiene el cursor sqlactualizado.
    print(row.apellido+", "+row.oficio+", "+str(row.salario)) #Y con
    # esto, le estamos diciendo que nos muestre los valores que tiene
    # para esas variables que han sido actualizadas por el cursor 
    # dentro de la BBDD.
cursor.commit() #Con esto aplicamos los cambios que hemos hecho.
cursor.close() #Con esto cerramos el cursor.
conexion.close() #Con esto cerramos la conexión.
print("")
print("Desconexión con éxito...")
print("Fin de programa")