# Ralph Pereira
# COSC3P71 Assignment 2
# TSP using a GA
###################################################################

#import statements
from city import City
import numpy as np
import copy
import random
import math
import time
import sys
#genetic object
class Gen(object):
  #initilize starting variables
  map = []
  travelOrder = []
  popSize = 1000
  totalCities = 0
  mutationRate = 0.1
  crossOverRate = 1.0

  def __init__(self,filename,mr,cr):
    f = open(filename, "r")
    mapFiles = []
    #populate the map with the points from the file
    [mapFiles.append(l) for l in f]
    for l in range(6,len(mapFiles)-1):
      line = mapFiles[l].split()
      #casting to a float
      if line[0].isdigit():
        temp = City(float(line[1]),float(line[2]))
        self.map.append(temp)
        self.totalCities += 1
    #create a random order
    order = [i for i in range(len(self.map))]
    for x in range (0, self.popSize):
      random.shuffle(order)
      self.travelOrder.append(list(order))
    self.mutationRate = mr
    self.crossOverRate = cr

#Calculates the fitness of the current Travel order
  def CalculateFitness(self, to):
    fitness = []
    for i in range(self.popSize):
      fitness.append(self.CalculateTravelDistance(to[i]))
    return fitness
#used to help calculate the fitness, it sums up the entire travel order
  def CalculateTravelDistance(self,orderArr):
    cd = 0
    for i in range(len(orderArr)-1):
      cd += self.CalculateDistance(self.map[orderArr[i]],self.map[orderArr[i+1]])
    return cd
#calculate the distance between 2 cities
  def CalculateDistance(self,point1, point2):
    return math.hypot(point2.getI() - point1.getI(), point2.getJ() - point1.getJ())    

#used to calculate the new generation of orders, with sudo-random chance it will pick an order set better than the last
  def NewGeneration(self,fit):
    newTO = []
    for i in range(self.popSize):
      newOrder = []
      firstOrder = self.PickChromosome(self.travelOrder,fit)
      secondOrder = self.PickChromosome(self.travelOrder,fit)
      #cross over
      if random.random() < self.crossOverRate:
        newOrder = self.UniformCrossOver(firstOrder, secondOrder)
        #mutates the new order
        newOrder = self.Mutate(newOrder)
        #adds it to the new 
        newTO.append(newOrder)
      else:
        #mutates the new order
        newOrder = self.Mutate(firstOrder)
        #adds it to the new 
        newTO.append(newOrder)
        
    self.travelOrder =  newTO
#Picks an element out of a tournment size of 10th the population of the population, it picks the element with the highest fitness value
  def PickChromosome(self,to,fit):
    rs = random.randint(0,len(fit)-int(self.popSize/10))
    lowestIndex = rs
    for i in range(int(self.popSize/10)):
      if fit[i+rs] < fit[lowestIndex]:
        lowestIndex = rs+i
    return to[lowestIndex]
  #two point cross over, pick a front and back from a, and move that to a new array, then fill the rest with b
  def TwoPointCrossOver(self,a,b):
    front = random.randint(0,len(a))
    back = random.randint(front ,len(a))
    newOrder = a[front:back]
    citiesLeft = self.totalCities - len(newOrder)
    for i in range(len(b)):
      if b[i] not in newOrder:
        newOrder.append(b[i])
    return newOrder
#take a subset of cities from order a the remaining elements from b and combines them
  def UniformCrossOver(self,a,b):
    bitMask = [random.randint(0,1) for i in range(self.totalCities)]
    newOrderA = [0 for i in range(len(a))]
    newOrderB = [0 for i in range(len(a))]
  #Uniform crossover
    for i in range(self.totalCities):
      if bitMask[i]:
        newOrderA[i] = a[i]
        newOrderB[i] = b[i]
    for i in range(self.totalCities):
      if newOrderA[i] == 0:
        for x in range(self.totalCities):
          if b[x] not in newOrderA:
            newOrderA[i] = b[x]
            break
      if newOrderB[i] == 0:
        for x in range(self.totalCities):
          if a[x] not in newOrderB:
            newOrderB[i] = a[x]
            break
    #picks the lowest costing route
    return newOrderA if self.CalculateTravelDistance(newOrderA) < self.CalculateTravelDistance(newOrderB) else newOrderB
   
#mutation of the order, if the random number is less than the rate it will swap elements
  def Mutate(self,order):
    ord = list(order)
    for i in range(0,self.totalCities):
      if random.random() < self.mutationRate:
        ord = self.swap(ord,i,random.randint(i,self.totalCities-1))
    return ord
#finds the best path, this can probably be optimized 
  def FindBest(self, to):
    best = self.CalculateTravelDistance(to[0])
    bestOrder = list(to[0])
    for i in range(1,self.popSize):
      temp = self.CalculateTravelDistance(to[i])
      if best > temp:
        bestOrder = list(to[i])
        best = temp
    return bestOrder
#switches the elements          
  def swap(self,x,i,j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp
    return x
#calculates travel distance
  def CalculateTotalDistance(self,to):
    travelDistance = []
    for i in range(self.popSize):
      travelDistance.append(self.CalculateTravelDistance(to[i]))
    return travelDistance
      
  def SetTO(self, to):
    self.travelOrder = to
  
  def GetTO(self):
    return self.travelOrder
        
  