#############################
# Ralph Pereira             #
# COSC3P71 Assignment 3     #
# Basic PSO                 #
#############################

#Particle Object
import random
import math

class Particle:
    #constructor for the class particle, define all the initial variables
    def __init__(self,d):
        self.d = d #dimension size
        self.x = [random.uniform(-5.12,5.12) for i in range(self.d)] #random x values between -5.12 and 5.12
        self.f = self.SolveRast() #get the fitness value for the current particle
        self.v = [0.0 for i in range(self.d)] #set the inital velocity to zero
        self.bestFit = self.f #the best fitness will be the current fitness value
        self.bestX = self.x[:] #the best x set will be the current x set
    
    #gets the fitness of the x values, uses the function given to us in the assignment 
    def SolveRast(self):
        fit = 10*self.d
        for i in range(1,self.d):
            try:
                fit += self.x[i]**2 - (10*math.cos(2*math.pi*self.x[i]))
            #Catches for the fitness, if it goes too high Math errors occour
            except OverflowError:
                break
            except ValueError:
                break
        return fit
    #Update the best fitness of the particle
    def UpdateFitness(self):
        self.f = self.SolveRast()
        if self.f < self.bestFit:
            self.bestFit = self.f
            self.bestX = self.x[:]

        