# Ejemplo de modelo OpenSeesPy

# Importa la librería de OpenSeesPy
import openseespy.opensees as ops

# Las siguientes son las dos diferentes librerias para graficar resultados de OpenSees

import vfo.vfo as vfo
import opsvis as opsv
import matplotlib.pyplot as plt

import math

ops.wipe()

ops.model('basic', '-ndm', 3, '-ndf', 6)

#Variables auxiliares

l1 = 5 #[m]
l2 = 6 #[m]
l3 = 7 #[m]

h1 = 4.5 #[m]
h2 = 3.5 #[m]

#Sección
b = 0.50 #[m]
h = 0.50 #[m]

A = b*h #[m]²

Iz = (b*h**3)/12 #[m]⁴
Iy = (h*b**3)/12 #[m]⁴

aa = max(b,h)
bb = min(b,h)

Jxx = aa*bb**3 * (1/3 - (0.21*bb/aa)*(1-bb**4/(12*aa*4)))

poiss = 0.3
E = 4700*math.sqrt(28) #[kPa]
G = E/(2*(1+poiss))

# Definición de nodos

ops.node(1 , 0., 0.   ,0.)
ops.node(2 , l1, 0.   ,0.)
ops.node(3 , l1, l2   ,0.)
ops.node(4 , l1, l2+l3,0.)
ops.node(5 , 0., l2+l3,0.)
ops.node(6 , 0., l2   ,0.)

ops.node(7 , 0., 0.   ,h1)
ops.node(8 , l1, 0.   ,h1)
ops.node(9 , l1, l2   ,h1)
ops.node(10, l1, l2+l3,h1)
ops.node(11, 0., l2+l3,h1)
ops.node(12, 0., l2   ,h1)

ops.node(13, l1, l2   ,h1+h2)
ops.node(14, l1, l2+l3,h1+h2)
ops.node(15, 0., l2+l3,h1+h2)
ops.node(16, 0., l2   ,h1+h2)

# Definición de secciones ======================================================================================================

rectSec1_TAG = 1
ops.section('Elastic', rectSec1_TAG, E, A, Iz, Iy, G, Jxx)

# Definición de elementos ======================================================================================================
#ops.element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, <'-mass', mass>, <'-cMass'>)

column_TAG = 1
xBeam_TAG  = 2
yBeam_TAG  = 3

ops.geomTransf('Linear', column_TAG, -1, 0,0)
ops.geomTransf('Linear', yBeam_TAG ,  1, 0,0)
ops.geomTransf('Linear', xBeam_TAG ,  0,-1,0)

# Columnas primer nivel (definición directa sin sección)
#ops.element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)
ops.element('elasticBeamColumn',1, 1, 7 , A, E, G, Jxx, Iy, Iz, column_TAG)
ops.element('elasticBeamColumn',2, 2, 8 , A, E, G, Jxx, Iy, Iz, column_TAG)
ops.element('elasticBeamColumn',3, 6, 12, A, E, G, Jxx, Iy, Iz, column_TAG)
ops.element('elasticBeamColumn',4, 3, 9 , A, E, G, Jxx, Iy, Iz, column_TAG)
ops.element('elasticBeamColumn',5, 5, 11, A, E, G, Jxx, Iy, Iz, column_TAG)
ops.element('elasticBeamColumn',6, 4, 10, A, E, G, Jxx, Iy, Iz, column_TAG)

# Columnas segundo nivel (definición con sección - MÁS VERSÁTIL)
# ops.element('elasticBeamColumn', eleTag, *eleNodes, secTag, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)
ops.element('elasticBeamColumn',7 , 12, 16, rectSec1_TAG, column_TAG)
ops.element('elasticBeamColumn',8 , 9 , 13, rectSec1_TAG, column_TAG)
ops.element('elasticBeamColumn',9 , 11, 15, rectSec1_TAG, column_TAG)
ops.element('elasticBeamColumn',10, 10, 14, rectSec1_TAG, column_TAG)

