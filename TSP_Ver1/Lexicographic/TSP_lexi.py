from city import City
from random import randint
import math
from time import time


#the number of cities
totalCities = 3
#The basic map will be an array of cities
map = []
#size of the map
mapSize = 250
#the order of cities
order = []
bestOrder = []
#2d array for display
dm = [[0 for x in range(mapSize)] for y in range(mapSize)] 
bestDistance = 0
#randomly populates the map with the x and y locations
def CreateMap():
    for n in range(totalCities):
        temp = City(randint(1,mapSize),randint(1,mapSize))
        map.append(temp)
        order.append(n)
        dm[(temp.i)-1][(temp.j)-1] = 1
#displays out the map
def DisplayMap():
    for y in range(mapSize):
        print(dm[y])
#find the distance between 2 points
def CalculateDistance(point1, point2):
    return math.hypot(point2.i - point1.i, point2.j - point1.j)
#get the total distanc
def CalculateTotalDistance():
    currentDistance = 0
    for ord in range(0, totalCities-1):
        currentDistance += CalculateDistance(map[order[ord]],map[order[ord+1]])
    return currentDistance
#finds all the purmatations of the array
def perm():
    largestI = -1
    for i in range(0,len(order)-1):
        if order[i] < order[i+1]:
            largestI = i
    if largestI == -1:
        return False
    largestJ = 0
    for j in range(0,len(order)):
        if order[largestI] < order[j]:
            largestJ = j
    Swap(order, largestI, largestJ)
    tempArr = order[largestI+1:]
    tempArr = tempArr[::-1]
    InsertArray(tempArr, largestI+1)
    return True
#swaps two elements of an array  
def Swap(x, i, j):
    temp = x[i]   
    x[i] = x[j]
    x[j] = temp
#appends one array onto another  
def InsertArray(tempArr, largestJ):
  for i in range(0, len(tempArr)):
    order[largestJ+i] = tempArr[i]
#main logic behind solving the map
def SolveMap():
    CreateMap()
    #DisplayMap()
    bestDistance = CalculateTotalDistance()
    while(perm()):
        tempD = CalculateTotalDistance()
        # print("Current order of cities: " + str(order))
        # print("Best Distance: %.2f \tCurrent Distance: %.2f" % (bestDistance , tempD))
        #if the current distance is better than the "best distance" it will copy the order into a new arry
        # and make the best distance the current distance
        if bestDistance > tempD:
            bestDistance = tempD
            bestOrder = list(order)
    print("Best Distance: %.2f" %bestDistance + "\tBest order: " + str(bestOrder))

start = time() 
SolveMap()
end = time()
print("It took: %.5f seconds to complete" %(end-start))
