# RAMA OSCAR

import numpy as np

def matriz_local(L, A, E, I):
    
    K11 = (E * A) / L 
    K21 = 0.0
    K31 = 0.0
    K41 = - (E * A) / L
    K51 = 0.0
    K61 = 0.0
    
    K12 = 0.0
    K22 = (12 * E * I) / (L ** 3) 
    K32 = (6 * E * I) / (L ** 2) 
    K42 = 0.0
    K52 = -(12 * E * I) / (L ** 3)
    K62 = (6 * E * I) / (L ** 2) 
    
    K13 = 0.0
    K23 = (6 * E * I) / (L ** 2)
    K33 = (4 * E * I) / L 
    K43 = 0.0
    K53 = -(6 * E * I) / (L ** 2)
    K63 = (2 * E * I) / L
    
    K14 = -(E * A) / L
    K24 = 0.0
    K34 = 0.0 
    K44 = (E * A) / L
    K54 = 0.0
    K64 = 0.0
    
    K15 = 0.0
    K25 = -(12 * E * I) / (L ** 3)
    K35 = -(6 * E * I) / (L ** 2) 
    K45 = 0.0
    K55 = (12 * E * I) / (L ** 3)
    K65 = -(6 * E * I) / (L ** 2) 
    
    K16 = 0.0
    K26 = (6 * E * I) / (L ** 2)
    K36 = (2 * E * I) / (L ** 2) 
    K46 = 0.0
    K56 = -(6 * E * I) / (L ** 2)
    K66 = (3 * E * I) / (L ** 2)
    
    k = [[K11, K21, K31, K41, K51, K61],[K12, K22, K32, K42, K52, K62],[K13, K23, K33, K43, K53, K63],
        [K14, K24, K34, K44, K54, K64],[K15, K25, K35, K45, K55, K65],[K16, K26, K36, K46, K56, K66]]
    
    matriz = np.matrix(np.round(k,2))
        
    return matriz

def matriz_T(CX, CY):
    
    T11 = CX 
    T21 = -CY
    T31 = 0.0
    T41 = 0.0
    T51 = 0.0
    T61 = 0.0
    
    T12 = CY
    T22 = CX
    T32 = 0.0
    T42 = 0.0
    T52 = 0.0
    T62 = 0.0
    
    T13 = 0.0
    T23 = 0.0
    T33 = 1.0
    T43 = 0.0 
    T53 = 0.0
    T63 = 0.0
    
    T14 = 0.0
    T24 = 0.0
    T34 = 0.0
    T44 = CX
    T54 = -CY
    T64 = 0.0
    
    T15 = 0.0
    T25 = 0.0
    T35 = 0.0
    T45 = CY
    T55 = CX 
    T65 = 0.0
    
    T16 = 0.0
    T26 = 0.0
    T36 = 0.0
    T46 = 0.0
    T56 = 0.0 
    T66 = 1.0
    
    T = [[T11, T21, T31, T41, T51, T61], [T12, T22, T32, T42, T52, T62], [T13, T23, T33, T43, T53, T63],
         [T14, T24, T34, T44, T54, T64], [T15, T25, T35, T45, T55, T65], [T16, T26, T36, T46, T56, T66]]
    
    matriz = np.matrix(np.round(T,4))
        
    return matriz
