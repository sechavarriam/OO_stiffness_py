import math
import numpy as np
import matplotlib.pyplot as plt

from clases import Node, ElementoPortico, Structure, Model

E=2e8
A=0.2*0.5
I=0.2*(0.5**3)/12

n1 = Node( [1, 0 ],[1,1,1])
n2 = Node( [3, 0 ],[1,0,0])
n3 = Node( [6, 0 ],[1,1,1])
n4 = Node( [1, 9 ],[0,0,0])
n5 = Node( [3, 9 ],[0,0,0])
n6 = Node( [6, 9 ],[0,0,0])
n7 = Node( [3, 15],[0,0,0])
n8 = Node( [6, 15],[0,0,0])

e1 = ElementoPortico([n1,n4],E,A,I)
e2 = ElementoPortico([n2,n5],E,A,I)
e3 = ElementoPortico([n3,n5],E,A,I)
e4 = ElementoPortico([n3,n6],E,A,I)
e5 = ElementoPortico([n5,n7],E,A,I)
e6 = ElementoPortico([n6,n8],E,A,I)
e7 = ElementoPortico([n4,n5],E,A,I)
e8 = ElementoPortico([n5,n6],E,A,I)
e9 = ElementoPortico([n7,n8],E,A,I)

s = Structure([n1,n2,n3,n4,n5,n6,n7,n8],[e1,e2,e3,e4,e5,e6,e7,e8,e9])
m = Model(s)

m.add_node_force(5,[50, 0, 0])
m.solve()

fig, ax = plt.subplots()
m.plot_deformed(ax,1000)
plt.show()

#s.plot()
pass
#import matplotlib.pyplot as plt
#plt.spy(s.Knn, marker='o')
#plt.show()