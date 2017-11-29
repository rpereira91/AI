from pso import PSO
p1 = PSO(30,0.729844,1.496180,1.496180,30,5000)
for i in range(5):
    filename = "p1_" + str(i)
    p1.SolvePso(filename)