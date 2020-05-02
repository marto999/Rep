import numpy as np
import matplotlib.pyplot as plt

N=40
n = np.random.randint(6, size = N)
print (n)

x = []
y = []
z = []

for i in n:
    if (n[i] == 0):
        x[i]=-1;
    elif (n[i] == 1):
        x[i]=1;
    elif (n[i] == 2):
        y[i]=-1;
    elif (n[i] == 3):
        y[i]=-1;
    elif (n[i] == 4):
        z[i]=-1;
    elif (n[i] == 5):
        z[i]=-1;

x = np.cumsum(x)
y = np.cumsum(y)
z = np.cumsum(z)

print (x)
print (y)
print (z)
print (x)
print (y)
print (z)

