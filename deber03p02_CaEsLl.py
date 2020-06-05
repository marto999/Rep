import numpy as np 

import matplotlib.pyplot as plt
print('Deber 03:Develop a random-variate generator for a random variable X with the pdf)
print('Integrantes: Catota-Escobar-LLangarí')
  
 
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
plt.title("Inverse Transform Sampling")
plt.hist(AU,density=True,facecolor='red', edgecolor='black',bins=100)
plt.show()



############################################################################
#                          Rejection Method                                #
############################################################################






########################################################################################################
#                   2.Develop a generation scheme for the triangular distribution with pdf             #                                               #
########################################################################################################

x1 = np.linspace(2, 3, 100)
fx1 = 1/2 * (x1-2)

x2 = np.linspace(3, 6, 100)
fx2 = 1/2 * (2-x2/3)

np.trapz(fx1,x1)
np.trapz(fx2,x2)



a=2
b=6
c=3
size = 100000
U1 = np.random.rand(size)  # Uniform distribution sampling

AU1=[]

#I1= a + np.sqrt((b-a)*(c-a)*u)
#I2= b - np.sqrt((b-a)(b-c)(1-u))

for i in range(len(U)):
    u=U1[i]
    
    if (u < 0.25):
         I1=(a + (np.sqrt((b-a)*(c-a)*u)))
         AU1.append(I1)    
    else:
         I2=(b - (np.sqrt((b-a)*(b-c)*(1-u))))
         AU1.append(I2)    

plt.plot(x1,fx1,linewidth=3)
plt.plot(x2,fx2,linewidth=3)
plt.title("Inverse Transform Sampling")
plt.hist(AU1,density=True,facecolor='red', edgecolor='black',bins=100)
plt.show()










