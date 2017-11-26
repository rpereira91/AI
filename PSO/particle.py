# Ralph Pereira
# COSC3P71 Assignment 3
# Basic PSO
###################################################################

#Particle Object
class Particle:
    def __init__(self,x,y,v,f):
        self.x = x
        self.y = y
        self.v = v
        self.f = f
    #Getter defs for the I and J location variables 
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getV(self):
        return self.v
    def getF(self):
        return self.f
    def setF(self,f):
        self.f = f
    def setNewLocation(self,x,y,v,f):
        self.x = x
        self.y = y
        self.v = v   
        self.f = f    