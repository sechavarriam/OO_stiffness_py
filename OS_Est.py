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

hP = 2.9 #[m]

#Longitudes
l1 = 8.45 #[m]
l2 = 4.43 #[m]
l3 = 8.50 #[m]
l4 = 7.40 #[m]
l5 = 4.24 #[m]
l6 = 3.12 #[m]
l7 = 2.46 #[m]
l8 = 8.73 #[m]
l9 = 2.47 #[m]
l10 = 1.04 #[m]
l11 = 3.45 #[m]
l12 = 1.83 #[m]
l13 = 1.00 #[m]
l14 = 2.85 #[m]
l15 = 3.30 #[m]
l16 = 1.00 #[m]
l17 = 1.15 #[m]
l18 = 2.81 #[m]
l19 = 1.44 #[m]
l20 = 2.08 #[m]
l21 = 2.65 #[m]
l22 = 1.13 #[m]
l23 = 6.57 #[m]
l24 = 9.02 #[m]
l25 = 5.84 #[m]
l26 = 4.40 #[m]
l27 = 2.07 #[m]
l28 = 2.88 #[m]
l29 = 3.12 #[m]
l30 = 2.83 #[m]
l31 = 2.46 #[m]
l32 = 2.30 #[m]
l33 = 3.50 #[m]
l34 = 5.25 #[m]
l35 = 1.92 #[m]
l36 = 2.45 #[m]
l37 = 3.13 #[m]
l38 = 2.59 #[m]
l39 = 0.80 #[m]

#Ángulos.
theta = math.radians(84.04)
alpha = math.radians(84.55)

#Secciones.

# Columna.
## Rectangular.
bCol = 0.50 #[m]
hCol = 0.70 #[m]

AColR = bCol*hCol #[m]²

IzColR = (bCol*hCol**3)/12 #[m]⁴
IyColR = (hCol*bCol**3)/12 #[m]⁴

aa = max(bCol,hCol)
bb = min(bCol,hCol)

JxxColR = aa*bb**3 * (1/3 - (0.21*bb/aa)*(1-bb**4/(12*aa*4)))

poiss = 0.3
ECol = 4700*math.sqrt(21) #[kPa]
GCol = ECol/(2*(1+poiss))

rectSec = 1
ops.section('Elastic', rectSec, ECol, AColR, IzColR, IyColR, GCol, JxxColR)

#Transformación.

column_TAG = 1
xBeam_TAG  = 2
yBeam_TAG  = 3

ops.geomTransf('Linear', column_TAG, -1, 0,0)
ops.geomTransf('Linear', yBeam_TAG ,  1, 0,0)
ops.geomTransf('Linear', xBeam_TAG ,  0,-1,0)

#Alturas de los pisos.
CoorZ = [0]
for i in range (25):
    CoorZ.append(CoorZ[-1]+hP)

#Función para definir el Tag del nodo.
def ij_2_Tag(i,j,num_nodosx,num_nodos_piso):
    return i*(num_nodosx)+(j+1)+num_nodos_piso

#Definición de nodos planta.

CoorXP = [
[-l23 + l22/math.tan(theta)         , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l29, l1+l2+l3+l4+l5+l24],
[-l23                               , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l37, l1+l2+l3+l4+l5+l24],
[-l23 - l7/math.tan(theta)          , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l30, l1+l2+l3+l4+l5+l24-l7/math.tan(alpha)],
[-l23 - (l7+l32)/math.tan(theta)    , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l38, l1+l2+l3+l4+l5+l24-(l7+l32)/math.tan(alpha)   ],
[-l23 - (l7+l33)/math.tan(theta)    , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l31, l1+l2+l3+l4+l5+l24-(l7+l33)/math.tan(alpha)   ],
[-l23 - (l7+l34)/math.tan(theta)    , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l31, l1+l2+l3+l4+l5+l24-(l7+l34)/math.tan(alpha)   ],
[-l23 - (l7+l8)/math.tan(theta)     , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l31, l1+l2+l3+l4+l5+l24-(l7+l8)/math.tan(alpha)    ],
[-l23 - (l7+l8+l39)/math.tan(theta) , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l31, l1+l2+l3+l4+l5+l24-(l7+l8+l9)/math.tan(alpha)],
[-l23 - (l7+l8+l39)/math.tan(theta) , 0, l26, l25, l1, l1+l27, l1+l28, l1+l2, l1+l2+l3, l1+l2+l3+l4, l1+l2+l3+l4+l5, l1+l2+l3+l4+l5+l31, l1+l2+l3+l4+l5+l24-(l7+l8+l9)/math.tan(alpha)]
]

CoorYP =[
[-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ,-l22        ],
[  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ,  0         ],
[l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ,l7          ],
[l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ,l7+l32      ],
[l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ,l7+l33      ],
[l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ,l7+l34      ],
[l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ,l7+l8       ],
[l7+l8+l39   ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ,l7+l8+l9    ],
[l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l35,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36,l7+l8+l9+l36]
]

