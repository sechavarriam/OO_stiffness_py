import numpy as np
import math #Importa la librería math de python para poder usar las funciones matemáticas usuales.
from K_cercha import K_cerchaGlobal
# Lo ideal es que las importaciones vayan al principio del archivo (o en un archivo aparte).

# DATOS SECCIÓN
E = 210e6      #[kPa] = 200 [GPa]
A = 0.05*0.02  #[m]^2

# Variables auxiliares para creación de la malla
r1 = 1.0
r2 = 1.2

t0 = 0
t1 = 90/4
t2 = 45
t3 = 3*90/4
t4 = 90

# Creación de arreglo de nodos en coordenadas polares. =================================================

# Es un arreglo de la libraria numpy donde cada entrada es una lista de python.

# Las listas en python son secuencias ordenadas de objetos, en este caso van a almacenar para cada nodo
# la coordenada radial y angular.
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


## Ejemplo de sintaxis MATLAB para cración de matriz
# nodosP_MATLAB = [r1, t4; r2, t3; ... ; r2, t0]'

# ======================================================================================================

# Creación de lista vacía dónde se almacenarán las coordenadas de los nodos en coordenadas cartesianas.
# Lo usual es que una estructura se describa directamente en este sistema coordenado.
nodos = []

for nodo in nodosPolares:  #Recorre cada entrada del arreglo, es decir, lista a lista.
    # NOTA: Esta no es la única forma de recorrer un ciclo for. 

    x = nodo[0]*math.cos(nodo[1]*math.pi/180) # Cambio de coordenadas
    y = nodo[0]*math.sin(nodo[1]*math.pi/180) #
    
    c = [x,y] # Creación de nueva lista con coordenadas cartesianas.
    
    nodos.append(c) # Agrega la lista "c" al final de la lista "nodos"
    # En cada paso se va agregando la pareja de coordenadas nueva al final.
    
    print("[{:.2f},{:.2f}]".format(c[0],c[1])) #Impresión en consola con formato.
    # Vea por ejemplo: https://www.geeksforgeeks.org/python-string-format-method/


# ======================================================================================================
# La estructura de control del ciclo se interrumpe cuando el codigo se devuelve en la identación.
nodos = np.array(nodos) # Convierte la lista de listas en un arreglo de numpy.

# Booleano que indica qué grado de libertad está restringido por nodo.
restricciones = np.array([
    [1,1],
    [0,0],
    [0,0],
    [0,0],
    [1,1],
    [1,0],
    [0,0],
    [0,0],
    [0,0],
    [1,0]
])

# https://www.geeksforgeeks.org/flatten-a-matrix-in-python-using-numpy/
rest_DoF = restricciones.flatten()
print(rest_DoF)

#rest_index = np.argwhere(rest_DoF)
#print(rest_index)
#
#rest_index = np.nonzero(rest_DoF)
#print(rest_index)
#
#rest_index = np.flatnonzero(rest_DoF)
#print(rest_index)
#

# https://stackoverflow.com/questions/4588628/find-indices-of-elements-equal-to-zero-in-a-numpy-array
rest_index = np.where(rest_DoF != 0)[0]
free_index = np.where(rest_DoF == 0)[0]

print(np.where(rest_DoF != 0))
#print(rest_index)
#print(free_index)


# Creación de arreglo con conectividades de los elementos. Es un arreglo de listas que para cada elemento
# contiene una lista con el índice del nodo inicial y del nodo final en orden.
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

# Cálculo de número de nodos y de elementos en términos de las listas de entrada.
n_nodos = len(nodos)
n_elem  = len(elementos)

DoF = n_nodos*2 # Número de grados de libertad totales para toda la estructura

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

    # Corrección de índice. Los arreglos en python inician en 0
    ni = ni - 1
    nj = nj - 1

    # Extracción de coordenadas nodo inicial
    xi = nodos[ni][0]
    yi = nodos[ni][1]

    # Extracción de coordenadas nodo final
    xj = nodos[nj][0]
    yj = nodos[nj][1] 

    theta.append(math.atan2(yj-yi,xj-xi))      # Pone el valor calculado del ángulo al final de la lista.
    L.append(math.sqrt((xj-xi)**2+(yj-yi)**2)) # Pone el valor calculado de la longitud al final de la lista.

    K_elem.append(K_cerchaGlobal(theta[i], E, A, L[i])) #Cálculo y almacenamiento de matriz de rigidez global por elemento.
    
    i=i+1

# ------- Gráfica de la malla --------------
from plot_Struct1D import plot_2D_Truss
plot_2D_Truss(nodos, elementos)
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

    # Corrección de índice. Los arreglos en python inician en 0
    ni = ni - 1
    nj = nj - 1

    # Extracción de coordenadas
    xi = nodos[ni][0]
    yi = nodos[ni][1]

    xj = nodos[nj][0]
    yj = nodos[nj][1]

    inicialI = 2*ni
    finalI = 2*ni + 1

    inicialJ = 2*nj
    finalJ = 2*nj + 1

    K[inicialI:finalI+1,inicialI:finalI+1] = K[inicialI:finalI+1,inicialI:finalI+1] +  K_elem[e][0:2,0:2]
    K[inicialJ:finalJ+1,inicialJ:finalJ+1] += K_elem[e][2:4,2:4]

    K[inicialI:finalI+1,inicialJ:finalJ+1] += K_elem[e][0:2,2:4]
    K[inicialJ:finalJ+1,inicialI:finalI+1] += K_elem[e][2:4,0:2]

print(K)
## ========================================================================================
## ========================================================================================


#print(K_elem[0])
#print(K_elem[0][0:2,0:2])

K[0:2,0:2] = K_elem[0][0:2,0:2]
K[3:5,3:5] = K_elem[0][0:2,0:2]


# List comprehension 
# https://www.geeksforgeeks.org/python-list-comprehension/

Knn = [[K[i][j] for j in free_index] for i in free_index]
Kaa = [[K[i][j] for j in rest_index] for i in rest_index]
Kan = [[K[i][j] for j in rest_index] for i in free_index]



Knn = np.matrix(Knn)
Kaa = np.matrix(Kaa)
Kan = np.matrix(Kan)
Kna = Kan.transpose()


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.spy(K, marker='o')
plt.show()


# https://stackoverflow.com/questions/29102955/how-to-print-numpy-objects-without-line-breaks
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

#print(np.round(Knn,0))
#print(np.round(Kaa,0))