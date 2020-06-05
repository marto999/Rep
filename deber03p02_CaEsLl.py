import numpy as np 
from scipy import random 
import matplotlib.pyplot as plt

  
#1.Develop a random-variate generator for a random variable X with the pdf 
x1=np.linspace(-5,0,100)
fx1=np.e**(2*x1)

x2=np.linspace(0,5,100)
fx2=np.e**(-2*x2)
 
print(np.trapz(fx1,x1))
print(np.trapz(fx2,x2))
print("\n")

############################################################################
#                      Inverse Transform Sampling                          #
############################################################################

size = 100000
U = np.random.rand(size)  # Uniform distribution sampling
AU=[]
#Inversa f1:  ln(2x)/2
#Inversa f2:  -ln(-2x)/2
#U < 0.5  # U distr. uniforme U(0,1)
#I1(U) else I2(U)  # I inversa de la acumulada

for i in range(len(U)):
    u=U[i]
    if(u<0.5):

        I1=(np.log(2*u))/2
        AU.append(I1)    
    else:
        I2=(-np.log((-2*u)+2))/2
        AU.append(I2)    

print("AU",AU)

plt.plot(x1,fx1,linewidth=3)
plt.plot(x2,fx2,linewidth=3)
plt.hist(AU,density=True,range=[-5,5],facecolor='red', edgecolor='black',bins=100)
plt.show()

############################################################################
#                          Rejection Method                                #
############################################################################
