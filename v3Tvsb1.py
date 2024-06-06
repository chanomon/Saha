#!/usr/bin/env python3

import matplotlib.pyplot as plt

xT = []
T = []
xb1 = []
b1 = []

#Data of the temperature cubes models
T11= {'T':8.319990e+03,'rho':1.3598838416081920E+017,'H':1.226102e+17,'HI':1.214931e+17,'Z':-75,
         'HII':1.117105e+15,'HeI':1.226102e+16,'HeII':1.000492e+08, 'HeIII':1.226102e+17,'b1':1.000000e+00}
T22= {'T':7.610000e+03,'rho':1.2990692270511490E+017,'H':1.177112e+17,'HI':1.172866e+17,'Z':-50,
         'HII':4.245889e+14,'HeI':1.177112e+16,'HeII':9.054896e+06, 'HeIII':9.054896e+06,'b1':1.000000e+00}
T33= {'T':6.910000e+03,'rho':1.2497481678350666E+017,'H':1.134900e+17,'HI':1.133541e+17,'Z':-25,
         'HII':1.358534e+14,'HeI':1.134900e+16,'HeII':5.296624e+05, 'HeIII':1.081089e-27,'b1':1.000000e+00}
T44= {'T':6.419993e+03,'rho':1.1436583510218205E+017,'H':1.039222e+17,'HI':1.038707e+17,'Z':0,
         'HII':5.145542e+13,'HeI':1.039222e+16,'HeII':4.904145e+04, 'HeIII':2.211169e-31,'b1':1.000000e+00}
T55= {'T':5.839993e+03,'rho':90210798156905680.,'H':8.199834e+16,'HI':8.198570e+16,'Z':50,
         'HII':1.263154e+13,'HeI':8.199834e+15,'HeII':1.675067e+03, 'HeIII':1.544291e-36,'b1':1.012878e+00}
T66= {'T':5.454994e+03,'rho':67292174531525320.,'H':6.117096e+16,'HI':6.116685e+16,'Z':100,
         'HII':4.114114e+12,'HeI':6.117096e+15,'HeII':1.168886e+02, 'HeIII':1.536597e-40,'b1':1.076110e+00}
T77={'T':4.169995e+03,'rho':2054000143651526.5,'H':1.867270e+15,'HI':1.867266e+15,'Z':515,
         'HII':3.571793e+09,'HeI':1.867270e+14,'HeII':7.568840e-05, 'HeIII':6.785565e-60,'b1':2.982902e-01}
T88={'T':6.149993e+03,'rho':9085542501650.3555,'H':7.614531e+12,'HI':6.904973e+12,'Z':1180,
         'HII':7.095582e+11,'HeI':7.614531e+11,'HeII':3.117520e+02, 'HeIII':1.143098e-32,'b1':9.905690e+00}
T99={'T':9.499989e+03,'rho':185865647373.76715,'H':8.921976e+10,'HI':1.498961e+09,'Z':2104,
         'HII':8.772080e+10,'HeI':8.918869e+09,'HeII':3.106368e+06, 'HeIII':4.042744e-14,'b1':3.069189e+01}
TAA={'T':1.069999e+04,'rho':169923704232.12473,'H':8.134339e+10,'HI':9.165050e+08,'Z':2107,
         'HII':8.042689e+10,'HeI':8.115252e+09,'HeII':1.908722e+07, 'HeIII':9.988068e-11,'b1':4.454739e+01}
TBB={'T':1.229999e+04,'rho':152650086425.49768,'H':7.285724e+10,'HI':4.848717e+08,'Z':2109,
         'HII':7.237237e+10,'HeI':7.150980e+09,'HeII':1.347447e+08, 'HeIII':3.799106e-07,'b1':7.528679e+01}
TCC={'T':1.849998e+04,'rho':107008160527.21744,'H':4.867734e+10,'HI':3.256713e+06,'Z':2113,
         'HII':4.867408e+10,'HeI':7.872827e+07,'HeII':4.789005e+09, 'HeIII':5.441422e+02,'b1':7.520729e+03}
TDD={'T':2.099998e+04,'rho':94199720507.881134,'H':4.282022e+10,'HI':4.092318e+05,'Z':2115,
         'HII':4.281981e+10,'HeI':4.422577e+06,'HeII':4.277527e+09, 'HeIII':7.169908e+04,'b1':7.169908e+04}
T_cubes = [T['T'] for T in [T11,T22,T33,T44,T55,T66,T77,T88,T99,TAA,TBB,TCC,TDD]]
b1_cubes = [T['b1'] for T in [T11,T22,T33,T44,T55,T66,T77,T88,T99,TAA,TBB,TCC,TDD]]
Z_heights = [T['Z']/1e3 for T in [T11,T22,T33,T44,T55,T66,T77,T88,T99,TAA,TBB,TCC,TDD]]

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
ax1.plot(Z_heights,T_cubes,'-',color='lightcoral')
ax2.plot(Z_heights,b1_cubes,'-',color='lightblue')
ax1.scatter(Z_heights,T_cubes,label='Temp',color='r')
ax2.scatter(Z_heights,b1_cubes,label='b1',color='b')

plt.legend()    
plt.grid()
plt.show()