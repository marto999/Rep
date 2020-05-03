import numpy as np
simulate = 1000


class Nodo:
    def __init__(self):
        self.position = np.array([0, 0, 0])
        self.position2 = np.array([0, 0, 0, 0])
        self.initial_position = np.array([0, 0, 0])
        self.initial_position2 = np.array([0, 0, 0, 0])
        self.directions = {'up': np.array([0, 1,0]),
                           'down': np.array([0, -1, 0]),
                           'right': np.array([1, 0, 0]),
                           'left': np.array([-1, 0, 0]),
                           'forward': np.array([0, 0, 1]),
                           'backward': np.array([0, 0, -1])
                           }

        self.directions2 = {'up': np.array([0, 1, 0, 0]),
                           'down': np.array([0, -1, 0, 0]),
                           'right': np.array([1, 0, 0, 0]),
                           'left': np.array([-1, 0, 0, 0]),
                           'forward': np.array([0, 0, 1, 0]),
                           'backward': np.array([0, 0, -1, 0]),
                           'back': np.array([0, 0, 0, 1]),
                           'front': np.array([0, 0, 0, -1])

                           }
    def move(self):
        direction_ = ['up', 'down', 'right', 'left', 'forward', 'backward']
        np.random.shuffle(direction_)
        direction = direction_[0]
        self.position += self.directions[direction]

    def move2(self):
        direction_ = ['up', 'down', 'right', 'left', 'forward', 'backward', 'back', 'front']
        np.random.shuffle(direction_)
        direction = direction_[0]
        self.position2 += self.directions2[direction]

def is_origin(node):
    return np.array_equal(node.position, node.initial_position)

def is_origin2(node):
    return np.array_equal(node.position2, node.initial_position2)

def walk_3d():
    flag = 0
    node = Nodo()
    while flag < 1000:
        flag += 1
        node.move()
        if is_origin(node):
            return True
    return False
def walk_4d():
    flag = 0
    node = Nodo()
    while flag < 1000:
        flag += 1
        node.move2()
        if is_origin2(node):
            return True
    return False

node = Nodo()
success = 0
success2 = 0
for i in range(simulate):
    if walk_3d():
        success += 1
    
for i in range(simulate):
    if walk_4d():
        success2 +=1
        
print('DEBER 03 P01 CATOTA - ESCOBAR - LLANGARI')
print('PROBABILITIES ')
print('The probability 3D walk', success/1000 )
print('The probability 4D walk', success2/1000 )


