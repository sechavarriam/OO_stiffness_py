# == Header ==================================================
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

import MemberEndForces as MEF

from clases import Node, ElementoPortico, Structure, Model
# ============================================================

# == Structure File ==========================================
# Cambiar struct1 por el archivo con la estructura.

from structures import struct1 as data
#from structures import awa as data
s = data.load_struct()

# ============================================================

m = Model(s)

m.add_node_force(5,[50, 0  ,   0])
m.add_node_force(5,[0 , 100, -25])

m.add_element_force(1, MEF.UniformGravity(m.S.elementos[1].L, -24))


m.solve()


print(m.Fn)
print(m.FEn)

print(m.Fn-m.FEn)

print(m.FEa)


fig, ax = plt.subplots()
m.plot_deformed(ax,180)


#plt.spy(s.K, marker='.')


plt.show()