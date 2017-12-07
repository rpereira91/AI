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
        self.d = d
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.Swarm = []
        self.SwarmSize = ss
        self.epoch = epoch


    def SolvePso(self,fn): 
        self.InitilizeSwarm()
        #the best fit is a particle
        GlobalFit = Particle(self.d)
        GlobalFit.bestFit = 10000
        #set the best fit to a high number
        f = open(fn,'w')
        for i in range(self.epoch):
            self.UpdateVelocity(self.d,self.w,self.c1,self.c2,GlobalFit)
            GlobalFit = self.GetBestFit(GlobalFit)
            f.write(str(GlobalFit.bestFit)+"\n")
        f.close()

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
                #Update the x values
                self.Swarm[i].x[j] += self.Swarm[i].v[j]
                #Clamping the x values doesn't seem to work but here's were I would try to clamp
                # if self.Swarm[i].x[j] > 5.12:
                #     self.Swarm[i].x[j] = 5.12
                # elif self.Swarm[i].x[j] < -5.12:
                #     self.Swarm[i].x[j] = -5.12
                #get the new fitness for the current particle
                self.Swarm[i].UpdateFitness()
    #get the best fitness for the entire swarm
    def GetBestFit(self,gb):
        for i in range(self.SwarmSize):
            if self.Swarm[i].bestFit < gb.bestFit:
                gb = self.Swarm[i]
        return gb
    #prints out the entire swarm
    def DisplaySwarm(self):
        for i in range(self.SwarmSize):
            print("Particle: " + str(self.Swarm[i].x) + "Best X: "+str(self.Swarm[i].bestX))



