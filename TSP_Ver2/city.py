# Ralph Pereira
# COSC3P71 Assignment 2
# TSP using a GA
###################################################################

#City Object
class City:
    def __init__(self,x,y):
        self.i = x
        self.j = y
    #Getter defs for the I and J location variables 
    def getI(self):
        return self.i
    def getJ(self):
        return self.j