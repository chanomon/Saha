#!/usr/bin/env python3

from scipy.constants import pi,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt

def sahaH(T):
    a = ((2*pi*m_e*Boltzmann*T)/h**2)**(3./2)
    b = np.exp((-13.6*e)/(Boltzmann*T)) #se multiplica xi_H por e para pasar de eV a J
    return ((1/1e16)*a*b)
T =  np.arange(1000,20500,500)

psi = []
for i in T:
    psi.append(sahaH(i))
#print(h)
plt.plot(T,psi)
#plt.xscale('log')
plt.show()
