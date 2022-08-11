## Función para graficar estructura con elementos 1-dimesionales (e.g. cerchas, pórticos)
import matplotlib.pyplot as plt

def plot_2D_Truss(nodos, elementos):
    n_nodos = len(nodos)
    n_elem  = len(elementos)

    fig, ax = plt.subplots()
    # https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python

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

        ax.plot([xi, xj], [yi, yj], 'k-o') 
        # https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
        
        ax.set_aspect('equal', 'box')

    plt.show()

    #return 0







