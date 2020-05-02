import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

walk = [[0,0,0]]
step = [0, 0, 0]
x = 0
for i in range(40):
    #axis refieres a ejes 0=x 1=y 2=z 
    axis = random.randrange(0, 3)
    # aumento o disminucion de paso en ejes
    step[axis] += random.choice([-1, 1])
    walk.append(step[:])
    

boolArr = ( walk == [[0,0,0]])
result = np.where(boolArr)

print (result)


print (walk)


x, y, z = zip(*walk)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
ax.scatter(x[-1], y[-1], z[-1], c='b', marker='o') 
ax.legend()
plt.show()

