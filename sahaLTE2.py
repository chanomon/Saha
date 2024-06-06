

#!/usr/bin/env python3
from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from v3sahaHHe import *
mpl.rcParams["savefig.directory"] = './'

valorPascales = str(11139)

T1 = {'T': 4000.0, 'rho': 2.13472e+17, 'H': 1.94066e+17, 'HI': 1.94065e+17, 'HII': 28893400000.0, 'HeI': 1.94066e+16, 'HeII': 0.000167, 'HeIII': 9.33162e-63, 'b1': 1.0}
T2 = {'T': 4999.99, 'rho': 1.70781e+17, 'H': 1.55254e+17, 'HI': 1.55252e+17, 'HII': 1584990000000.0, 'HeI': 1.55254e+16, 'HeII': 5.37001, 'HeIII': 3.96712e-46, 'b1': 1.0}
T3 = {'T': 5999.99, 'rho': 1.42361e+17, 'H': 1.29398e+17, 'HI': 1.29375e+17, 'HII': 23073700000000.0, 'HeI': 1.29398e+16, 'HeII': 5476.36, 'HeIII': 5.08183e-35, 'b1': 1.0}
T4 = {'T': 6999.99, 'rho': 1.22297e+17, 'H': 1.11037e+17, 'HI': 1.10879e+17, 'HII': 157119000000000.0, 'HeI': 1.11037e+16, 'HeII': 776694.0, 'HeIII': 4.52444e-27, 'b1': 1.0}
T5 = {'T': 7999.99, 'rho': 1.08058e+17, 'H': 9.76312e+16, 'HI': 9.69675e+16, 'HII': 663651000000000.0, 'HeI': 9763120000000000.0, 'HeII': 32128500.0, 'HeIII': 4.2599e-21, 'b1': 1.0}
T6 = {'T': 8999.99, 'rho': 9.89127e+16, 'H': 8.80722e+16, 'HI': 8.60388e+16, 'HII': 2033340000000000.0, 'HeI': 8807220000000000.0, 'HeII': 587813295.0, 'HeIII': 1.9361e-16, 'b1': 1.00508}
T7 = {'T': 9999.99, 'rho': 9.50935e+16, 'H': 8.19678e+16, 'HI': 7.70389e+16, 'HII': 4928900000000000.0, 'HeI': 8196780000000000.0, 'HeII': 6105000000.0, 'HeIII': 1.05071e-12, 'b1': 1.01292}
T8 = {'T': 11000.0, 'rho': 9.68395e+16, 'H': 7.90221e+16, 'HI': 6.91069e+16, 'HII': 9915180000000000.0, 'HeI': 7902170000000000.0, 'HeII': 42053800000.0, 'HeIII': 1.20327e-09, 'b1': 1.0167}
T9 = {'T': 12000.0, 'rho': 1.03485e+17, 'H': 7.85615e+16, 'HI': 6.14944e+16, 'HII': 1.70671e+16, 'HeI': 7855940000000000.0, 'HeII': 212423000000.0, 'HeIII': 4.25261e-07, 'b1': 1.01729}
T10 = {'T': 13000.0, 'rho': 1.12735e+17, 'H': 7.92142e+16, 'HI': 5.36155e+16, 'HII': 2.55987e+16, 'HeI': 7920580000000000.0, 'HeII': 834141000000.0, 'HeIII': 5.98279e-05, 'b1': 1.01645}
T11 = {'T': 14000.0, 'rho': 1.21254e+17, 'H': 7.94221e+16, 'HI': 4.55354e+16, 'HII': 3.38867e+16, 'HeI': 7939580000000000.0, 'HeII': 2625490000000.0, 'HeIII': 0.00396149, 'b1': 1.01618}
T12 = {'T': 15000.0, 'rho': 1.26437e+17, 'H': 7.83607e+16, 'HI': 3.8127e+16, 'HII': 4.02337e+16, 'HeI': 7829340000000000.0, 'HeII': 6736550000000.0, 'HeIII': 0.137499, 'b1': 1.01755}
T13 = {'T': 16000.0, 'rho': 1.27546e+17, 'H': 7.60783e+16, 'HI': 3.22326e+16, 'HII': 4.38457e+16, 'HeI': 7593510000000000.0, 'HeII': 14325100000000.0, 'HeIII': 2.71224, 'b1': 1.02048}
T14 = {'T': 17000.0, 'rho': 1.25438e+17, 'H': 7.30564e+16, 'HI': 2.80062e+16, 'HII': 4.50502e+16, 'HeI': 7279690000000000.0, 'HeII': 25948500000000.0, 'HeIII': 33.1445, 'b1': 1.02436}
T15 = {'T': 18000.0, 'rho': 1.21511e+17, 'H': 6.97866e+16, 'HI': 2.50828e+16, 'HII': 4.47039e+16, 'HeI': 6937110000000000.0, 'HeII': 41554700000000.0, 'HeIII': 276.488, 'b1': 1.02855}
T16 = {'T': 19000.0, 'rho': 1.16964e+17, 'H': 6.65552e+16, 'HI': 2.28634e+16, 'HII': 4.36917e+16, 'HeI': 6594030000000000.0, 'HeII': 61482900000000.0, 'HeIII': 1752.14, 'b1': 1.04296}
T17 = {'T': 20000.0, 'rho': 1.12316e+17, 'H': 6.34926e+16, 'HI': 2.11043e+16, 'HII': 4.23883e+16, 'HeI': 6263420000000000.0, 'HeII': 85845400000000.0, 'HeIII': 8942.71, 'b1': 1.06182}
T18 = {'T': 21000.0, 'rho': 1.07778e+17, 'H': 6.06439e+16, 'HI': 1.96885e+16, 'HII': 4.09553e+16, 'HeI': 5949980000000000.0, 'HeII': 114407000000000.0, 'HeIII': 38123.9, 'b1': 1.07935}

