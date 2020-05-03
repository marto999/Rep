import random 
import numpy as np 
import matplotlib.pyplot as plt 

print('Ejercicio #2 - Random Walk 5%')
print('Integrantes: Catota-EscobarLlangari')
print('---------------------------------------------------------')

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
    plt.plot(x)
    return sum



def main ():
    
    numSim=50
    count=0
    for i in range(numSim):
        print("\nSimulación #",i+1)
        count+=walk()
      
    print("----------------------------\nTotal:",count)
    print("Prom :",count/numSim)
    
    plt.show()
main()



