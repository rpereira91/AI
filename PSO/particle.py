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
        self.v = [0.0 for i in range(self.d)]
        self.bestFit = self.f
        self.bestX = self.x[:]
    
    #gets the fitness of the x values
    def SolveRast(self):
        fit = 10*self.d
        for i in range(1,self.d):
            fit += self.x[i]**2 - (10*math.cos(2*math.pi*self.x[i]))
        return fit
    #Update the best fitness of the particle
    def UpdateFitness(self):
        fit = self.SolveRast()
        if fit < self.bestFit:
            self.bestFit = fit
            self.bestX = self.x[:]
        self.f = fit

        