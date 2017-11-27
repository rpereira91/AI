# Ralph Pereira
# COSC3P71 Assignment 3
# Basic PSO
###################################################################

#Particle Object
import random
import math

class Particle:
    def __init__(self,d):
        self.x = self.GenXValues(d)
        self.f = self.SolveRast(self.x,d)
        self.bestFit = self.f
    def GenXValues(self,d):
        return [random.uniform(-5.12,5.12) for i in range(d)]
    #Getter defs for the I and J location variables 
    def getX(self):
        return self.x
    def getFit(self):
        return self.f
    def getV(self):
        return self.v
    def getBestFit(self):
        return self.bestFit
    def setF(self,f):
        self.f = f
    def SolveRast(self,x,d):
        fit = 10*d
        for i in range(1,d):
            fit += x[i]**2 - (10*math.cos(2*math.pi*x[i]))
        return fit
        