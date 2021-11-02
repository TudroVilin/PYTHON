import pyodbc
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
conexion=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="+servidor
+"; DATABASE="+bbdd+";UID="+usuario+";PWD="+password)
#Creamos el cursor
cursor=conexion.cursor()
sql="insert into dept values (66,'PROGRAMACION','IBIZA')"
#Ejecutamos la consulta
cursor.execute(sql)
#Vamos a imprimir ROWCOUNT para averiguar si tenemos contenido en la
#propiedad
#Rowcount viene con un valor en las consultas de acción indica el
#número de filas que han sido afectadas por la consulta.
print("Rowcount: "+str(cursor.rowcount))
#Cuando realizamos consultas de acción, todas las consultas son 
#temporales, es decir, no se llevan a la BBDD. Para llevar las consultas
#de acción a la BBDD de forma permanente, debemos realizar un commit
#en el cursor.
cursor.commit()
#Cerramos el cursor
cursor.close()
#Cerramos la conexión
conexion.close()
print("Fin de programa.")