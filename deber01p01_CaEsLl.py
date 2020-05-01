import numpy as np
import matplotlib.pyplot as plt

##variables
x=[]
y=[]
steps = [[0,0]]

##generacion de numeros aleatorios
n = np.random.randint(4, size=20)
print (n)

##generacion de movimientos
mov = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


##
for i in n:
    steps += [[steps[-1][0] + mov[i][0], steps[-1][1] + mov[i][1]]]
print(steps)
##
for e in steps:
    x += [e[0]]
    y += [e[1]]

##IMPRESION DE LOS GRAFICOS 
plt.plot(x, y,  color= 'r')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()