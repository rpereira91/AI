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


    def SolvePso(self): 
        self.InitilizeSwarm()
        #the best fit is a particle
        GlobalFit = Particle(self.d)
        GlobalFit.bestFit = 10000
        #set the best fit to a high number
        for i in range(self.epoch):
            print("\nPass by #: " + str(i+1))
            #DisplaySwarm()
            
            print("Global Best: " + str(GlobalFit.bestFit))
            self.UpdateVelocity(self.d,self.w,self.c1,self.c2,GlobalFit)
            GlobalFit = self.GetBestFit(GlobalFit)

    def InitilizeSwarm(self):
        for i in range(self.SwarmSize):
            p = Particle(self.d)
            self.Swarm.append(p)
    def UpdateVelocity(self,d,w,c1,c2,gb):
        for i in range(self.SwarmSize):        
            for j in range(d):
                r1 = random.random()  
                r2 = random.random()
                #calculate the new velocity 
                self.Swarm[i].v[j] = ((w*self.Swarm[i].v[j])+(c1*r1*(self.Swarm[i].bestX[j]-self.Swarm[i].x[j]))+(c2*r2*(gb.x[j] - self.Swarm[i].x[j]))) 
                #if the velocity goes past the bounds of the current x min and max, it will loop back around
                if self.Swarm[i].v[j] < -5.12:
                    self.Swarm[i].v[j] = 5.12
                elif self.Swarm[i].v[j] > 5.12:
                    self.Swarm[i].v[j] = -5.12
            for j in range(d):
                self.Swarm[i].x[j] += self.Swarm[i].v[j]
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



