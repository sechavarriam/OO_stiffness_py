import numpy as np

r1 = 1
r2 = 1.2

t0 = 0
t1 = 30
t2 = 45
t3 = 60
t4 = 90

#nodosP_MATLAB = [r1, t4; ]

nodosPolares = np.array([
    [r1,t4],
    [r2,t3],
    [r1,t2],
    [r2,t1],
    [r1,t0],
    [r2,t4],
    [r1,t3],
    [r2,t2],
    [r1,t1],
    [r2,t0]
])

print(nodosPolares)

import math

nodos = []

for nodo in nodosPolares:
    x = nodo[0]*math.cos(nodo[1]*math.pi/180)
    y = nodo[0]*math.sin(nodo[1]*math.pi/180)
    c = [x,y]
    nodos.append(c)
    print("[{:.2f},{:.2f}]".format(c[0],c[1]))

nodos = np.array(nodos)

elementos = np.array([
    [1,7],
    [1,6],
    [6,2],
    [6,7],
    [5,10],
    [4,10],
    [5,4],
    [9,5],
    [9,4],
    [8,4],
    [8,9],
    [3,9],
    [2,8],
    [3,8],
    [2,3],
    [2,7],
    [7,3]
])

print(len(elementos))

from rigidez import cerchaGlobal

cerchaGlobal(math.pi,0,0,0)
mat2 = cerchaGlobal(math.pi,0,0,0)
print(matRigidez)