from particle import Particle
 
SwarmSize = 3
Swarm = []
def InitilizeSwarm(d):
    for i in range(SwarmSize):
        p = Particle(d)
        Swarm.append(p)
def DisplaySwarm():
    for i in range(SwarmSize):
        print("Particle: " + str(Swarm[i].getX()) + "Best Fit: "+str(Swarm[i].getBestFit()))




InitilizeSwarm(3)
DisplaySwarm()
