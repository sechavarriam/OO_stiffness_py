import math
import numpy as np
import matplotlib.pyplot as plt


# Compute force vector for a fixed end force in element for different types of loads


def UniformGravity(Q, L):
    # Q: Load intensity
    # L: Length of the element

    return np.array([ 0, Q*L/2, Q*L**2/12, 0, Q*L/2, -Q*L**2/12]).transpose()


# Functions Taken fron Kassimali, A. (2011). Matrix Analysis of Structures. Cengage Learning.

def ConcentratedLoad(W,l1,L):
    # W: Load intensity
    # l1: Distance from the left end of the element to the point of application of the load
    # L: Length of the element

    l2 = L - l1

    FAb = 0.0
    FSb = (W*l2**2/(L**3))*(3*l1 + l2)
    FMb = W*l1*l2**2/L**2
    
    FAe = 0.0
    FSe = (W*l1**2/(L**3))*(3*l2 + l1)
    FMe = W*l2*l1**2/L**2

    return np.array([FAb, FSb, FMb, FAe, FSe, FMe]).transpose()

def ConcentratedMoment(M,l1,L):
    # M: Moment intensity (clockwise positive)
    # l1: Distance from the left end of the element to the point of application of the moment
    # L: Length of the element

    l2 = L - l1

    FAb = 0.0
    FSb = -6*M*l1*l2/(L**3)
    FMb = (M*l2*(-2*l1 + l2))/L**2
    
    FAe = 0.0
    FSe = 6*M*l1*l2/(L**3)
    FMe = (M*l1*(l1 - 2*l2))/L**2

    return np.array([FAb, FSb, FMb, FAe, FSe, FMe]).transpose()

def GeneralTrapezoidal(w1,w2,l1,l2,L):
    # w1: Load intensity at l1 (left end of the element)
    # w2: Load intensity at l2 (right end of the element)
    # l1: Distance from the left end of the element to the point where the load changes
    # l2: Distance from the right end of the element to the point where the load changes
    # L: Length of the element

    FAb = 0.0

    FSb = (w1*(L-l1)**3/(20*L**3))*(
        (7*L+8*l1)-(l2*(3*L+2*l1)/(L-l1))*(1+(l2/(L-l1))+l2**2/(L-l1)**2)+(2*l2**4/(L-l1)**3))
    +(w2*(L-l2)**3/(20*L**3))*(
        (3*L+2*l1)*(1+(l2/(L-l1))+(l2**2/(L-l1)**2)) - (l2**3/(L-l1)**2)*(2+(15*L+8*l2)/(L-l1)))
    
    FMb = (w1*(L-l1)**3/(60*L**2))*(
        3*(L+4*l1) - (l2*(2*L+3*l1)/(L-l1))*(1+l2/(L-l1)+l2**2/(L-l1)**2) + 3*l2**4/(L-l1)**3
    )+(w2*(L-l1)**3/(60*L**2))*(
        (2*L+3*l1)*(1+l2/(L-l1)+l2**2/(L-l1)**2) - (3*l2**3/(L-l1)**2)*(1+(5*L-4*l2)/(L-l1)))
    
    FAe = 0.0

    FSe = ((w1+w2)/2) * (L-l1-l2) - FSb
    
    FMe =  ((L-l1-l2)/6)*(w1*(-2*L+2*l1-l2) -w2*(L-l1+2*l2) ) + FSb*L - FMb

    return np.array([FAb, FSb, FMb, FAe, FSe, FMe]).transpose()

