class Coche:
    marca=""
    modelo=""
    velocidad=0
    #Deberiamos tener un estado para saber si el coche está arrancado
    #o no.
    estado=False
    def acelerar(self):
        if(self.estado==False):
            print("Primero debe arrancar el coche.")
        else:
            self.velocidad+=20
            print("Velocidad: "+str(self.velocidad))
    def frenar(self):
        if(self.velocidad==0):
            print("El coche está detenido")
        else:
            self.velocidad-=20
            print("Velocidad: "+str(self.velocidad))
    def arrancar(self):
        #Cambiamos del estado a arrancado
        self.estado=True
        print("Arrancando coche...")
    def detener(self):
        self.estado=False
        self.velocidad=0
        print("Coche detenido...")