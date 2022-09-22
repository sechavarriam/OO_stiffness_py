from clases import Nodo, ElementoPortico, Structure

E=2e8
A=0.2*0.5
I=0.2*(0.5**3)/12

n1 = Nodo(0.2, 0.3)
n2 = Nodo(0.4, 0.3, [0,1,0])

print(n1.x1)
print(n2.indice)

daniela = ElementoPortico([n1,n2],E,A,I)

daniela.A
daniela.E
daniela.I

daniela.calcularLongitud()
daniela.K_porticoGlobal()

#print(daniela.K)
Nodo.indice = 1

n1 = Nodo( 1, 0 ,[1,1,1])
n2 = Nodo( 3, 0 ,[1,0,0])
n3 = Nodo( 6, 0 ,[1,1,1])
n4 = Nodo( 1, 9 ,[0,0,0])
n5 = Nodo( 3, 9 ,[0,0,0])
n6 = Nodo( 6, 9 ,[0,0,0])
n7 = Nodo( 3, 15,[0,0,0])
n8 = Nodo( 6, 15,[1,1,0])

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

#s.plot()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.spy(s.K, marker='o')
plt.show()