# Vigas X - Nivel 1
ops.element('elasticBeamColumn',11,  7, 8 , rectSec1_TAG, xBeam_TAG)
ops.element('elasticBeamColumn',12, 12, 9 , rectSec1_TAG, xBeam_TAG)
ops.element('elasticBeamColumn',13, 11, 10, rectSec1_TAG, xBeam_TAG)

# Vigas Y - Nivel 1
ops.element('elasticBeamColumn',14, 7 , 12 , rectSec1_TAG, yBeam_TAG)
ops.element('elasticBeamColumn',15, 12, 11 , rectSec1_TAG, yBeam_TAG)
ops.element('elasticBeamColumn',16,  8,  9 , rectSec1_TAG, yBeam_TAG)
ops.element('elasticBeamColumn',17,  9, 10 , rectSec1_TAG, yBeam_TAG)

# Vigas X - Nivel 2
ops.element('elasticBeamColumn',18, 16, 13, rectSec1_TAG, xBeam_TAG)
ops.element('elasticBeamColumn',19, 15, 14, rectSec1_TAG, xBeam_TAG)

# Vigas Y - Nivel 2
ops.element('elasticBeamColumn',20, 16, 15, rectSec1_TAG, yBeam_TAG)
ops.element('elasticBeamColumn',21, 13, 14, rectSec1_TAG, yBeam_TAG)

# =====================================================================================================
ops.fixZ(0, 1,1,1,1,1,1) # Restringe totalmente los nodos con coordenada z=0 (plano XY).
# =====================================================================================================


# create TimeSeries
constantTIME_SERIES_TAG = 1
ops.timeSeries("Constant", constantTIME_SERIES_TAG)

# create a plain load pattern
plainPATTERN_TAG = 1
ops.pattern("Plain", plainPATTERN_TAG, constantTIME_SERIES_TAG)


Fx = -4.0e4 #[N]  
Fy = -2.5e4 #[N]
Fz = -3.0e4 #[N]

Q = -40e3 #[N]/[m]

ops.load(14, Fx, Fy, Fz, 0., 0., 0.)

ops.eleLoad('-ele', 20,'-type', '-beamUniform', Q, 0,0)

ops.eleLoad('-ele', [11,12,13,14,15,16,17,18,19], '-range', 11, 19, '-type', '-beamUniform', Q, 0,0)


# ========================================================
# Por ahora esto va por default
ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.test('NormDispIncr', 1.0e-6, 6, 2)
ops.algorithm('Linear')
ops.integrator('LoadControl', 1)
# ========================================================

ops.analysis('Static')
ops.analyze(1)

# PLOT ================================================================================================
opsv.plot_model()

sfac = 0e0

# fig_wi_he = 22., 14.
fig_wi_he = 30., 20.

# - 1
nep = 9
opsv.plot_defo(sfac, nep, az_el=(-68., 39.),
               fig_wi_he=fig_wi_he, endDispFlag=0)

plt.title('Deformed test')


sfacN  = 0.0  # 1.e-2
sfacVy = 0.0  # 5.e-2
sfacVz = 0.0  # 1.e-2
sfacMy = 0.0  # 1.e-2
sfacMz = 7.5e-6
sfacT  = 0.0  # 1.e-2

# plt.figure()
#opsv.section_force_diagram_3d('N', sfacN)
#plt.title('Axial force N')
#
#opsv.section_force_diagram_3d('Vy', sfacVy)
#plt.title('Transverse force Vy')
#
#opsv.section_force_diagram_3d('Vz', sfacVz)
#plt.title('Transverse force Vz')
#
#opsv.section_force_diagram_3d('My', sfacMy)
#plt.title('Bending moments My')
#
opsv.section_force_diagram_3d('Mz', sfacMz)
plt.title('Bending moments Mz')
#
#opsv.section_force_diagram_3d('T', sfacT)
#plt.title('Torsional moment T')


plt.show()

#vfo.plot_model(show_nodetags="yes",show_eletags="yes")



