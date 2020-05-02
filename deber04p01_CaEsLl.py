import matplotlib.pyplot as plt
import numpy as np

#numrandom = np.random.randint(10000,100000)/100000
p = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
formula = p**2*(2-p**2)
print(formula)

def prob():
    graf = np.random.choice([0, 1], p=[0.4, 0.6], size = (2,2))
    print(graf)
    plt.matshow(graf)
    plt.show()
    x = 1
    y = 0
   # a = np.array([[1,0], [1,0]])
   # b = np.array([[0,1], [0,1]])
   # c = np.array([[0,0], [1,0]])
   # d = np.array([[1,0], [0,0]])
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 0
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 0
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 0
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 0
    else:
        return 1
print(prob())

#rep = 10
#def perRange(rep):
#    per = [prob() for i in range(rep)]
#    return np.sum(per)

#sim = 100
#rep = 10
#sum_result = [perRange(rep) for i in range (sim)]

#sumatoria = len(np.where(np.array(sum_result) == rep/9))/sim
#print(sumatoria)