num_nodosyP = len(CoorXP)
num_nodosxP = len(CoorXP[0])
num_nodosz = len(CoorZ)

TagEx = 1
TagEy = 5001
TagEz = 10001
Tag_n = 1
num_nodos_piso = 0
Cambio_planta = 6      #Piso en el que cambia de planta.

for k in range (Cambio_planta):
    for i in range (num_nodosyP):
        Opt = []
        for j in range (num_nodosxP):
            Opt.append([CoorXP[i][j],CoorYP[i][j]])
            ops.node(Tag_n, CoorXP[i][j], CoorYP[i][j], CoorZ[k])
            Tag_n += 1
        #CoorXY.append(Opt)

    #Definición de elementos.
    for i in range (num_nodosyP):
        for j in range (num_nodosxP):
            n = ij_2_Tag(i,j,num_nodosxP,num_nodos_piso)
            #Definición de los elementos en "x".
            if (n-num_nodos_piso) % num_nodosxP != 0:                        #La función módulo ("%"), se usa para evitar que se cree un elemento desde el nodo final de fila con nodo inicial de la siguiente fila.
                if i != (num_nodosyP-1): 
                    ops.element('elasticBeamColumn', TagEx, n, n+1 , rectSec, xBeam_TAG)
                    TagEx += 1
                elif j != 0 and j != 1:
                    ops.element('elasticBeamColumn', TagEx, n, n+1 , rectSec, xBeam_TAG)
                    TagEx += 1
                TagEx += 1
            #Definición de los elementos en "y".
            if (i+1) % num_nodosyP != 0:
                                                    #De manera análoga para los elementos de la fila final.
                if i != (num_nodosyP-2):
                    ops.element('elasticBeamColumn', TagEy, n, n+num_nodosxP , rectSec, yBeam_TAG)
                    TagEy += 1
                elif j != 0 and j != 1:
                    ops.element('elasticBeamColumn', TagEy, n, n+num_nodosxP , rectSec, yBeam_TAG)
                    TagEy += 1
                TagEy += 1
    if num_nodos_piso == 0:
        n_n_piso_planta = Tag_n - 1
    else:
        for i in range (1, n_n_piso_planta + 1):
            if i != n_n_piso_planta - num_nodosxP + 1 and i != n_n_piso_planta - num_nodosxP + 2:
                ops.element('elasticBeamColumn', TagEz, num_nodos_piso + i,  num_nodos_piso + i - n_n_piso_planta , rectSec, column_TAG)
                TagEz += 1
            TagEz += 1
    
    #Elementos particulares.
    ops.element('elasticBeamColumn', TagEx, num_nodos_piso+7*num_nodosxP+2, num_nodos_piso+8*num_nodosxP+3, rectSec, yBeam_TAG)
    TagEx+=1

    num_nodos_piso = Tag_n - 1
    
    #Remoción de elementos.
    

# Definición de nodos
CoorX = [
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5],
[0, l1, l1+l20, l1+l18, l1+l14, l1+l2, l1+l2+l3, l1+l2+l3+l14, l1+l2+l3+l4, l1+l2+l3+l4+l5]
]

CoorY = [
[-l22           ,-l22           ,-l22           ,-l22           ,-l22           ,-l22           ,-l22           ,-l22           ,-l22           ,-l22           ],
[  0            ,  0            ,  0            ,  0            ,  0            ,  0            ,  0            ,  0            ,  0            ,  0            ],
[ l7            , l7            , l7            , l7            , l7            , l7            , l7            , l7            , l7            , l7            ],
[ l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        , l7+l11        ],
[ l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    , l7+l11+l12    ],
[ l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         , l7+l8         ],
[ l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      , l7+l8+l9      ], 
[ l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  , l7+l8+l9+l10  ]
]

CoorXY = []

#print(CoorZ,len(CoorZ))

num_nodosy = len(CoorX)
num_nodosx = len(CoorX[0])

#plt.plot(CoorX,CoorY,marker='o')
#plt.show()

#Elementos.
# ops.element('elasticBeamColumn', eleTag, *eleNodes, secTag, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)


