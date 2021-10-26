#Necesitamos importar la clase Persona
from persona import *
print("Ejemplo clases Persona")
#Creamos una nueva persona
person=Persona()
print("Pais: "+person.pais)
person.pais="España"
print("Pais: "+person.pais)
#Cambiamos sus propiedades
person.nombre="Alumno"
person.apellido="Azure"
person.fechanacimiento=1984
person.getDescripcion("soy un buen estudiante")
#Podemos llamar a métodos
print(person.getNombreCompleto())
print("Edad: "+str(person.getEdad()))
print(person)