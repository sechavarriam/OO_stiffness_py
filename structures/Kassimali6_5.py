import math
import numpy as np

from clases import Node, ElementoPortico, Structure

def load_struct():

    E=200e6    #[GPa]
    A=4740e-6  #[mm^2]
    I=22.2e-6  #[mm^4]

    n1 = Node( [0, 0 ],[1,1,1])
    n2 = Node( [0,10 ],[1,0,0])
    n3 = Node( [8,10 ],[1,1,1])

    e1 = ElementoPortico([n1,n2],E,A,I)
    e2 = ElementoPortico([n2,n3],E,A,I)

    s = Structure([n1,n2,n3],[e1,e2])

    return(s)