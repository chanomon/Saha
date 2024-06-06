#!/usr/bin/env python

from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
from modsahaHHe import saha
import matplotlib as mpl

mpl.rcParams["savefig.directory"] = './'
##########Reading VALC
with open('hydrostatic.dat', "rb") as fvalc:
        for i in range(14):
            l = fvalc.readline()
            #print l
        contentvalc = fvalc.readlines()
Tvalc = []
Hvalc = []
HI = []
HII = []
HeI = []
HeII = []
HeIII = []
zvalc = []
n_e = []
for l in contentvalc:
    line = l.split()
    Tvalc.append(int(line[2]))
    Hvalc.append(float(line[4]))
    zvalc.append(float(line[1]))
    H = Hvalc[-1]
    ni = saha(Tvalc[-1],H)
    HIp =  ni[0]####esto seria cero por la carga del H neutro?
    HIIp = ni[1]
    HeIp = ni[2]###### y esto tambien?
    HeIIp = ni[3]
    HeIIIp = ni[4]
    n_e.append(ni[5])
    He = 0.1*H
    HI.append(HIp/H)
    HII.append(HIIp/H)
    HeI.append(HeIp/He)
    HeII.append(HeIIp/He)
    HeIII.append(HeIIIp/He)

plt.plot (zvalc, n_e)
plt.plot(Tvalc,HI,label='HI')
plt.plot(Tvalc,HII,label='HII')
plt.plot(Tvalc,HeI,label='HeI')
plt.plot(Tvalc,HeII,label='HeII')
plt.plot(Tvalc,HeIII,label='HeIII')
plt.legend()
plt.xscale('log')
plt.show()
