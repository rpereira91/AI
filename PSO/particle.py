# Ralph Pereira
# COSC3P71 Assignment 3
# Basic PSO
###################################################################

#Particle Object
import random
import math

class Particle:
    def __init__(self,d):
        self.d = d
        self.x = [random.uniform(-5.12,5.12) for i in range(self.d)]
        self.f = self.SolveRast()
        self.bestFit = self.f
    #Getter defs for the I and J location variables 
    def getX(self):
        return self.x
    def getFit(self):
        return self.f
    def getV(self):
        return self.v
    def getBestFit(self):
        return self.bestFit
    def setX(self,x):
        self.x = x[:]
    def SolveRast(self):
        fit = 10*self.d
        for i in range(1,self.d):
            fit += self.x[i]**2 - (10*math.cos(2*math.pi*self.x[i]))
        return fit
    def UpdateFitness(self):
        fit = self.SolveRast()
        if fit < self.bestFit:
            self.bestFit = fit
        self.f = fit
    def BadFit(cls):
        p = Particle(d)
        p.bestFit = 1000
        return cls(p)

        