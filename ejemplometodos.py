def ejemploMetodo1():
    print("Soy el método 1...")

def ejemploMetodo2():
    print("Soy el método 2...")
    ejemploMetodo3()

def ejemploMetodo3():
    print("Soy el método 3...")

print("Ejemplo de métodos")
print("Programa principal")
#Si realizamos la llamada, dará un salto, para leer el contenido del
#método1
n=1
if(n==2):
    ejemploMetodo1()
else:
    ejemploMetodo2()
ejemploMetodo1()
ejemploMetodo2()
print("Fin de programa")