TT = [t['T'] for t in [T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]]
T1hi = T1['HI']/T1['H']
T2hi = T2['HI']/T2['H']
T3hi = T3['HI']/T3['H']
T4hi = T4['HI']/T4['H']
T5hi = T5['HI']/T5['H']
T6hi = T6['HI']/T6['H']
T7hi = T7['HI']/T7['H']
T8hi = T8['HI']/T8['H']
T9hi = T9['HI']/T9['H']
T10hi = T10['HI']/T10['H']
T11hi = T11['HI']/T11['H']
T12hi = T12['HI']/T12['H']
T13hi = T13['HI']/T13['H']
T14hi = T14['HI']/T14['H']
T15hi = T15['HI']/T15['H']
T16hi = T16['HI']/T16['H']
T17hi = T17['HI']/T17['H']
T18hi = T18['HI']/T18['H']

T1hii = T1['HII']/T1['H']
T2hii = T2['HII']/T2['H']
T3hii = T3['HII']/T3['H']
T4hii = T4['HII']/T4['H']
T5hii = T5['HII']/T5['H']
T6hii = T6['HII']/T6['H']
T7hii = T7['HII']/T7['H']
T8hii = T8['HII']/T8['H']
T9hii = T9['HII']/T9['H']
T10hii = T10['HII']/T10['H']
T11hii = T11['HII']/T11['H']
T12hii = T12['HII']/T12['H']
T13hii = T13['HII']/T13['H']
T14hii = T14['HII']/T14['H']
T15hii = T15['HII']/T15['H']
T16hii = T16['HII']/T16['H']
T17hii = T17['HII']/T17['H']
T18hii = T18['HII']/T18['H']

