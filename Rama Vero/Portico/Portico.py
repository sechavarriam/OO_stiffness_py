import numpy as np
import math #Importa la librería math de python para poder usar las funciones matemáticas usuales.
from K_Portico import K_PorticoGlobal

# DATOS SECCIÓN
E = 2.5e7      #[kPa] 
A = 0.3*0.3  #[m]^2
I = 0.000675    #m4 

# Creación de arreglo de nodos. =================================================

nodos = np.array([
    [0,0],
    [3,4],
    [6,4],
    [8,1],
])

# Booleano que indica qué grado de libertad está restringido por nodo.
restricciones = np.array([
    [1,1,0],
    [0,0,0],
    [0,0,0],
    [1,1,0],
])

# https://www.geeksforgeeks.org/flatten-a-matrix-in-python-using-numpy/
rest_DoF = restricciones.flatten()
print(rest_DoF)


# https://stackoverflow.com/questions/4588628/find-indices-of-elements-equal-to-zero-in-a-numpy-array
rest_index = np.where(rest_DoF != 0)[0]
free_index = np.where(rest_DoF == 0)[0]

#print(np.where(rest_DoF != 0))
#print(rest_index)
#print(free_index)


# Creación de arreglo con conectividades de los elementos. Es un arreglo de listas que para cada elemento
# contiene una lista con el índice del nodo inicial y del nodo final en orden.
elementos = np.array([
    [0,1],
    [1,2],
    [2,3],
])

# Cálculo de número de nodos y de elementos en términos de las listas de entrada.
n_nodos = len(nodos)
n_elem  = len(elementos)

DoF = n_nodos*3 # Número de grados de libertad totales para toda la estructura

#print(len(elementos)) # Imprime la longitud de los elementos.
# ======================================================================================================

theta = [] #Lista que almacenará la inclinación de cada elemento
L = [] # Lista que almacenará la longitud de cada elemento

# -------------------------------------------------------------------------------------------------
# NOTA:
# Las siguientes listas no se necesitan puesto que todos los elementos de este ejemplo
# son del mismo material y tienen la misma sección.
# En el caso genérico, de sección y material variables, esas listas deben ser un dato de entrada.
#  
# A = []
# E = []
# -------------------------------------------------------------------------------------------------

K_elem = [] #Lista que almacenará las matrices globales de cada elemento.


i = 0
for elem in elementos:
    
    ni = elem[0] # índice de nodo inicial
    nj = elem[1] # Índice de nodo final

    # Extracción de coordenadas nodo inicial
    xi = nodos[ni][0]
    yi = nodos[ni][1]

    # Extracción de coordenadas nodo final
    xj = nodos[nj][0]
    yj = nodos[nj][1] 

    theta.append(math.atan2(yj-yi,xj-xi))      # Pone el valor calculado del ángulo al final de la lista.
    L.append(math.sqrt((xj-xi)**2+(yj-yi)**2)) # Pone el valor calculado de la longitud al final de la lista.

    K_elem.append(K_PorticoGlobal(theta[i], E, I, A, L[i])) #Cálculo y almacenamiento de matriz de rigidez global por elemento.
    
    i=i+1

# ------- Gráfica de la malla --------------
from plot_Frame2D import plot_2D_Frame
plot_2D_Frame(nodos, elementos)
# ------------------------------------------

## ========================================================================================
## ========================================================================================
## ============== Ensamble de la matriz global de la estructura. ========================== 
## ========================================================================================
## ========================================================================================

K = np.zeros([DoF,DoF]) #Inicialización de la matriz de rigidez global de la estructura.

# https://realpython.com/python-enumerate/
# When you use enumerate(), the function gives you back two loop variables:
#   1. The count of the current iteration (i)
#   2. The value of the item at the current iteration (elem)

