import pyodbc
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
conexion=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="+servidor
+"; DATABASE="+bbdd+";UID="+usuario+";PWD="+password)
#Pediremos los datos:
#El número será un sttring porque lo voy a concatenar abajo.
#Buena praxis será definir el nombre de las variables evitando las
#abreviaturas porque en códigos largos, no sabremos lo que estamos
#haciendo referencia.
# numero=input("Introduzca el número de departamento: ")
# nombre=input("Introduzca el nombre del departamento: ")
# localidad=input("Introduzca la localidad del departamento: ")
#Creamos el cursor
cursor=conexion.cursor()
#Un truco para saber que hemos introducido las cosas bien en la consulta
#sql, es hacer un print y ver si tiene lógica dentro de SQL.
# print(str(numero)+nombre+localidad)
# sql="insert into dept values ("+numero+", '"+nombre+"', '"+localidad+"')"
# #Ejecutamos la consulta
#cursor.execute(sql)
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
#Vamos a intentar reutilizar el cursor para mostrar los departamentos
sqlselect="select dept_no, dnombre, loc from dept"
cursor.execute(sqlselect)
print("----------------DEPARTAMENTOS-----------------")
for row in cursor:
    print(row.nombre+ ","+row.localidad)
#Cerramos la conexión
conexion.close()
print("Fin de programa.")