#!/usr/bin/env python3

from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["savefig.directory"] = './'


#print pi
h = 6.6e-27
#print e
m_e =9.1e-28
Boltzmann = 8.6e-5
K = 1.38e-16



C = np.log10(2.0*(((2.0*pi*m_e*K) / (h**2))**(3./2)))
#print 'C',C


#def PsiHI(T, n_e):
#    return C - np.log10(n_e) + no.log()

def PsiHII(T,n_e):
    return C - np.log10(n_e)+ np.log10(0.5)+  1.5*np.log10(T)- 13.6*(5040.0/T) 

#def PsiHeI(T, n_e):
#    return C - np.log10(n_e) + np.log(/)

def PsiHeII(T,n_e):
    return C - np.log10(n_e) +  1.5*np.log10(T)- 24.59*(5040.0/T)

def PsiHeIII(T,n_e):
    return C - np.log10(n_e)+ np.log10(0.5) +  1.5*np.log10(T) - 54.59*(5040.0/T)#np.log10(2) 


def sahaH(T,N,epsilon):
    H = 0.9*N
    He = 0.1*N
    HI = (H * 0.5)  #####aqui me quede corrigiendo
    HII = HI*0.1
    HeI = He * 0.1
    HeII = HeI 
    HeIII = HeII
	
    n_e = 1e10
    error = 1e40
    
    while(True): 
       

        PSIHII = pow(10, PsiHII(T,n_e))
        PSIHeII = pow(10, PsiHeII(T,n_e))
        PSIHeIII = pow(10, PsiHeIII(T,n_e))
	###################################
        HI = (H) / (1.0 + PSIHII)
        HII = H - HI
        HeI = He/(1.0+PSIHeII*(1+PSIHeIII))
        HeII =  PSIHeII*HeI
        HeIII = PSIHeIII * HeII
	###################################
       ###################################
        n0 = n_e
        n_e = HII+ HeII + 2*HeIII
        n_e = (n_e + n0)/2.0        
        error = abs(n0-n_e) #### aqui podria estar la clave
        RHI = HI/(H)
        RHII = HII/(H)
        RHeI = HeI/(He)
        RHeII = HeII/(He)
        RHeIII = HeIII/(He)
        #print error
        if error <= epsilon:
            #print(T,RHI,RHII,RHeI,RHeII,RHeIII,n_e)
            break

        
    return RHI,RHII,RHeI,RHeII,RHeIII,n_e

temperatures =  np.arange(1000,500000,1000)##80000
#temperatures = [10000.0]
#sahaH(5000)

#### TAble of values obtained from the simulations
#### All from dt = 1 it = 1
T1 = {'T':6.582992e3,'rho':5693761045746987.0,'H':5.166328e+15,'HI':5.155527e+15,
         'HII':1.080058e+13,'HeI':5.166328e+14,'HeII':1.685692e+04, 'HeIII':1.997059e-30, 'b1':4.656953e-01} 
T2 = {'T':4.529990e+03,'rho':503483663156121.00,'H':4.576968e+14,'HI':4.576796e+14,
         'HII':1.719157e+10,'HeI':4.576968e+13,'HeII':4.135235e-03, 'HeIII':6.057253e-53,'b1':4.656953e-01}
T3 = {'T':4.480263e+03,'rho':423097318469564.38,'H':3.846200e+14,'HI':3.846048e+14,
         'HII':1.525923e+10,'HeI':3.846200e+13,'HeII':2.685823e-03, 'HeIII':1.302021e-53,'b1':1.722403e+00}
T4 = {'T':5.608734e+03,'rho':20985020601850.918,'H':1.877820e+13,'HI':1.844920e+13,
         'HII':3.290003e+11,'HeI':1.877820e+12,'HeII':1.805179e+01, 'HeIII':6.798283e-38,'b1':1.007221e+01}
T5 = {'T':6.622204e+03,'rho':870351810762.43091,'H':5.768361e+11,'HI':3.410040e+11,
         'HII':2.358321e+11,'HeI':7.965357e+02,'HeII':7.965357e+02, 'HeIII':4.015894e-29,'b1':4.707660e+00}
T6 = {'T':6.461409e+04,'rho':28080775459.989269,'H':1.220905e+10,'HI':2.959773e+02,
         'HII':1.220905e+10,'HeI':1.968145e-03,'HeII':4.516401e+04, 'HeIII':1.220860e+09,'b1':2.069515e+07}
