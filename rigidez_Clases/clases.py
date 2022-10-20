from ast import Pass
import math
import copy
from operator import index
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------
class Node:
    # indice propio de la clase. Cada vez que se llame el constructor para crear un
    # nodo nuevo, el índice se actualiza. Almacenará la cantidad de nodos creados.

    # Al ser un atributo de la clase no se pone "self"
    indice = 1 # 

    def __init__(self, x1, x2, restricciones=[0,0,0]) -> None:
        self.indice = Node.indice           # Indice propio del nodo creado. 
        self.x1 = x1                        # Coordenada 1.
        self.x2 = x2                        # Coordenada 2.
        self.restricciones = restricciones  # Arreglo de restricciones. [0,0,0] default

        self.n_DoF = 0 # Númreo de grados de libertad del nodo. Dependerá del modelo.
                       # Por ejemplo, en porticos planos n_DoF es 3, en cerchas planas es 2. 


        self.u = [] # Arreglo con desplazamientos del nodo. Se llenará dependiendo del 
                    # tipo de modelo a resolver. Su tamaño dependerá entonces de la 
                    # cantidad de grados de libertad del nodo en el modelo n_DoF.

        #TODO: Asignar para cada grado de libertad un índice en la posición global de la
        #      estructura. (self.DoF_Index = [])

        Node.indice += 1 # Suma uno al índice de la clase. 

    #__str__(self) -> str: es un método (función) de la clase que le dice a 
    # python qué mostrar cuando se hace print. En este caso mostrará las 
    # coordenadas del nodo.
    def __str__(self) -> str: 
        return "("+str(self.x1)+","+str(self.x2)+")" 


#---------------------------------------------------------------------------------
class MaterialIsotropicoLineal:
    def __init__(self, E) -> None:
        self.E = E

#---------------------------------------------------------------------------------
# Clase elemento genérico. Tiene los atributos generales a cualquie tipo de elemento sea 
# de volúmen, de área, o estructural tipo viga o pórtico. 
class Elemento:
    indice = 1
    def __init__(self, nodes) -> None:
        self.indice = Elemento.indice
        self.nodes = nodes
        Elemento.indice += 1
#---------------------------------------------------------------------------------
# Clase elemento pórtico:
# Utiliza "Herencia múltiple" ya que hereda todos los atributos y métodos de elemento y 
# de material isotrópico lineal.
class ElementoPortico(Elemento, MaterialIsotropicoLineal):

    # Constructor: Método para crear (construir, instanciar) Elementos pórtico. ==========
    def __init__(self, nodes, E, A, I) -> None:

        #Atributos creados por el constructor ==========
        self.L = 0 # Se inicializa de longitul L
        self.A = A
        self.I = I
        self.K = np.array(np.zeros([6,6]))
        # ===============================================

        # Se llama el constructor como un metodo de clase y se pasa self:
        # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
        Elemento.__init__(self,nodes)
        MaterialIsotropicoLineal.__init__(self,E)
        
        # Asignación de número de DoF por nodo. Evalúa si no se ha asignado.
        if self.nodes[0].n_DoF == 0: self.nodes[0].n_DoF = 3
        if self.nodes[1].n_DoF == 0: self.nodes[1].n_DoF = 3

        #TODO: Qué pasa si no es cero, pero tampoco 3? Puede pasar si se usan diferentes tipos
        #      De elemento. 

        self.calcularLongitud()
        self.K_porticoGlobal()

    # Fin del constructor =================================================================
    
    # Métodos adicionales propios de la clase. 

    # Cálculo de la longitud en términos de las coordenadas. Se usa en el constructor.
    def calcularLongitud(self):
        ni = self.nodes[0]
        nj = self.nodes[1]

        self.L = math.sqrt((nj.x1 - ni.x1)**2 + (nj.x2 - ni.x2)**2)
        self.theta = math.atan2((nj.x2 - ni.x2),(nj.x1 - ni.x1))

    # Cálculo de la matriz de rigidez del elemento en coordenadas globales. Se una en el constructor.
    def K_porticoGlobal(self):
        c = math.cos(self.theta) 
        s = math.sin(self.theta) 

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

        EAL = self.E*self.A/self.L
        EI= self.E*self.I

        l = self.L

        k = np.zeros([6,6])
        k = np.matrix(k)

        k[0,0] =  EAL
        k[0,3] = -EAL
        k[1,1] =  12 * EI/l**3
        k[1,2] =   6 * EI/l**2
        k[1,4] = -12 * EI/l**3
        k[1,5] =   6 * EI/l**2
        k[2,1] =   6 * EI/l**2
        k[2,2] =   4 * EI/l
        k[2,4] = - 6 * EI/l**2
        k[2,5] =   2 * EI/l
        k[3,0] = -EAL
        k[3,3] =  EAL
        k[4,1] = -12*EI/l**3
        k[4,2] = - 6*EI/l**2
        k[4,4] =  12*EI/l**3
        k[4,5] = - 6*EI/l**2
        k[5,1] =   6*EI/l**2
        k[5,2] =   2*EI/l
        k[5,4] = - 6*EI/l**2
        k[5,5] =   4*EI/l 

        self.K = np.transpose(T) * k * T

    def plot(self,ax):
        ni = self.nodes[0]
        nj = self.nodes[1]

        # Extracción de coordenadas nodo inicial
        xi = ni.x1
        yi = ni.x2

        # Extracción de coordenadas nodo final
        xj = nj.x1
        yj = nj.x2

        # Traza en el eje "ax" la línea del elemento. Se debe pasar el eje.
        ax.plot([xi, xj], [yi, yj], 'k-o') 
    
#---------------------------------------------------------------------------------

