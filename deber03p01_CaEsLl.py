import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
def walk3d():
    walk = [[0,0,0]]
    step = [0, 0, 0]
    x = 0
    for i in range(40):
        #axis refieres a ejes 0=x 1=y 2=z 
        axis = random.randrange(0, 3)
        # aumento o disminucion de paso en ejes
        step[axis] += random.choice([-1, 1])
        walk.append(step[:])
    
    
    print (walk)

def walk4d():
    walk1= [[0,0,0,0]]
    step2=
    

walk3d()
#boolArr = ( walk == [[0,0,0]])
#result = np.where(boolArr)