T7 = {'T':3.698417e+05,'rho':4559257602.1237888,'H':1.982286e+09,'HI':1.561717e+00,
         'HII':1.982286e+09,'HeI':2.980232e-08,'HeII':5.620723e-01, 'HeIII':1.982286e+08,'b1':6.361830e+08}
b1_text = [T['b1'] for T in [T1,T2,T3,T4,T5,T6,T7]]

#T8 = {'T':3.698417e+05,'rho':4559257602.1237888,'H':1.982286e+09,'HI':1.561717e+00,
#         'HII':1.982286e+09,'HeI':2.980232e-08,'HeII':5.620723e-01, 'HeIII':1.982286e+08,'b1':}
         ################################################################## aqui  me quede
for i in [T1,T2,T3,T4,T5,T6,T7]:
    r = i['HI'] + 2*i['HII'] + i['HeI'] + 2*i['HeII'] + 3*i['HeIII']
    print(r,i['rho'],i['T'])

####Percentage of ionization
T1hi = T1['HI']/T1['H']#percentage of ionization fo HI in Temperature1 test
T2hi = T2['HI']/T2['H']
T3hi = T3['HI']/T3['H']
T4hi = T4['HI']/T4['H']
T5hi = T5['HI']/T5['H']
T6hi = T6['HI']/T6['H']
T7hi = T7['HI']/T7['H']

T1hii = T1['HII']/(T1['H'])
T2hii = T2['HII']/(T2['H'])
T3hii = T3['HII']/(T3['H'])
T4hii = T4['HII']/(T4['H'])
T5hii = T5['HII']/(T5['H'])
T6hii = T6['HII']/(T6['H'])
T7hii = T7['HII']/(T7['H'])

T1hei = T1['HeI']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2hei = T2['HeI']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3hei = T3['HeI']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4hei = T4['HeI']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5hei = T5['HeI']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6hei = T6['HeI']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7hei = T7['HeI']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])

T1heii = T1['HeII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2heii = T2['HeII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3heii = T3['HeII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4heii = T4['HeII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5heii = T5['HeII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6heii = T6['HeII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7heii = T7['HeII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])

T1heiii = T1['HeIII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
T2heiii = T2['HeIII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
T3heiii = T3['HeIII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
T4heiii = T4['HeIII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
T5heiii = T5['HeIII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
T6heiii = T6['HeIII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
T7heiii = T7['HeIII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])

hi = [T1hi,T2hi,T3hi,T4hi,T5hi,T6hi,T7hi]
hii = [T1hii,T2hii,T3hii,T4hii,T5hii,T6hii,T7hii]
hei = [T1hei,T2hei,T3hei,T4hei,T5hei,T6hei,T7hei]
heii = [T1heii,T2heii,T3heii,T4heii,T5heii,T6heii,T7heii]
heiii = [T1heiii,T2heiii,T3heiii,T4heiii,T5heiii,T6heiii,T7heiii]
t = [T1['T'],T2['T'],T3['T'],T4['T'],T5['T'],T6['T'],T7['T']]


HI = []
HII = []
HeI = []
HeII = []
HeIII = []
n_e = []
N = 1e16
epsilon = 1e13
for T in temperatures:
    hI, hII, heI, heII, heIII,ne = sahaH(T,N, epsilon)
    HI.append(hI)
    HII.append(hII)
    HeI.append(heI)
    HeII.append(heII)
    HeIII.append(heIII)
    n_e.append(ne)
    #print h
plt.plot(t,hi,"-",label='HI')
plt.scatter(t,hii,marker="v",label='HII')
plt.scatter(t,hei,marker="1",label='HeI',s=60)
plt.scatter(t,heii,marker="2",label='HeII',s=60)
plt.scatter(t,heiii,marker="3",label='HeIII',s=60) 
for i in range(7):
     plt.text(t[i],hi[i],b1_text[i],fontsize=10)
plt.plot(temperatures,HI,label='HI',linestyle='dashed')
plt.plot(temperatures,HII,label='HII',linestyle='dashed')
plt.plot(temperatures,HeI,label='HeI',linestyle='dashed')
plt.plot(temperatures,HeII,label='HeII',linestyle='dashed')
plt.plot(temperatures,HeIII,label='HeIII',linestyle='dashed')
plt.title('Ecuacion de Saha')
plt.xlabel('Temperatura [K]')
plt.ylabel('%')
plt.legend()
plt.xscale('log')
plt.show()

#plt.plot(temperatures, n_e)
#plt.show()
