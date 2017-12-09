#############################
# Ralph Pereira             #
# COSC3P71 Assignment 3     #
# Basic PSO                 #
#############################

from pso import PSO
p1 = PSO(30,0.729844,1.496180,1.496180,200,5000)
p2 = PSO(30,0.4,1.2,1.2,200,5000)
p3 = PSO(30,1,2,2,200,5000)
p4 = PSO(30,-1,2,2,200,5000)

for i in range(10):
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
