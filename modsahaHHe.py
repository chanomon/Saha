#!/usr/bin/env python3
#######ecuacion de Saha para H y He usando modelo de tesis de maestria de V de la Luz

from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["savefig.directory"] = './'


#############constants
h = 6.626e-27
m_e =9.1e-28

k = 1.38064852e-16
C = np.log10(2.0*(((2.0*pi*m_e*k) / (h**2))**(3./2)))


#def PsiHI(T, n_e):
#    return C - np.log10(n_e) + no.log()

def PsiHII(T,n_e):
    return C - np.log10(n_e)+ np.log10(0.5)+  1.5*np.log10(T)- 13.6*(5040.0/T) 

def PsiHeII(T,n_e):
    return C - np.log10(n_e) +  1.5*np.log10(T)- 24.59*(5040.0/T)

def PsiHeIII(T,n_e):
    return C - np.log10(n_e)+ np.log10(0.5) +  1.5*np.log10(T) - 54.59*(5040.0/T)


def saha(T,N):
    
    #N = 1e16
    H = N*.9#N
    He = 0.1*N
    HI = (H * 0.5)
    #HII = HI*0.1
    #HeI = He * 0.1
    #HeII = HeI 
    #HeIII = HeII
   
    n_e = HI#+HeII+2*HeIII#ne
    #error = 1e40
    
    while(True): 
       
	#print n_e
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
        ne = n_e
        n_e = (n_e + n0)/2.0        
        error = abs(n0-n_e) 
        
        print(error,ne/100.,n0)
        if error <= ne/100.:
            
            break

    print('1')
    return HI,HII,HeI,HeII,HeIII,n_e
