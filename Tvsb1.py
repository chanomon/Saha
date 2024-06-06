#!/usr/bin/env python3

import matplotlib.pyplot as plt

xT = []
T = []
xb1 = []
b1 = []

#Data of the temperature cubes models
T1 = {'T':6.582992e3,'rho':5693761045746987.0,'H':5.166328e+15,'HI':5.155527e+15,'Z':0.000000e+00,
         'HII':1.080058e+13,'HeI':5.166328e+14,'HeII':1.685692e+04, 'HeIII':1.997059e-30, 'b1':4.656953e-01} 
T2 = {'T':4.529990e+03,'rho':503483663156121.00,'H':4.576968e+14,'HI':4.576796e+14,'Z':4.285714e-01,
         'HII':1.719157e+10,'HeI':4.576968e+13,'HeII':4.135235e-03, 'HeIII':6.057253e-53,'b1':2.168067e+00}
T3 = {'T':4.480263e+03,'rho':423097318469564.38,'H':3.846200e+14,'HI':3.846048e+14, 'Z':4.537815e-01,
         'HII':1.525923e+10,'HeI':3.846200e+13,'HeII':2.685823e-03, 'HeIII':1.302021e-53,'b1':1.722403e+00}
T4 = {'T':5.608734e+03,'rho':20985020601850.918,'H':1.877820e+13,'HI':1.844920e+13, 'Z':8.823529e-01,
         'HII':3.290003e+11,'HeI':1.877820e+12,'HeII':1.805179e+01, 'HeIII':6.798283e-38,'b1':1.007221e+01}
T5 = {'T':6.622204e+03,'rho':870351810762.43091,'H':5.768361e+11,'HI':3.410040e+11, 'Z':1.512605e+00,
         'HII':2.358321e+11,'HeI':7.965357e+02,'HeII':7.965357e+02, 'HeIII':4.015894e-29,'b1':4.707660e+00}
T6 = {'T':6.461409e+04,'rho':28080775459.989269,'H':1.220905e+10,'HI':2.959773e+02, 'Z':2.168067e+00,
         'HII':1.220905e+10,'HeI':1.968145e-03,'HeII':4.516401e+04, 'HeIII':1.220860e+09,'b1':2.069515e+07}
T7 = {'T':3.698417e+05,'rho':4559257602.1237888,'H':1.982286e+09,'HI':1.561717e+00,'Z':3.333333e+00,
         'HII':1.982286e+09,'HeI':2.980232e-08,'HeII':5.620723e-01, 'HeIII':1.982286e+08,'b1':6.361830e+08}

T_cubes = [T['T'] for T in [T1,T2,T3,T4,T5,T6,T7]]
b1_cubes = [T['b1'] for T in [T1,T2,T3,T4,T5,T6,T7]]
Z_heights = [T['Z'] for T in [T1,T2,T3,T4,T5,T6,T7]]

with open('T.dat', "rb") as Tvalc:
    for line in Tvalc:
        values = line.split()
        xT.append(float(values[0]))
        T.append(float(values[1]))
with open('b1.dat', "rb") as b1profile:
    for line in b1profile:
        values = line.split()
        xb1.append(float(values[0]))
        b1.append(float(values[1]))




fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(xT, T, 'r-')
ax2.plot(xb1, b1, 'b-')

ax1.set_xlabel('Z [Mm]')
ax1.set_ylabel('Temp [K]', color='r')
ax2.set_ylabel('b1', color='b')
ax1.set_yscale('log')
ax2.set_yscale('log')
#for b,t,c,z in zip(b1_cubes,T_cubes,['b','r','g','y','c','m','k'],Z_heights):
ax1.scatter(Z_heights,T_cubes,label='Temp',color='r')
ax2.scatter(Z_heights,b1_cubes,label='b1',color='b')

plt.legend()    
plt.grid()
plt.show()