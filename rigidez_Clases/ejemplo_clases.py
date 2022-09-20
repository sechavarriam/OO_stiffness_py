from clases import Nodo, ElementoPortico

n1 = Nodo(0.2, 0.3)
n2 = Nodo(0.4, 0.3)

print(n1.x1)
print(n2.indice)

E=2e8
A=0.2*0.5
I=0.2*(0.5**3)/12


#listaNodos = []
#
#with open('archivoEstructura.txt', 'r') as archivo:
#    linea = archivo.readline()
#    while linea != "":
#        datos = linea.split()
#        x1 = float(datos[0])
#        x2 = float(datos[1])
#
#        n = Nodo(x1,x2)
#        listaNodos.append(n)
#        print(n)



elPortico = ElementoPortico([n1,n2],E,A,I)
elPortico.calcularLongitud()
elPortico.K_porticoGlobal()
print(elPortico.K)
