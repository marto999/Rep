import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
import random
###graficacion del camino
    
def caminosaleatorio():
    mov = {0: (0, -1), 1: (0, 1), 2: (1, 0), 3: (-1, 0)}
    walk=[[0,0]]
    acum=0
    walkA=[]

    while(acum!=4):   
        step=[]    
        n=random.randint(0,3)
        step += [[walk[-1][0] + mov[n][0], walk[-1][1] + mov[n][1]]]
        
        ##comprobacion del paso anterior en la lista
        if(step[0] not in walkA):
            walkA.append(step[0])
            ##acumulador aumenta este paso para verificar que se pueda o no seguir moviendo
            acum+=1
        ##comprabacion del paso inexistente en el camino para sumarlo     
        if(step[0] not in walk):
            walk.extend(step)
            acum=0
            walkA=[]
    n = len(walk)
    
    x = []
    y = []
    for e in walk:
        x += [e[0]]
        y += [e[1]]

    plt.plot(x,y)

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.gca().set_aspect('equal', adjustable='box')
    
    return n

def simulacion():
    numSim = 10
    s = []
    for i in range(numSim):
        s += [caminosaleatorio()]
    w= np.array(s)
    
    print('The mean distribution of steps in 1000 simulation is' , stats.median(w))

def impresion():
    
    
    print( 'DEBER 01 SARW CATOTA ESCOBAR LLANGARI')
    print('')
    simulacion()
    print('')
    
    print('The second graph is de frecuency - distribution of steps in 1000 simulations')   

    plt.show()
    
   
impresion()
