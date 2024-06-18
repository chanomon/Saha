#!/usr/bin/env python3
from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from v3sahaHHe import *
mpl.rcParams["savefig.directory"] = './'



T2 = {'T': 4000.0, 'rho': 191811000000.0, 'H': 174296000000.0, 'HI': 174211000000.0, 'HII': 85602800.0, 'HeI': 17429600000.0, 'HeII': 4.95014e-07, 'HeIII': 9.12896e-62, 'b1': 9.78287}
T3 = {'T': 4999.99, 'rho': 163073000000.0, 'H': 143778000000.0, 'HI': 138860000000.0, 'HII': 4917460000.0, 'HeI': 14377800000.0, 'HeII': 0.0172504, 'HeIII': 4.42053e-45, 'b1': 11.1426}
T4 = {'T': 5999.99, 'rho': 231330000000.0, 'H': 160608000000.0, 'HI': 105948000000.0, 'HII': 54660500000.0, 'HeI': 16060800000.0, 'HeII': 19.6628, 'HeIII': 5.27822e-34, 'b1': 10.3927}
T5 = {'T': 6999.99, 'rho': 333578000000.0, 'H': 178058000000.0, 'HI': 40344000000.0, 'HII': 137714000000.0, 'HeI': 17805800000.0, 'HeII': 3000.32, 'HeIII': 4.21022e-26, 'b1': 9.61527}
T6 = {'T': 7999.99, 'rho': 332851000000.0, 'H': 164092000000.0, 'HI': 11741900000.0, 'HII': 152350000000.0, 'HeI': 16409100000.0, 'HeII': 102371.0, 'HeIII': 2.57321e-20, 'b1': 10.2375}
T7 = {'T': 8999.99, 'rho': 301904000000.0, 'H': 147019000000.0, 'HI': 6837830000.0, 'HII': 140182000000.0, 'HeI': 14701100000.0, 'HeII': 851151.0, 'HeIII': 2.43194e-16, 'b1': 10.9982}
T8 = {'T': 9999.99, 'rho': 273382000000.0, 'H': 132682000000.0, 'HI': 5254450000.0, 'HII': 127428000000.0, 'HeI': 13264500000.0, 'HeII': 3744800.0, 'HeIII': 2.44298e-13, 'b1': 12.3502}
T9 = {'T': 11000.0, 'rho': 249741000000.0, 'H': 120860000000.0, 'HI': 4079090000.0, 'HII': 116781000000.0, 'HeI': 12073200000.0, 'HeII': 12820800.0, 'HeIII': 7.31986e-11, 'b1': 14.4624}
T10 = {'T': 12000.0, 'rho': 230629000000.0, 'H': 111413000000.0, 'HI': 3372440000.0, 'HII': 108040000000.0, 'HeI': 11106600000.0, 'HeII': 34665900.0, 'HeIII': 8.01076e-09, 'b1': 16.1504}
T11 = {'T': 13000.0, 'rho': 215850000000.0, 'H': 104139000000.0, 'HI': 2921800000.0, 'HII': 101217000000.0, 'HeI': 10335000000.0, 'HeII': 78971100.0, 'HeIII': 4.10969e-07, 'b1': 17.45}
T12 = {'T': 14000.0, 'rho': 205191000000.0, 'H': 98702900000.0, 'HI': 2267860000.0, 'HII': 96435000000.0, 'HeI': 9687240000.0, 'HeII': 183043000.0, 'HeIII': 1.57812e-05, 'b1': 21.4096}
T13 = {'T': 15000.0, 'rho': 193261000000.0, 'H': 92673500000.0, 'HI': 1733360000.0, 'HII': 90940200000.0, 'HeI': 8887180000.0, 'HeII': 380176000.0, 'HeIII': 0.000385793, 'b1': 26.406}
T14 = {'T': 16000.0, 'rho': 182356000000.0, 'H': 87072900000.0, 'HI': 1252790000.0, 'HII': 85820100000.0, 'HeI': 7951840000.0, 'HeII': 755444000.0, 'HeIII': 0.00720296, 'b1': 34.4685}
T15 = {'T': 17000.0, 'rho': 172521000000.0, 'H': 81972600000.0, 'HI': 938374000.0, 'HII': 81034200000.0, 'HeI': 6880600000.0, 'HeII': 1316659150.0, 'HeIII': 0.0902862, 'b1': 43.4406}
T16 = {'T': 18000.0, 'rho': 163833000000.0, 'H': 77429700000.0, 'HI': 749817000.0, 'HII': 76679900000.0, 'HeI': 5762360000.0, 'HeII': 1980600000.0, 'HeIII': 0.756152, 'b1': 51.4321}
T17 = {'T': 19000.0, 'rho': 156571000000.0, 'H': 73355200000.0, 'HI': 505030000.0, 'HII': 72850100000.0, 'HeI': 4305360000.0, 'HeII': 3030160000.0, 'HeIII': 6.51827, 'b1': 72.5333}
T18 = {'T': 20000.0, 'rho': 149854000000.0, 'H': 69688000000.0, 'HI': 375448000.0, 'HII': 69312500000.0, 'HeI': 3083850000.0, 'HeII': 3884940000.0, 'HeIII': 37.1983, 'b1': 92.8135}
T19 = {'T': 21000.0, 'rho': 143905000000.0, 'H': 66371000000.0, 'HI': 239951000.0, 'HII': 66131100000.0, 'HeI': 1870900000.0, 'HeII': 4766210000.0, 'HeIII': 210.426, 'b1': 138.537}

