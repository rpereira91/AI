from pso import PSO
p1 = PSO(30,0.729844,1.496180,1.496180,30,5000)
p2 = PSO(30,0.4,1.2,1.2,30,5000)
p3 = PSO(30,1,2,2,30,5000)
p4 = PSO(30,-1,2,2,30,5000)

for i in range(5):
    f1 = "p1_" + str(i) + ".txt"
    # f2 = "p2_" + str(i) + ".txt"
    # f3 = "p3_" + str(i) + ".txt"
    # f4 = "p4_" + str(i) + ".txt"
    p1.SolvePso(f1)
    # p2.SolvePso(f2)
    # p3.SolvePso(f3)
    # p4.SolvePso(f4)
    p1 = PSO(30,0.729844,1.496180,1.496180,30,5000)
    # p2 = PSO(30,0.4,1.2,1.2,30,5000)
    # p3 = PSO(30,1,2,2,30,5000)
    # p4 = PSO(30,-1,2,2,30,5000)
