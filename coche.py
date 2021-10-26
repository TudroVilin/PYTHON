class Coche:
    marca=""
    modelo=""
    velocidad=0
    arrancado=0
    def __init__(self):
        return self.marca+self.modelo+self.velocidad+self.arrancado
    def arrancar(self):
        self.arrancado=1
        return self.arrancado
    def detener(self):
        self.arrancado=0
        return self.arrancado
    def acelerar(self):
        self.velocidad=self.velocidad+10
        return self.velocidad
    def frenar(self):
        self.velocidad=0
        return self.velocidad
