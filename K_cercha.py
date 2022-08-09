import math
import numpy as np

# Definición de función
def K_cerchaGlobal(angulo, moduloE, area, longitud):
    c = math.cos(angulo)
    s = math.sin(angulo)

    T = np.zeros([4,4])
    T = np.matrix(T)
    

    T[0,0] = c
    T[0,1] = s
    T[1,0] = -s
    T[1,1] = c
    T[2,2] = c
    T[2,3] = s
    T[3,2] = -s
    T[3,3] = c 

    EAL = moduloE*area/longitud

    k = np.zeros([4,4])
    k = np.matrix(k)

    k[0,0] = EAL
    k[0,2] = -EAL
    k[2,2] = EAL
    k[2,0] = -EAL

    K = np.transpose(T) * k * T
    #print(K)
    return K