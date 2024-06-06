#!/usr/bin/env python3

from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt


#print pi
h = 6.6e-27
#print e
m_e =9.1e-28
Boltzmann = 8.6e-5
K = 1.38e-16



C = np.log10(2.0*(((2.0*pi*m_e*K) / (h**2))**(3./2)))
print('C',C)


def PsiHII(T,n_e):
    return C - np.log10(n_e)+ np.log10(0.5)+  1.5*np.log10(T)- 13.6*(5040.0/T) 

#def PsiHeI(T, n_e):
#    return C - np.log10(n_e) + np.log(/)

def PsiHeII(T,n_e):
    return C - np.log10(n_e) +  1.5*np.log10(T)- 24.59*(5040.0/T)

def PsiHeIII(T,n_e):
    return C - np.log10(n_e)+ np.log10(2)+  1.5*np.log10(T) - 54.59*(5040.0/T) 


def sahaH(T,N,epsilon):
    H = 0.9*N
    He = 0.1*N
    HI = (H * 0.5)  #####aqui me quede corrigiendo
	
    #n_e = 1e10
    error = 1e40
    
    while(True): 
        #a = (   (2.0*pi*m_e*Boltzmann*T) / (h**2) )**(3./2)
        #b = np.exp((-13.6)/(Boltzmann*T )) #se multiplica xi_H por e para pasar de ev a J

        #HII = pow(10, Psi(T,n_e))*HI  #(2.0*a*b/n_e)*HI
        #print T, Psi(T,n_e),  pow(10, Psi(T,n_e)), n_e
        #if HII > H:
        #    HII=H
        #n0 = n_e
        #n_e= HII

        PSIHII = pow(10, PsiHII(T,n_e))
        PSIHeII = pow(10, PsiHeII(T,n_e))
        PSIHeIII = pow(10, PsiHeIII(T,n_e))
	##################################
        HI = (H) / (1.0 + PSIHII)
        HII = H - HI
        HeI = He/(1.0+PSIHeII*(1+PSIHeII))
        HeII =  He/(1/PSIHeII)
        HeIII = PSIHeIII * HeII
	###################################
        n0 = n_e
        n_e = HII+ HeII + 2*HeIII
        n_e = (n_e + n0)/2.0        
        error = abs(n0-n_e) #### aqui podria estar la clave
        RHI = HI/(0.9*N)
        RHII = HII/(0.9*N)
        RHeI = HeI/(0.1*N)
        RHeII = HeII/(0.1*N)
        RHeIII = HeIII/(0.1*N)
        #print(error,'error')
        if error <= epsilon:
            print(T,RHI,RHII,RHeI,RHeII,RHeIII)
            break

        
    return RHI,RHII,RHeI,RHeII,RHeIII

temperatures =  np.arange(1000,50000,1000)
#temperatures = [10000.0]
#sahaH(5000)
HI = []
HII = []
HeI = []
HeII = []
HeIII = []
N = 1e16
epsilon = 1e11#1e13
for T in temperatures:
    hI, hII, heI, heII, heIII = sahaH(T,N, epsilon)
    HI.append(hI)
    HII.append(hII)
    HeI.append(heI)
    HeII.append(heII)
    HeIII.append(heIII)
    #print h
plt.plot(temperatures,HI,label='HI')
plt.plot(temperatures,HII,label='HII')
plt.plot(temperatures,HeI,label='HeI')
plt.plot(temperatures,HeII,label='HeII')
plt.plot(temperatures,HeIII,label='HeIII')
plt.legend()
#plt.xscale('log')
plt.show()
