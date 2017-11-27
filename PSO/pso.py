from particle import Particle
 
SwarmSize = 3
Swarm = []
d = 3
#the best fit is a particle
GlobalFit = Particle(d)
#create a swarm with dimension D
def InitilizeSwarm(d):
    for i in range(SwarmSize):
        p = Particle(d)
        Swarm.append(p)
def UpdateVelocity():
    for i in range(SwarmSize):
        x = Swarm[i].getX()
        for j in range(len(x)):
            x[j] -= 0.1
        Swarm[i].setX(x)
        Swarm[i].UpdateFitness()
#get the best fitness for the entire swarm
def GetBestFit():
    global GlobalFit
    bf = GlobalFit
    for i in range(SwarmSize):
        if Swarm[i].getBestFit() < bf.getBestFit():
            bf = Swarm[i]
    return bf 
#prints out the entire swarm
def DisplaySwarm():
    for i in range(SwarmSize):
        print("Particle: " + str(Swarm[i].getX()) + "Best Fit: "+str(Swarm[i].getBestFit()))



InitilizeSwarm(d)
#set the best fit to a high number
GlobalFit.bestFit = 10000
for i in range(2):
    print("Pass by #: " + str(i+1))
    DisplaySwarm()
    GlobalFit = GetBestFit()
    print("\nGlobal Best: " + str(GlobalFit.getX()))
    UpdateVelocity()
