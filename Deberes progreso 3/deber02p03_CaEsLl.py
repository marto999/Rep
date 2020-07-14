import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats



def literal1():
    profitL =[]
    flag =0
    Ep = 0
    EpA = []
    t = []
    var = 0
    x = np.random.randint(100000,140000, size=40 )
    x.sort()
    
    while(flag < len(x)):
        
        for i in x:
            profit = i - 100000
            bid = 0
            simulation = 100000
            u =[]
            for j in range(simulation):
                xC = np.random.randint(70000, 140000)
                u.append(xC)
                if xC > i:
                    bid += 1
            
            Ep = (bid/simulation) * i
            EpA.append(Ep)
            flag +=1
    
    print('Oferta', x)
    print('Utilidad Esperada', EpA)
    var = np.mean(EpA)
    print(' ')
    print('Bid estimated', var)
    plt.subplot(2,2,1)
    plt.plot(x,EpA, color='green', linestyle='dashed', linewidth= 1, marker='o', markerfacecolor='blue', markersize=3)      
    plt.xlabel('Oferta')
    plt.ylabel('Utilidad_Esperada')
    


def literal2() :
    print('DEBER 2 LITERAL 2')
    t= np.random.randint(30, 60, size=30)
    mu, sigma = 40, 7 # media y variacion estandar
    normal = stats.norm(mu, sigma)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x)
    prob = np.max(fp)
    fx= x - 40 / 7
    val= 1.645

    t = (val *7 ) + 40 ##51.52
    seg, min = math.modf(t)
    minF= 60 - min
    segF= 0.60 - seg

    print ('Tiempo de viaje maximo', t)
    print ('min', minF)
    print('seg', segF)

    plt.subplot(2,2,2)
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.ylabel('probabilidad')
    plt.xlabel('valores')

    

literal1()
literal2()

plt.show()

