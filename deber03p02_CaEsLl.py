import numpy as np 
from scipy import random 
import matplotlib.pyplot as plt

  
#1.Develop a random-variate generator for a random variable X with the pdf 

x1=np.linspace(-5,0,100)
fx1=np.e**(2*x1)

x2=np.linspace(5,0,100)
fx2=np.e**(-2*x2)
 
print(np.trapz(fx1,x1))
print(np.trapz(fx2,x2))
print("\n")


plt.show()



#Inverse Transform Sampling (ITS) 

#Inversa f1:  ln(2x)/2
#Inversa f2:  -ln(-2x)/2


#Generador de números randómicos
size=1000
AX=[]
AY=[]

for i in range(size):
    randomX=random.uniform(-5, 5) 
    

    if(randomX>0 and randomX<0.5):
        y=(np.log(2*randomX))/2
        AX.append(randomX)   
        AY.append(y)

    if(randomX>=0.5 and randomX<=1):
        nrandomX=randomX*-1
        y=(-np.log(-2*nrandomX))/2
        AX.append(randomX)       
        AY.append(y)

print('\nAX: ',AX)
print('\nAY: ',AY)

plt.plot(x1,fx1)
plt.plot(x2,fx2)

#(img.ravel(),256,[0,256])

plt.hist(AY, density=True, bins=100)
plt.show()

#Rejection method (RM).





