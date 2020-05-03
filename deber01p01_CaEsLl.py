# Python code for 1-D random walk. 
import random 
import numpy as np 
import matplotlib.pyplot as plt 

# Probability to move up or down 
prob = [0.05, 0.95] 

<<<<<<< HEAD
# statically defining the starting position 
start = 2
positions = [start] 
=======
##generacion de numeros aleatorios
n = np.random.randint(4, size=20)

>>>>>>> 3cb1ee385920cfe7db3e60c7659212bd00d388ac

# creating the random points 
rr = np.random.random(1000) 
downp = rr < prob[0] 
upp = rr > prob[1] 


<<<<<<< HEAD
for idownp, iupp in zip(downp, upp): 
	down = idownp and positions[-1] > 1
	up = iupp and positions[-1] < 4
	positions.append(positions[-1] - down + up) 
=======
##
for i in n:
    steps += [[ steps[-1][0] + mov[i][0], steps[-1][1] + mov[i][1] ]]
print(steps)
##
for e in steps:
    x += [e[0]]
    y += [e[1]]
>>>>>>> 3cb1ee385920cfe7db3e60c7659212bd00d388ac

# plotting down the graph of the random walk in 1D 
plt.plot(positions) 
plt.show() 

help(numpy)