TT = [t['T'] for t in [T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19]]

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
T19hi = T19['HI']/T19['H']

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
T19hii = T19['HII']/T19['H']

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
T19hei = T19['HeI']/(T19['HeI'] + T19['HeII'] + T19['HeIII'])

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
T19heii = T19['HeII']/(T19['HeI'] + T19['HeII'] + T19['HeIII'])

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
T19heiii = T19['HeIII']/(T19['HeI'] + T19['HeII'] + T19['HeIII'])

hi = [T2hi,T3hi,T4hi,T5hi,T6hi,T7hi,T8hi,T9hi,T10hi,T11hi,T12hi,T13hi,T14hi,T15hi,T16hi,T17hi,T18hi,T19hi]
hii = [T2hii,T3hii,T4hii,T5hii,T6hii,T7hii,T8hii,T9hii,T10hii,T11hii,T12hii,T13hii,T14hii,T15hii,T16hii,T17hii,T18hii,T19hii]
hei = [T2hei,T3hei,T4hei,T5hei,T6hei,T7hei,T8hei,T9hei,T10hei,T11hei,T12hei,T13hei,T14hei,T15hei,T16hei,T17hei,T18hei,T19hei]
heii = [T2heii,T3heii,T4heii,T5heii,T6heii,T7heii,T8heii,T9heii,T10heii,T11heii,T12heii,T13heii,T14heii,T15heii,T16heii,T17heii,T18heii,T19heii]
heiii = [T2heiii,T3heiii,T4heiii,T5heiii,T6heiii,T7heiii,T8heiii,T9heiii,T10heiii,T11heiii,T12heiii,T13heiii,T14heiii,T15heiii,T16heiii,T17heiii,T18heiii,T19heiii]

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

b1__text = [T['b1'] for T in [T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19]]


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
ax1.set_title('Hidrógeno')#Ecuacion de Saha')
ax1.set_xlabel('Temperatura [K]')
ax1.set_ylabel('% de ionizacion')
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(temperatures,HeI,c='tab:green',label="HeI SAHA")
ax2.plot(TT,hei,c='green',label='HeI, Tonalli(gas ideal)',linestyle="dashed")
ax2.set_title('Helio')
ax2.set_xlabel('Temperatura [K]')
ax2.set_ylabel('% de ionización')

ax2.plot(temperatures,HeII,c='tab:purple',label="HeII SAHA")
ax2.plot(TT,heii,c='purple',label='HeII, Tonalli(gas ideal)',linestyle="dashed")
ax2.legend()

ax2.plot(temperatures,HeIII,c='tab:brown',label="HeIII SAHA")
ax2.plot(TT,heiii,c='brown',label='HeIII, Tonalli(gas ideal)',linestyle="dashed")
ax2.legend()
plt.show()

