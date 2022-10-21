# == Header ==================================================
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

from clases import Node, ElementoPortico, Structure, Model
# ============================================================

# == Structure File ==========================================
# Cambiar struct1 por el archivo con la estructura.

#from structures import struct1 as data
from structures import awa as data
s = data.load_struct()

# ============================================================

m = Model(s)

m.add_node_force(5,[50, 0  ,   0])
m.add_node_force(5,[0 , 100, -25])


m.solve()

fig, ax = plt.subplots()
m.plot_deformed(ax,100)
plt.show()

#s.plot()
pass
import matplotlib.pyplot as plt
plt.spy(s.K, marker='.')
plt.show()