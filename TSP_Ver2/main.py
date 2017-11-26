# Ralph Pereira
# COSC3P71 Assignment 2
# TSP using a GA
###################################################################
#import statements
from Gen import Gen
import numpy as np
import csv
#create the two maps
b1 = Gen("berlin52.tsp",0.0,1.0)
d1 = Gen("dj38.tsp",0.0,1.0)
b2 = Gen("berlin52.tsp",0.1,1.0)
d2 = Gen("dj38.tsp",0.1,1.0)
b3 = Gen("berlin52.tsp",0.0,0.9)
d3 = Gen("dj38.tsp",0.0,0.9)
b4 = Gen("berlin52.tsp",0.1,0.9)
d4 = Gen("dj38.tsp",0.1,0.9)
b5 = Gen("berlin52.tsp",0.05,0.95)
d5 = Gen("dj38.tsp",0.05,0.95)
#main logic for the test file creatation
def CalculatePath(m,genCount,filename):
    #open the file with the file name provided
    wf = open(filename,"w")
    wf.write("Generation No.\tBest Distance\tAverage Distance\n")
    #create the maps and calculate the fitness
    fit = m.CalculateFitness(m.GetTO())
    bestOrder = m.FindBest(m.travelOrder)
    travelDistance = m.CalculateTotalDistance(m.GetTO())
    #run it for "genCount" amount of Generations
    for i in range(genCount):
        m.NewGeneration(fit)
        fit = m.CalculateFitness(m.GetTO())
        #pick the over all best travel order
        if m.CalculateTravelDistance(bestOrder) > min(fit):
            bestOrder = m.FindBest(m.travelOrder)
        wf.write(str(i) + "\t" + str(min(fit)) +"\t" + str(np.average(fit)) +"\n")
    wf.write("Best Order: " + str(bestOrder) + "\n")
    wf.write("Best Distance: " + str(m.CalculateTravelDistance(bestOrder)))
    wf.write ("\nMutation Rate: %.2f%%\tCross over rate: %.2f%%" % (m.mutationRate*100, m.crossOverRate*100))
    wf.close()

#Calculates the path with the file name sent over
CalculatePath(b1,150,"Berlin-Crossover100-Mutation0.txt")
CalculatePath(d1,150,"Djibouti-Crossover100-Mutation0.txt")
CalculatePath(b2,150,"Berlin-Crossover100-Mutation10.txt")
CalculatePath(d2,150,"Djibouti-Crossover100-Mutation10.txt")
CalculatePath(b3,150,"Berlin-Crossover90-Mutation0.txt")
CalculatePath(d3,150,"Djibouti-Crossover90-Mutation0.txt")
CalculatePath(b4,150,"Berlin-Crossover90-Mutation10.txt")
CalculatePath(d4,150,"Djibouti-Crossover90-Mutation10.txt")
CalculatePath(b5,150,"Berlin-Crossover95-Mutation5.txt")
CalculatePath(d5,150,"Djibouti-Crossover95-Mutation5.txt")
CalculatePath(b2,300,"Berlin-Crossover100-Mutation10-Population300.txt")
CalculatePath(d2,300,"Djibouti-Crossover100-Mutation10-Population300.txt")
