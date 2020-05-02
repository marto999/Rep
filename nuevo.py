
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
N=40
R = np.random.randint(6, size=N)
print (R)

x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)


#condiciones para movimientos
x[ R==0 ] = -1
x[ R==1 ] = 1
y[ R==2 ] = -1
y[ R==3 ] = 1
z[ R==4 ] = -1
z[ R==5 ] = 1


x = np.cumsum(x)
y = np.cumsum(y)
z = np.cumsum(z)
print (x)
print (y)
print (z)



plt.figure()
ax = plt.subplot(1,1,1, projection='3d')
ax.plot(x, y, z, alpha=0.6)
ax.scatter(x[-1],y[-1],z[-1])
plt.show()

