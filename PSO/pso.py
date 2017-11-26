from particle import Particle
import random
SpaceSize = 10000
SwarmSize = 30
Swarm = []
def InitilizeSwarm():
    for i in range(SwarmSize):
        p = Particle(random.randint(0,SpaceSize), random.randint(0,SpaceSize),0,0)
        Swarm.append(p)
def DisplaySwarm():
    for i in range(SwarmSize):
        print("(" + str(Swarm[i].getX()) + "," + str(Swarm[i].getY())+")")
    

InitilizeSwarm()
DisplaySwarm()
