class Mes:
    nombre=""
    max=0
    min=0
    def getMedia(self):
        return (self.max+self.min)/2
    #Por comodidad, voy a devolver en el print del objeto el nombre
    #mes, la maxima, minima y media.
    def __str__(self):
        return (self.nombre+", Máxima: "+str(self.max)+", Mínima: "+str(self.min)+", Media: "+str(self.getMedia()))