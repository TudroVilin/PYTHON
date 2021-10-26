import random
class Mes:
    tmax=0
    tmin=0
    tmed=0
    def max(self):
        self.tmax=random.randint(0,50)
    def min(self):
        self.tmin=random.randint(0,50)
        if(self.tmax<self.tmin):
            self.tmax=self.tmin
            self.tmin-=5
    def med(self):
        self.tmed=(self.tmax+self.tmin)/2
