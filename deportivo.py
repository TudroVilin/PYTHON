from pacocoche import Coche
class Deportivo(Coche):
    def turbo(self):
        self.velocidad+=80
        print("Activando turbo... "+srt(self.velocidad))
    def acelerar(self):
        self.velocidad+=100
        print("Velocidad actual: "+self.marca+": "+str(self.velocidad))