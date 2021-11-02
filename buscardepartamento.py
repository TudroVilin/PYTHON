import pyodbc
print("Buscador de departamentos")
print("")
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +servidor+ "; DATABASE=" +bbdd+ "; UID=" +usuario+ "; PWD=" +password)
print("")
print("Intentando conectar...")
conexion=pyodbc.connect(cadenaconexion)
print("")
print("---CONEXIÓN CON EXITO---")
print("")
print("Consulta a la BBDD:")
print("")
# Vamos a utilizar el número para CONCATENAR la consulta SQL.
# Deberíamos capturar el número str para concatenarlo con el str SQL.
a=input("Introduzca el departamento a buscar: ")
print("")
sql="select dept_no, DNOMBRE, loc from DEPT where dept_no="+a
cursor=conexion.execute(sql)
row=cursor.fetchone()
if(not row):
    print("No existe el departamento.")
else:
    print(row.DNOMBRE+", "+row.loc)
print("")
cursor.close()
conexion.close()
print("Fin de programa.")