import math
import numpy as np

# Definición de función para la matriz de rigidez del portico
def K_porticoGlobal(angulo, moduloE, inercia, area, longitud):
    c = math.cos(angulo)  #lambda
    s = math.sin(angulo)  #miu

    T = np.zeros([6,6])
    T = np.matrix(T)
    

    T[0,0] = c
    T[0,1] = s
    T[1,0] = -s
    T[1,1] = c
    T[2,2] = 1
    T[3,3] = c
    T[3,4] = s
    T[4,3] = -s
    T[4,4] = c
    T[5,5] = 1

    EAL = moduloE*area/longitud
    EI= moduloE*inercia

    k = np.zeros([6,6])
    k = np.matrix(k)

    k[0,0] = EAL
    k[0,3] = -EAL
    k[1,1] = 12*EI/longitud**3
    k[1,2] = 6 * EI / longitud ** 2
    k[1,4] = -12 * EI / longitud ** 3
    k[1,5] = 6 * EI / longitud ** 2
    k[2,1] = 6 * EI / longitud ** 2
    k[2,2] = 4 * EI / longitud
    k[2,4] = -6 * EI / longitud ** 2
    k[2,5] = 2 * EI / longitud
    k[3,0] = -EAL
    k[3,3] = EAL
    k[4,1] = -12 * EI / longitud ** 3
    k[4,2] = -6 * EI / longitud ** 2
    k[4,4] = 12 * EI / longitud ** 3
    k[4,5] = -6 * EI / longitud ** 2
    k[5,1] = 6 * EI / longitud ** 2
    k[5,2] = 2 * EI / longitud
    k[5,4] = -6 * EI / longitud ** 2
    k[5,5] = 4 * EI / longitud

    K = np.transpose(T) * k * T
    #print(K)
    return K