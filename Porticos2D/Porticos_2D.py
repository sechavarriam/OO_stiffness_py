# RAMA OSCAR

import numpy as np

def matriz_local(L, A, E, I):
    
    K11 = (4 * E * I) / L 
    K21 = (2 * E * I) / L
    K31 = (K11 + K21) / L
    K41 = -(K11 + K21) / L
    K51 = 0.0
    K61 = 0.0
    
    K12 = K21
    K22 = (4 * E * I) / L
    K32 = (K22 + K21) / L
    K42 = -(K22 + K21) / L
    K52 = 0.0
    K62 = 0.0
    
    K13 = K31
    K23 = K32
    K33 = (K11 + K22 + 2 * K21) / (L ** 2) 
    K43 = -(K11 + K22 + 2 * K21) / (L ** 2) 
    K53 = 0.0
    K63 = 0.0
    
    K14 = K41
    K24 = K42
    K34 = K43 
    K44 = (K11 + K22 + 2 * K21) / (L ** 2)
    K54 = 0.0
    K64 = 0.0
    
    K15 = K51
    K25 = K52
    K35 = K53 
    K45 = K54
    K55 = A * E / L 
    K65 = - A * E / L
    
    K16 = K61
    K26 = K62
    K36 = K63 
    K46 = K64
    K56 = K65 
    K66 = A * E / L
    
    k = [[K11, K21, K31, K41, K51, K61],[K12, K22, K32, K42, K52, K62],[K13, K23, K33, K43, K53, K63],
        [K14, K24, K34, K44, K54, K64],[K15, K25, K35, K45, K55, K65],[K16, K26, K36, K46, K56, K66]]
    
    matriz = np.matrix(np.round(k,2))
        
    return matriz

def matriz_T(CX, CY):
    
    T11 = 1.0 
    T21 = 0.0
    T31 = 0.0
    T41 = 0.0
    T51 = 0.0
    T61 = 0.0
    
    T12 = 0.0
    T22 = 1.0
    T32 = 0.0
    T42 = 0.0
    T52 = 0.0
    T62 = 0.0
    
    T13 = 0.0
    T23 = 0.0
    T33 = -1.0 * CY 
    T43 = 0.0 
    T53 = CX
    T63 = 0.0
    
    T14 = 0.0
    T24 = 0.0
    T34 = 0.0
    T44 = -1.0 * CY
    T54 = 0.0
    T64 = CX
    
    T15 = 0.0
    T25 = 0.0
    T35 = CX 
    T45 = 0.0
    T55 = CY 
    T65 = 0.0
    
    T16 = 0.0
    T26 = 0.0
    T36 = 0.0
    T46 = CX
    T56 = 0.0 
    T66 = CY
    
    T = [[T11, T21, T31, T41, T51, T61], [T12, T22, T32, T42, T52, T62], [T13, T23, T33, T43, T53, T63],
         [T14, T24, T34, T44, T54, T64], [T15, T25, T35, T45, T55, T65], [T16, T26, T36, T46, T56, T66]]
    
    matriz = np.matrix(np.round(T,4))
        
    return matriz




















