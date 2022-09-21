import math
import numpy as np

#---------------------------------------------------------------------------------
class Nodo:
    indice = 1
    def __init__(self, x1, x2):
        self.indice = Nodo.indice
        self.x1 = x1
        self.x2 = x2
        Nodo.indice += 1 
    
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
class Elemento:
    indice = 1
    def __init__(self, nodos) -> None:
        self.indice = Elemento.indice
        self.nodos = nodos
        Elemento.indice += 1
#---------------------------------------------------------------------------------
class ElementoPortico(Elemento, MaterialIsotropicoLineal):
    def __init__(self, nodos, E, A, I) -> None:
        self.L = 0
        self.A = A
        self.I = I
        self.K = np.matrix(np.zeros([6,6]))
        # Se llama el constructor como un metodo de clase y se pasa self:
        # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
        Elemento.__init__(self,nodos)
        MaterialIsotropicoLineal.__init__(self,E)

    def calcularLongitud(self):
        ni = self.nodos[0]
        nj = self.nodos[1]

        self.L = math.sqrt((nj.x1 - ni.x1)**2 + (nj.x2 - ni.x2)**2)
        self.theta = math.atan2((nj.x2 - ni.x2),(nj.x1 - ni.x1))

    def T(self):
        pass    

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
#---------------------------------------------------------------------------------