T1hei = T1['HeI']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2hei = T2['HeI']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3hei = T3['HeI']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4hei = T4['HeI']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5hei = T5['HeI']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6hei = T6['HeI']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7hei = T7['HeI']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
T8hei = T8['HeI']/(T8['HeI'] + T8['HeII'] + T8['HeIII'])
T9hei = T9['HeI']/(T9['HeI'] + T9['HeII'] + T9['HeIII'])
T10hei = T10['HeI']/(T10['HeI'] + T10['HeII'] + T10['HeIII'])
T11hei = T11['HeI']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
T12hei = T12['HeI']/(T12['HeI'] + T12['HeII'] + T12['HeIII'])
T13hei = T13['HeI']/(T13['HeI'] + T13['HeII'] + T13['HeIII'])
T14hei = T14['HeI']/(T14['HeI'] + T14['HeII'] + T14['HeIII'])
T15hei = T15['HeI']/(T15['HeI'] + T15['HeII'] + T15['HeIII'])
T16hei = T16['HeI']/(T16['HeI'] + T16['HeII'] + T16['HeIII'])
T17hei = T17['HeI']/(T17['HeI'] + T17['HeII'] + T17['HeIII'])
T18hei = T18['HeI']/(T18['HeI'] + T18['HeII'] + T18['HeIII'])

