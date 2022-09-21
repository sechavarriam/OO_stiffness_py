from clases import Nodo, ElementoPortico

E=2e8
A=0.2*0.5
I=0.2*(0.5**3)/12

n1 = Nodo(0.2, 0.3)
n2 = Nodo(0.4, 0.3)

print(n1.x1)
print(n2.indice)

elPortico = ElementoPortico([n1,n2],E,A,I)

elPortico.calcularLongitud()
elPortico.K_porticoGlobal()
print(elPortico.K)
