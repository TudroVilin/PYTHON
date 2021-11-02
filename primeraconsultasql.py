import pyodbc #Esto es lo primero que necesitamos para conectarnos a
#SQL Server.
print("Primera consulta SQL Server")
#Después le tenemos que aclarar lo siguiente:
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +servidor+ "; DATABASE=" +bbdd+ "; UID=" +usuario+ "; PWD=" +password)
print("Intentando contectar...")
conexion=pyodbc.connect(cadenaconexion)
print("Conectado con éxito.")
cursor=conexion.cursor()
sql="select dept_no, dnombre, loc from dept"
cursor.execute(sql)
print("Número de Filas: "+str(cursor.rowcount))
cursor.close()
conexion.close()
print("Fin de programa")