for e, elem in enumerate(elementos): 

    ni = elem[0] # índice de nodo inicial
    nj = elem[1] # Índice de nodo final

    # Extracción de coordenadas
    xi = nodos[ni][0]
    yi = nodos[ni][1]

    xj = nodos[nj][0]
    yj = nodos[nj][1]

    inicialI = 3*ni
    medioI = 3*ni + 1
    finalI = 3*ni + 2

    inicialJ = 3*nj
    medioJ = 3*nj + 1
    finalJ = 3*nj + 2

    K[inicialI:finalI+1,inicialI:finalI+1] = K[inicialI:finalI+1,inicialI:finalI+1] +  K_elem[e][0:3,0:3]
    K[inicialJ:finalJ+1,inicialJ:finalJ+1] += K_elem[e][3:6,3:6]

    K[inicialI:finalI+1,inicialJ:finalJ+1] += K_elem[e][0:3,3:6]
    K[inicialJ:finalJ+1,inicialI:finalI+1] += K_elem[e][3:6,0:3]

print(K)
## ========================================================================================

Knn = [[K[i][j] for j in free_index] for i in free_index]
Kaa = [[K[i][j] for j in rest_index] for i in rest_index]
Kan = [[K[i][j] for j in free_index] for i in rest_index]

Knn = np.matrix(Knn)
Kaa = np.matrix(Kaa)
Kan = np.matrix(Kan)
Kna = Kan.transpose()

# Vector de fuerzas puntuales aplicadas en los nodos (Fp)
Fp = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

Fp = Fp.flatten()
Fp = [Fp[i] for i in free_index]
F = np.transpose(np.matrix(Fp))

#Vector de fuerzaa en los elementos
L=np.array(L)

#Carga_elem =[w1,w2,l1,l2]
Carga_elem = np.array([
    [0,0,0,0],
    [40,40,0,0],
    [0,0,0,0]
    ])

#Longitud de cada elemnto 
for e, elem in enumerate(elementos):
    Li=L[e]
    
efe=[]
Fo=np.zeros(3*len(nodos))
enumerate(elementos)
for e, elem in enumerate(elementos): 
    Li = L[e] #Longitud del elemento e
    w1 = Carga_elem[e][0]
    w2 = Carga_elem[e][1]
    l1 = Carga_elem[e][2]
    l2 = Carga_elem[e][3]
    FSi = w1*(Li-l1)**3/(20*Li**3)*((7*Li+8*l1)-(l2*(3*Li+2)/(Li-l1))*(1+l2/(Li-l1)+l2**2/(Li-l1)**2)+2*l2**4/(Li-l1)**3)+w2*(Li-l1)**3/(20*Li**3)*((3*Li+2*l1)*(1+l2/(Li-l1)+l2**2/(Li-l1)**2)-l2**3/(Li-l1)**2*(2+(15*Li-8*l2)/(Li-l1)))
    FMi = w1*(Li-l1)**3/(60*Li**2)*(3*(Li+4*l1)-(l2*(2*Li+2*l1)/(Li-l1)*(1+l2/(Li-l1)+l2**2/(Li-l1)**2)+3*l2**4/(Li-l1)**3))+w2*(Li-l1)**3/(60*Li**2)*((2*Li+3*l1)*(1+l2/(Li-l1)+l2**2/(Li-l1)**2)-3*l2**3/(Li-l1)**2*(1+(5*Li-4*l2)/(Li-l1)))
    FSj = ((w1+w2)/2)*(Li-l1-l2)-FSi   
    FMj = ((Li-l1-l2)/6)*(w1*(-2*Li+2*l1-l2)-w2*(Li-l1+2*l2))+FSi*Li-FMi                                                                                                                                
    MEPi=[0,FSi,FMi,0,FSj,FMj]
    efe.append(MEPi)
    Fefe=np.array(efe)
    
    ni = elem[0] # índice de nodo inicial
    nj = elem[1] # Índice de nodo final

    inicialI = 3*ni
    finalI = 3*ni + 2

    inicialJ = 3*nj
    finalJ = 3*nj + 2
    
    Fo[inicialI:finalI+1] += np.transpose(Fefe[e][0:3])
    Fo[inicialJ:finalJ+1] += np.transpose(Fefe[e][3:6])
    Foo = [Fo[i] for i in free_index]
    Ff = np.transpose(np.matrix(Foo))
    Fz = [Fo[j] for j in rest_index]

Fn = F - Ff

#Desplazamientos desconocidos
dn = Knn**(-1)*Fn  

#Fuerzas conocidas 
Fa = Kan*dn
print(Fa)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.spy(K, marker='o')
plt.show()

