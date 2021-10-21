#Declaración de métodos
def saludo(nombre):
    print("Bienvenido, "+nombre)
def despedida(nombre,dia):
    print("Ha sido un placer hoy "+dia+", "+nombre)

#Programa principal
print("Ejemplo métodos con parámetros")
print("¿Cuál es su nombre?")
name=input()
# En la llamada, el nombre de variable NO tiene porqué coincidir.
# Son códigos distintos.
print("¿En qué día estamos?")
day=input()
#Por aquí utilizamos el valor...
#Ejemplo método que devuelve un valor upper()
#upper es un método que DEVUELVE el texto en mayúsculas
#si quieremos poner el texto en mayúsculas, debemos recuperar el valor
#que nos devuleve el método.
day=day.upper()
despedida(name,day)
print("Fin de programa")