from particle import Particle
import random
import math
SwarmSize = 3
Swarm = []
dimension = 30
#the best fit is a particle
GlobalFit = Particle(dimension)
#create a swarm with dimension D

def InitilizeSwarm(d):
    for i in range(SwarmSize):
        p = Particle(d)
        Swarm.append(p)
def UpdateVelocity(d,w,c1,c2):
    for i in range(SwarmSize):        
        for j in range(d):
            r1 = random.random()  
            r2 = random.random()
            #calculate the new velocity 
            Swarm[i].v[j] = ((w*Swarm[i].v[j])+(c1*r1*(Swarm[i].bestX[j]-Swarm[i].x[j]))+(c2*r2*(GlobalFit.x[j] - Swarm[i].x[j]))) 
            #if the velocity goes past the bounds of the current x min and max, it will loop back around
            if Swarm[i].v[j] < -5.12:
                Swarm[i].v[j] = 5.12
            elif Swarm[i].v[j] > 5.12:
                Swarm[i].v[j] = -5.12
        for j in range(d):
            Swarm[i].x[j] += Swarm[i].v[j]
        Swarm[i].UpdateFitness()
#get the best fitness for the entire swarm
def GetBestFit():
    global GlobalFit
    bf = GlobalFit
    for i in range(SwarmSize):
        if Swarm[i].bestFit < bf.bestFit:
            bf = Swarm[i]
    return bf 
#prints out the entire swarm
def DisplaySwarm():
    for i in range(SwarmSize):
        print("Particle: " + str(Swarm[i].x) + "Best X: "+str(Swarm[i].bestX))


def SolvePso():
    global dimension
    d = dimension
    w = 0.729    # inertia
    c1 = 1.49445 # cognitive
    c2 = 1.49445 # social 
    InitilizeSwarm(d)
    #set the best fit to a high number
    GlobalFit.bestFit = 10000
    for i in range(225):
        print("\nPass by #: " + str(i+1))
        #DisplaySwarm()
        GlobalFit = GetBestFit()
        print("Global Best: " + str(GlobalFit.bestFit))
        UpdateVelocity(d,w,c1,c2)

SolvePso()