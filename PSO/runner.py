#############################
# Ralph Pereira             #
# COSC3P71 Assignment 3     #
# Basic PSO                 #
#############################

from pso import PSO
def CreateTestFiles():
    p1 = PSO(30,0.729844,1.496180,1.496180,200,5000)
    p2 = PSO(30,0.4,1.2,1.2,200,5000)
    p3 = PSO(30,1,2,2,200,5000)
    p4 = PSO(30,-1,2,2,200,5000)
    r1 = PSO(30,0.729844,1.496180,1.496180,200,5000)

    for i in range(1):
        f1 = "Test\p1_" + str(i+1) + ".txt"
        f2 = "Test\p2_" + str(i+1) + ".txt"
        f3 = "Test\p3_" + str(i+1) + ".txt"
        f4 = "Test\p4_" + str(i+1) + ".txt"
        p1.SolvePso(f1)
        p2.SolvePso(f2)
        p3.SolvePso(f3)
        p4.SolvePso(f4)
        p1 = PSO(30,0.729844,1.496180,1.496180,200,5000)
        p2 = PSO(30,0.4,1.2,1.2,200,5000)
        p3 = PSO(30,1,2,2,200,5000)
        p4 = PSO(30,-1,2,2,200,5000)
        rand = "Test\r1_" + str(i+1) + ".txt"
        r1.RandomSearch(rand)
def CreateResults(x):
    p1 = PSO(30,0.729844,1.496180,1.496180,200,5000)
    p2 = PSO(30,0.4,1.2,1.2,200,5000)
    p3 = PSO(30,1,2,2,200,5000)
    p4 = PSO(30,-1,2,2,200,5000)
    r1 = PSO(30,0.729844,1.496180,1.496180,200,5000)
    pa1 = []
    pa2 = []
    pa3 = []
    pa4 = []
    for i in range(x):
        print("Pass by",i)
        pa1.append(p1.SolvePso())
        pa2.append(p2.SolvePso())
        pa3.append(p3.SolvePso())
        pa4.append(p4.SolvePso())       
    f = open("fn",'w')
    f.write(str(sum(pa1)/len(pa1)))
    f.write(str(sum(pa2)/len(pa2)))
    f.write(str(sum(pa3)/len(pa3)))
    f.write(str(sum(pa4)/len(pa4)))
    f.close()

CreateResults(2)