# Clase Sructure. 
class Structure:
    # Constructor. La estructura se crea en términos de la malla, es decir, una lista de nodos
    # y una lista de elementos.

    def __init__(self ,nodos, elementos) -> None:
        self.nodes = nodos
        self.elementos = elementos

        n_DoF = 3*len(nodos) # Número de grados de libertad totales de la estructura.
                             # En este caso está definido para pórticos planos únicamente.

        self.n_DoF = n_DoF

        self.K    = np.array(np.zeros([n_DoF, n_DoF]))
        self.resV = np.array(np.zeros([n_DoF,1])) # Vector de restricciones.

        self.extraerRestricciones()
        self.ensambleK()
        #self.extraer_subK() #Se deja para que lo haga el modelo.

    def ensambleK(self):
        for elem in self.elementos: 
            ni = elem.nodes[0].indice - 1 # índice de nodo inicial
            nj = elem.nodes[1].indice - 1 # Índice de nodo final

            inicialI = 3*ni
            finalI = 3*ni + 2

            inicialJ = 3*nj
            finalJ = 3*nj + 2

            self.K[inicialI:finalI+1,inicialI:finalI+1] += elem.K[0:3,0:3]
            self.K[inicialJ:finalJ+1,inicialJ:finalJ+1] += elem.K[3:6,3:6]

            self.K[inicialI:finalI+1,inicialJ:finalJ+1] += elem.K[0:3,3:6]
            self.K[inicialJ:finalJ+1,inicialI:finalI+1] += elem.K[3:6,0:3]


    # Con el siguiente método no es necesario introducir las restricciones en el constructor
    # de la estructura. La idea es extraer las restricciones desde los atributos de los nodos.
    def extraerRestricciones(self):
        resMat = [] # Inicialización de la matriz de restricciones.

        for n in self.nodes: # Se podría simplificar usando list comprehension.
            resMat.append(n.restricciones)

        resMat =np.array(resMat) # Convierte en array de python.

        self.resV = resMat.flatten() # Convierte matriz en lista.

        self.rest_index = np.where(self.resV != 0)[0] # Índices de DoF restringidos (apoyos)
        self.free_index = np.where(self.resV == 0)[0] # Índices de DOF libres.


    # El siguiente método extrae, de la matriz global, las submatrices necesarias para el análisis
    # elástico lineal estático.
    def extraer_subK(self):

        Knn = [[self.K[i][j] for j in self.free_index] for i in self.free_index]
        Kaa = [[self.K[i][j] for j in self.rest_index] for i in self.rest_index]
        Kan = [[self.K[i][j] for j in self.rest_index] for i in self.free_index]
        Kna = [[self.K[i][j] for j in self.free_index] for i in self.rest_index]

        self.Knn = np.array(Knn)
        self.Kaa = np.array(Kaa)
        self.Kan = np.array(Kan)
        self.Kna = np.array(Kna) 

    def plot(self,ax):
        for e in self.elementos:
            e.plot(ax)

        ax.set_aspect('equal', 'box')

#---------------------------------------------------------------------------------

# Clase Model (static)

class Model:
    def __init__(self ,struct) -> None:
        self.S = struct
        self.F = np.array(np.zeros([self.S.n_DoF])) #Vector de fuerzas.
        self.u = np.array(np.zeros([self.S.n_DoF])) #Vector de desplazamientos 

    def add_node_displacement(self, node_index, displacement): 
        # displacement = [u,v,theta]
        pos_1 = 3*(node_index-1)
        pos_2 = 3*(node_index-1)+2

        self.F[pos_1:pos_2+1] += displacement[0:3]


    def add_node_force(self, node_index, force): 
        # force = [Fx,Fy,M]
        pos_1 = 3*(node_index-1)
        pos_2 = 3*(node_index-1)+2

        self.F[pos_1:pos_2+1] += force[0:3]

    def extraer_Fn(self): #Extracción de vector de fuerzas para DoF libres.
        self.Fn = [self.F[index] for index in self.S.free_index]

    def extraer_ua(self): #Extracción de vector de desplazamientos impuestos (apoyos).
        self.ua = [self.u[index] for index in self.S.rest_index]


    def set_displacements(self): 
        #Ensambla el vector total de desplaamientos en términos de un y ua.
        for i, index in enumerate(self.S.free_index):
            self.u[index] = self.un[i]

        for i, index in enumerate(self.S.rest_index):
            self.u[index] = self.ua[i]

        #A cada nodo se le asigna su correspondiente desplazamiento en términos del vector u.
        for i, node in enumerate(self.S.nodes):

            for j in range(node.n_DoF):
                node.u.append(self.u[3*i+j])

            #node.u.append(self.u[3*i])
            #node.u.append(self.u[3*i+1])
            #node.u.append(self.u[3*i+2])


    def solve(self):        
        self.extraer_Fn()
        self.extraer_ua()
        self.S.extraer_subK() # Extrae matrices Knn de la estructura.

        # Cálculo de los desplazamientos.
        self.un = np.linalg.solve(self.S.Knn , self.Fn - np.matmul(self.S.Kan, self.ua))

        # Cálculo de las reacciones.
        self.Fa = np.matmul(self.S.Kna, self.un) + np.matmul(self.S.Kaa, self.ua)

        # Ensamble del vector total de desplazamientos.
        self.set_displacements()


    def plot_deformed(self,ax,ampFactor): 
        S_updated = copy.deepcopy(self.S)  #Create a new structure to modify his nodes. (copy)
        
        for n in S_updated.nodes:
            n.x1 += ampFactor*n.u[0] # Se aplifican los desplazamientos para que sean visibles.
            n.x2 += ampFactor*n.u[1] 
            
        self.S.plot(ax)
        S_updated.plot(ax)









## ========================================================================================
## ========================================================================================

