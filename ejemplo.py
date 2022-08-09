import numpy as np

# Variables auxiliares para creación de la malla
r1 = 1
r2 = 1.2

t0 = 0
t1 = 30
t2 = 45
t3 = 60
t4 = 90



# Creación de arreglo de nodos en coordenadas polares.

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

print(nodosPolares)

import math #Importa la librería math de python para poder usar las funciones matemáticas usuales.

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


# La estructura de control del ciclo se interrumpe cuando el codigo se devuelve en la identación.
nodos = np.array(nodos) # Convierte la lista de listas en un arreglo de numpy.

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

print(len(elementos)) # Imprime la longitud de los elementos.

from rigidez import cerchaGlobal

#cerchaGlobal(math.pi,0,0,0)
#mat2 = cerchaGlobal(math.pi,0,0,0)
#print(matRigidez)