##for k in range (Cambio_planta,num_nodosz):
#for k in range (Cambio_planta,9):
##k=6
#    for i in range (num_nodosy):
#        Opt = []
#        for j in range (num_nodosx):
#            Opt.append([CoorX[i][j],CoorY[i][j]])
#            ops.node(Tag_n, CoorX[i][j], CoorY[i][j], CoorZ[k])
#            Tag_n += 1
#        CoorXY.append(Opt)
#    #Nodos casos particulares.
#    ops.node(Tag_n, l1+l2+l3+l4+l5+l6, 0, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1+l2+l3+l4+l5+l17+l16, l7+l11, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1+l2+l3+l4+l5+l17, l7+l11, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1+l2+l3+l4+l5+l17, l7+l11+l12, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1, l7+l8+l9+l10+l19, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1+l20, l7+l8+l9+l10+l19, CoorZ[k])
#    Tag_n+=1
#    ops.node(Tag_n, l1+l2, l7+l8+l9+l10+l19, CoorZ[k])
#    Tag_n+=1
#    #Definición de elementos.
#    for i in range (num_nodosy):
#        for j in range (num_nodosx):
#            n = ij_2_Tag(i,j,num_nodosx,num_nodos_piso)
#            #Definición de los elementos en "x".
#            if (n-num_nodos_piso) % num_nodosx != 0:                        #La función módulo ("%"), se usa para evitar que se cree un elemento desde el nodo final de fila con nodo inicial de la siguiente fila.
#                ops.element('elasticBeamColumn', TagEx, n, n+1 , rectSec, xBeam_TAG)
#                TagEx += 1
#            #Definición de los elementos en "y".
#            if (i+1) % num_nodosy != 0:                                     #De manera análoga para los elementos de la fila final.
#                if j != 2 and (i < 5):
#                    ops.element('elasticBeamColumn', TagEy, n, n+num_nodosx , rectSec, yBeam_TAG)
#                    TagEy += 1
#                elif i >= 5:
#                    ops.element('elasticBeamColumn', TagEy, n, n+num_nodosx , rectSec, yBeam_TAG)
#                    TagEy += 1
#                TagEy += 1
#    #Elementos casos particulares.
#    ops.element('elasticBeamColumn', TagEx, 2*num_nodosx + num_nodos_piso, num_nodos_piso + num_nodosx*num_nodosy + 1, rectSec, xBeam_TAG)
#    TagEx += 1
#    ops.element('elasticBeamColumn', TagEy, num_nodos_piso + num_nodosx*num_nodosy + 1, num_nodos_piso + num_nodosx*num_nodosy + 2, rectSec, yBeam_TAG)
#    TagEy += 1
#    ops.element('elasticBeamColumn', TagEx, num_nodos_piso + num_nodosx*num_nodosy + 2, num_nodos_piso + num_nodosx*num_nodosy + 3, rectSec, xBeam_TAG)
#    TagEx += 1
#    ops.element('elasticBeamColumn', TagEx, 4*num_nodosx + num_nodos_piso, num_nodos_piso + num_nodosx*num_nodosy + 3, rectSec, xBeam_TAG)
#    TagEx += 1
#    ops.element('elasticBeamColumn', TagEx, 5*num_nodosx + num_nodos_piso, num_nodos_piso + num_nodosx*num_nodosy + 4, rectSec, xBeam_TAG)
#    TagEx += 1
#    ops.element('elasticBeamColumn', TagEy, num_nodos_piso + num_nodosx*num_nodosy + 3, num_nodos_piso + num_nodosx*num_nodosy + 4, rectSec, yBeam_TAG)
#    TagEy += 1
#    ops.element('elasticBeamColumn', TagEy, num_nodos_piso + 7*num_nodosx + 2, num_nodos_piso + num_nodosx*num_nodosy + 5, rectSec, yBeam_TAG)
#    TagEy += 1
#    ops.element('elasticBeamColumn', TagEy, num_nodos_piso + 7*num_nodosx + 3, num_nodos_piso + num_nodosx*num_nodosy + 6, rectSec, yBeam_TAG)
#    TagEy += 1
#    ops.element('elasticBeamColumn', TagEy, num_nodos_piso + 7*num_nodosx + 6, num_nodos_piso + num_nodosx*num_nodosy + 7, rectSec, yBeam_TAG)
#    TagEy += 1
#    ops.element('elasticBeamColumn', TagEx, num_nodos_piso + num_nodosx*num_nodosy + 5, num_nodos_piso + num_nodosx*num_nodosy + 6, rectSec, xBeam_TAG)
#    TagEx += 1
#    ops.element('elasticBeamColumn', TagEx, num_nodos_piso + num_nodosx*num_nodosy + 6, num_nodos_piso + num_nodosx*num_nodosy + 7, rectSec, xBeam_TAG)
#    TagEx += 1
#    
#    if num_nodos_piso == (Cambio_planta)*n_n_piso_planta:
#        n_n_piso = - num_nodos_piso + Tag_n - 1
#    else:
#        for i in range (1, n_n_piso + 1):
#            ops.element('elasticBeamColumn', TagEz, num_nodos_piso + i,  num_nodos_piso + i - n_n_piso , rectSec, column_TAG)
#            TagEz += 1
#    num_nodos_piso = Tag_n - 1

##opsv.plot_model()
#
# fig_wi_he = 22., 14.
fig_wi_he = 30., 20.

# - 1
nep = 9
opsv.plot_model(node_labels = 0, element_labels = 0, local_axes = False, az_el=(-68., 39.),
               fig_wi_he=fig_wi_he)
plt.show()

#PREGUNTAS.
#¿Cuál es el J para sección circular?
#¿Por qué en el despiece muestra una dimensión distinta al plano en la viga de las escaleras?
#¿Se deben definir los bordillos? No