T1heii = T1['HeII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2heii = T2['HeII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3heii = T3['HeII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4heii = T4['HeII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5heii = T5['HeII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6heii = T6['HeII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7heii = T7['HeII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
T8heii = T8['HeII']/(T8['HeI'] + T8['HeII'] + T8['HeIII'])
T9heii = T9['HeII']/(T9['HeI'] + T9['HeII'] + T9['HeIII'])
T10heii = T10['HeII']/(T10['HeI'] + T10['HeII'] + T10['HeIII'])
T11heii = T11['HeII']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
T12heii = T12['HeII']/(T12['HeI'] + T12['HeII'] + T12['HeIII'])
T13heii = T13['HeII']/(T13['HeI'] + T13['HeII'] + T13['HeIII'])
T14heii = T14['HeII']/(T14['HeI'] + T14['HeII'] + T14['HeIII'])
T15heii = T15['HeII']/(T15['HeI'] + T15['HeII'] + T15['HeIII'])
T16heii = T16['HeII']/(T16['HeI'] + T16['HeII'] + T16['HeIII'])
T17heii = T17['HeII']/(T17['HeI'] + T17['HeII'] + T17['HeIII'])
T18heii = T18['HeII']/(T18['HeI'] + T18['HeII'] + T18['HeIII']) 

T1heiii = T1['HeIII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2heiii = T2['HeIII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3heiii = T3['HeIII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4heiii = T4['HeIII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5heiii = T5['HeIII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6heiii = T6['HeIII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7heiii = T7['HeIII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
T8heiii = T8['HeIII']/(T8['HeI'] + T8['HeII'] + T8['HeIII'])
T9heiii = T9['HeIII']/(T9['HeI'] + T9['HeII'] + T9['HeIII'])
T10heiii = T10['HeIII']/(T10['HeI'] + T10['HeII'] + T10['HeIII'])   
T11heiii = T11['HeIII']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
T12heiii = T12['HeIII']/(T12['HeI'] + T12['HeII'] + T12['HeIII'])
T13heiii = T13['HeIII']/(T13['HeI'] + T13['HeII'] + T13['HeIII'])
T14heiii = T14['HeIII']/(T14['HeI'] + T14['HeII'] + T14['HeIII'])
T15heiii = T15['HeIII']/(T15['HeI'] + T15['HeII'] + T15['HeIII'])
T16heiii = T16['HeIII']/(T16['HeI'] + T16['HeII'] + T16['HeIII'])
T17heiii = T17['HeIII']/(T17['HeI'] + T17['HeII'] + T17['HeIII'])
T18heiii = T18['HeIII']/(T18['HeI'] + T18['HeII'] + T18['HeIII'])


hi = [T1hi,T2hi,T3hi,T4hi,T5hi,T6hi,T7hi,T8hi,T9hi,T10hi,T11hi,T12hi,T13hi,T14hi,T15hi,T16hi,T17hi,T18hi]
hii = [T1hii,T2hii,T3hii,T4hii,T5hii,T6hii,T7hii,T8hii,T9hii,T10hii,T11hii,T12hii,T13hii,T14hii,T15hii,T16hii,T17hii,T18hii]
hei = [T1hei,T2hei,T3hei,T4hei,T5hei,T6hei,T7hei,T8hei,T9hei,T10hei,T11hei,T12hei,T13hei,T14hei,T15hei,T16hei,T17hei,T18hei]
heii = [T1heii,T2heii,T3heii,T4heii,T5heii,T6heii,T7heii,T8heii,T9heii,T10heii,T11heii,T12heii,T13heii,T14heii,T15heii,T16heii,T17heii,T18heii,]
heiii = [T1heiii,T2heiii,T3heiii,T4heiii,T5heiii,T6heiii,T7heiii,T8heiii,T9heiii,T10heiii,T11heiii,T12heiii,T13heiii,T14heiii,T15heiii,T16heiii,T17heiii,T18heiii]

HI = []
HII = []
HeI = []
HeII = []
HeIII = []
n_e = []
N = 1e16
epsilon = 1e13

temperatures =  np.arange(4000,21000,1000)
for T in temperatures:
    hI, hII, heI, heII, heIII,ne = sahaH(T,N, epsilon)
    HI.append(hI)
    HII.append(hII)
    HeI.append(heI)
    HeII.append(heII)
    HeIII.append(heIII)
    n_e.append(ne)

b1__text = [T['b1'] for T in [T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]]


fig1, ax1 = plt.subplots()

ax1.plot(temperatures,HI,label='HI SAHA',color='tab:blue')
ax1.plot(TT,hi,label='HI, Tonalli(gas ideal)',linestyle="dashed",color='blue')
#colors = ["blue","blue","blue","blue","blue","blue","green","red","red","red","red","red","red"]
ax1.scatter(TT,hi,marker="o", label='b1')#,c=colors)
for i in range(len(b1__text)):
     #plt.text(t[i],hi[i],b1_text[i],fontsize=10)
     ax1.text(TT[i],hi[i],"%.1f" % b1__text[i],fontsize=10)
ax1.set_title('Hidrógeno')#Ecuacion de Saha')
ax1.set_xlabel('Temperatura [K]')
ax1.set_ylabel('%')
ax1.legend()


#fig2, ax2 = plt.subplots()
ax1.plot(temperatures,HII,c='tab:orange',label="HII SAHA")
ax1.plot(TT,hii,c='red',label='HII, Tonalli(gas ideal)',linestyle="dashed")
#plt.scatter(temperatures,HI,label='HI, NLTE',marker="o",c='tab:red',)
#plt.xscale('log')
ax1.set_title('Hidrógeno, P = '+valorPascales+"[Pa] modelo sin H-")#Ecuacion de Saha')
ax1.set_xlabel('Temperatura [K]')
ax1.set_ylabel('% de ionizacion')
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(temperatures,HeI,c='tab:green',label="HeI SAHA")
ax2.plot(TT,hei,c='green',label='HeI, Tonalli(gas ideal)',linestyle="dashed")
ax2.set_title('Helio, P = '+ valorPascales +"[Pa] modelo sin H-")
ax2.set_xlabel('Temperatura [K]')
ax2.set_ylabel('% de ionización')

ax2.plot(temperatures,HeII,c='tab:purple',label="HeII SAHA")
ax2.plot(TT,heii,c='purple',label='HeII, Tonalli(gas ideal)',linestyle="dashed")
ax2.legend()

ax2.plot(temperatures,HeIII,c='tab:brown',label="HeIII SAHA")
ax2.plot(TT,heiii,c='brown',label='HeIII, Tonalli(gas ideal)',linestyle="dashed")
ax2.legend()
plt.show()

