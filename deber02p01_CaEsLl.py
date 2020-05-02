# Python code for 1-D random walk. 
import random 
import numpy as np 
import matplotlib.pyplot as plt 

def walk():
    m=10
    x=[0]
    sum=0
    while(x[-1]!=m):
        n=np.random.choice([-1,1],p=[0.5,0.5])
        if(x[-1]==0):
            x += [x[-1]+1]        
        else:
            if(x[-1]!=0):
                x += [x[-1]+n]
    sum=len(x)-1
    print(x)
    print("Pasos:",sum)
    #plt.plot(x)
    #plt.show()
    return sum


def main ():
    
    numSim=100
    count=0
    for i in range(numSim):
        print("\nSimulación #",i+1)
        count+=walk()
    print("----------------------------\nTotal:",count)
    print("Prom :",count/numSim)

main()



