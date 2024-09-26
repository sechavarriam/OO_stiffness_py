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

#from structures import struct1 as data
#from structures import awa as data
from structures import Kassimali6_5 as data
s = data.load_struct()

# ============================================================

m = Model(s)

#m.add_node_force(5,[50, 0  ,   0])
#m.add_node_force(5,[0 , 100, -25])

#m.add_element_force(0, MEF.UniformGravity(24, m.S.elementos[0].L))

m.add_element_force(0, MEF.UniformGravity  (24,10))
m.add_element_force(1, MEF.ConcentratedLoad(75,4,8))

m.solve()


print(m.Fn)
print(m.FEn)

print(m.Fn-m.FEn)

print(m.FEa)


fig, ax = plt.subplots()
m.plot_deformed(ax,1000)


#plt.spy(s.K, marker='.')


plt.show()