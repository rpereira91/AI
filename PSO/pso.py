#############################
# Ralph Pereira             #
# COSC3P71 Assignment 3     #
# Basic PSO                 #
#############################
from particle import Particle
import random
import math


#create a swarm with dimension D
class PSO:
    def __init__(self,d,w,c1,c2,ss,epoch):
        self.d = d #set the dimensions
        #set the constants
        self.w = w 
        self.c1 = c1
        self.c2 = c2
        #initilize the swarm
        self.Swarm = []
        #set the swarm size
        self.SwarmSize = ss
        #set the number of iterations 
        self.epoch = epoch


    def SolvePso(self,fn="NONE"): 
        self.InitilizeSwarm()
        #the best fit is a particle
        GlobalFit = Particle(self.d)
        GlobalFit.bestFit = 10000
        #set the best fit to a high number
        #f = open(fn,'w')
        for i in range(self.epoch):
            self.UpdateVelocity(self.d,self.w,self.c1,self.c2,GlobalFit)
            GlobalFit = self.GetBestFit(GlobalFit)
            #Only used for creating the test file
            # f.write(str(GlobalFit.bestFit)+"\n")
        return GlobalFit.bestFit
        #f.close()

    def InitilizeSwarm(self):
        for i in range(self.SwarmSize):
            p = Particle(self.d)
            self.Swarm.append(p)
    #this updates the velocity for each particle
    def UpdateVelocity(self,d,w,c1,c2,gb):
        for i in range(self.SwarmSize): 
            #each x value within the particle is updated       
            for j in range(d):
                #random doubles between 0 and 1
                r1 = random.random()  
                r2 = random.random()
                #calculate the new velocity 
                self.Swarm[i].v[j] = ((w*self.Swarm[i].v[j])+(c1*r1*(self.Swarm[i].bestX[j]-self.Swarm[i].x[j]))+(c2*r2*(gb.x[j] - self.Swarm[i].x[j]))) 
                #Update the x values only if it's inside the range of -5.12 and 5.12
                if self.Swarm[i].x[j] + self.Swarm[i].v[j] >= -5.12 and self.Swarm[i].x[j] + self.Swarm[i].v[j] <= 5.12:
                    self.Swarm[i].x[j] += self.Swarm[i].v[j]

                #get the new fitness for the current particle
                self.Swarm[i].UpdateFitness()
    #get the best fitness for the entire swarm
    def GetBestFit(self,gb):
        for i in range(self.SwarmSize):
            if self.Swarm[i].bestFit < gb.bestFit:
                gb = self.Swarm[i]
        return gb
    def RandomSearch(self,fn):
        #the best fit is a particle
        GlobalFit = Particle(self.d)
        GlobalFit.bestFit = 10000
        #set the best fit to a high number
        f = open(fn,'w')
        for i in range(self.epoch):
            self.InitilizeSwarm()
            GlobalFit = self.GetBestFit(GlobalFit)
            f.write(str(GlobalFit.bestFit)+"\n")
        f.close()
