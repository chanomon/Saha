#!/usr/bin/env python3

from scipy.constants import pi#,h,epsilon_0,e,m_e,Boltzmann
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["savefig.directory"] = './'


#print pi
h = 6.6e-27 #m^2 kg/s
#print e
m_e =9.1e-28
Boltzmann = 8.6e-5 #Boltzmann in eV/K
K = 1.38e-16 #Boltzmann in J/K



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

if __name__ == '__main__':

    temperatures =  np.arange(4000,21000,1000)##80000
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


    T11= {'T':8.319990e+03,'rho':1.3598838416081920E+017,'H':1.226102e+17,'HI':1.214931e+17,
            'HII':1.117105e+15,'HeI':1.226102e+16,'HeII':1.000492e+08, 'HeIII':1.226102e+17,'b1':1.000000e+00}
    T22= {'T':7.610000e+03,'rho':1.2990692270511490E+017,'H':1.177112e+17,'HI':1.172866e+17,
            'HII':4.245889e+14,'HeI':1.177112e+16,'HeII':9.054896e+06, 'HeIII':9.054896e+06,'b1':1.000000e+00}
    T33= {'T':6.910000e+03,'rho':1.2497481678350666E+017,'H':1.134900e+17,'HI':1.133541e+17,
            'HII':1.358534e+14,'HeI':1.134900e+16,'HeII':5.296624e+05, 'HeIII':1.081089e-27,'b1':1.000000e+00}
    T44= {'T':6.419993e+03,'rho':1.1436583510218205E+017,'H':1.039222e+17,'HI':1.038707e+17,
            'HII':5.145542e+13,'HeI':1.039222e+16,'HeII':4.904145e+04, 'HeIII':2.211169e-31,'b1':1.000000e+00}
    T55= {'T':5.839993e+03,'rho':90210798156905680.,'H':8.199834e+16,'HI':8.198570e+16,
            'HII':1.263154e+13,'HeI':8.199834e+15,'HeII':1.675067e+03, 'HeIII':1.544291e-36,'b1':1.012878e+00}
    T66= {'T':5.454994e+03,'rho':67292174531525320.,'H':6.117096e+16,'HI':6.116685e+16,
            'HII':4.114114e+12,'HeI':6.117096e+15,'HeII':1.168886e+02, 'HeIII':1.536597e-40,'b1':1.076110e+00}
    T77={'T':4.169995e+03,'rho':2054000143651526.5,'H':1.867270e+15,'HI':1.867266e+15,
            'HII':3.571793e+09,'HeI':1.867270e+14,'HeII':7.568840e-05, 'HeIII':6.785565e-60,'b1':2.982902e-01}
    T88={'T':6.149993e+03,'rho':9085542501650.3555,'H':7.614531e+12,'HI':6.904973e+12,
            'HII':7.095582e+11,'HeI':7.614531e+11,'HeII':3.117520e+02, 'HeIII':1.143098e-32,'b1':9.905690e+00}
    T99={'T':9.499989e+03,'rho':185865647373.76715,'H':8.921976e+10,'HI':1.498961e+09,
            'HII':8.772080e+10,'HeI':8.918869e+09,'HeII':3.106368e+06, 'HeIII':4.042744e-14,'b1':3.069189e+01}
    TAA={'T':1.069999e+04,'rho':169923704232.12473,'H':8.134339e+10,'HI':9.165050e+08,
            'HII':8.042689e+10,'HeI':8.115252e+09,'HeII':1.908722e+07, 'HeIII':9.988068e-11,'b1':4.454739e+01}
    TBB={'T':1.229999e+04,'rho':152650086425.49768,'H':7.285724e+10,'HI':4.848717e+08,
            'HII':7.237237e+10,'HeI':7.150980e+09,'HeII':1.347447e+08, 'HeIII':3.799106e-07,'b1':7.528679e+01}
    TCC={'T':1.849998e+04,'rho':107008160527.21744,'H':4.867734e+10,'HI':3.256713e+06,
            'HII':4.867408e+10,'HeI':7.872827e+07,'HeII':4.789005e+09, 'HeIII':5.441422e+02,'b1':7.520729e+03}
    TDD={'T':2.099998e+04,'rho':94199720507.881134,'H':4.282022e+10,'HI':4.092318e+05,
            'HII':4.281981e+10,'HeI':4.422577e+06,'HeII':4.277527e+09, 'HeIII':7.169908e+04,'b1':7.169908e+04}


    #b1_text = [T['b1'] for T in [T1,T2,T3,T4,T5,T6,T7]]
    b1__text = [T['b1'] for T in [T11,T22,T33,T44,T55,T66,T77,T88,T99,TAA,TBB,TCC,TDD]]
    #T8 = {'T':3.698417e+05,'rho':4559257602.1237888,'H':1.982286e+09,'HI':1.561717e+00,
    #         'HII':1.982286e+09,'HeI':2.980232e-08,'HeII':5.620723e-01, 'HeIII':1.982286e+08,'b1':}
            ################################################################## aqui  me quede
    for i in [T1,T2,T3,T4,T5,T6,T7]:
        r = i['HI'] + 2*i['HII'] + i['HeI'] + 2*i['HeII'] + 3*i['HeIII']
        #print(r,i['rho'],i['T'])
    TT = [t['T'] for t in [T77,T66,T55,T88,T44,T33,T22,T11,T99,TAA,TBB,TCC,TDD]]
    ####Percentage of ionization
    T1hi = T1['HI']/T1['H']#percentage of ionization fo HI in Temperature1 test
    T2hi = T2['HI']/T2['H']
    T3hi = T3['HI']/T3['H']
    T4hi = T4['HI']/T4['H']
    T5hi = T5['HI']/T5['H']
    T6hi = T6['HI']/T6['H']
    T7hi = T7['HI']/T7['H']
    T11hi= T11['HI']/T11['H']
    T22hi= T22['HI']/T22['H']
    T33hi= T33['HI']/T33['H']
    T44hi= T44['HI']/T44['H']
    T55hi= T55['HI']/T55['H']
    T66hi= T66['HI']/T66['H']
    T77hi= T77['HI']/T77['H']
    T88hi= T88['HI']/T88['H']
    T99hi= T99['HI']/T99['H']
    TAAhi= TAA['HI']/TAA['H']
    TBBhi= TBB['HI']/TBB['H']
    TCChi= TCC['HI']/TCC['H']
    TDDhi= TDD['HI']/TDD['H']

    T1hii = T1['HII']/(T1['H'])
    T2hii = T2['HII']/(T2['H'])
    T3hii = T3['HII']/(T3['H'])
    T4hii = T4['HII']/(T4['H'])
    T5hii = T5['HII']/(T5['H'])
    T6hii = T6['HII']/(T6['H'])
    T7hii = T7['HII']/(T7['H'])
    T11hii= T11['HII']/(T11['H'])
    T22hii= T22['HII']/(T22['H'])
    T33hii= T33['HII']/(T33['H'])
    T44hii= T44['HII']/(T44['H'])
    T55hii= T55['HII']/(T55['H'])
    T66hii= T66['HII']/(T66['H'])
    T77hii= T77['HII']/(T77['H'])
    T88hii= T88['HII']/(T88['H'])
    T99hii= T99['HII']/(T99['H'])
    TAAhii= TAA['HII']/(TAA['H'])
    TBBhii= TBB['HII']/(TBB['H'])
    TCChii= TCC['HII']/(TCC['H'])
    TDDhii= TDD['HII']/(TDD['H'])

    T1hei = T1['HeI']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
    T2hei = T2['HeI']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
    T3hei = T3['HeI']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
    T4hei = T4['HeI']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
    T5hei = T5['HeI']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
    T6hei = T6['HeI']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
    T7hei = T7['HeI']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
    T11hei= T11['HeI']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
    T22hei= T22['HeI']/(T22['HeI'] + T22['HeII'] + T22['HeIII'])
    T33hei= T33['HeI']/(T33['HeI'] + T33['HeII'] + T33['HeIII'])
    T44hei= T44['HeI']/(T44['HeI'] + T44['HeII'] + T44['HeIII'])
    T55hei= T55['HeI']/(T55['HeI'] + T55['HeII'] + T55['HeIII'])
    T66hei= T66['HeI']/(T66['HeI'] + T66['HeII'] + T66['HeIII'])
    T77hei= T77['HeI']/(T77['HeI'] + T77['HeII'] + T77['HeIII'])
    T88hei= T88['HeI']/(T88['HeI'] + T88['HeII'] + T88['HeIII'])
    T99hei= T99['HeI']/(T99['HeI'] + T99['HeII'] + T99['HeIII'])
    TAAhei= TAA['HeI']/(TAA['HeI'] + TAA['HeII'] + TAA['HeIII'])
    TBBhei= TBB['HeI']/(TBB['HeI'] + TBB['HeII'] + TBB['HeIII'])
    TCChei= TCC['HeI']/(TCC['HeI'] + TCC['HeII'] + TCC['HeIII'])
    TDDhei= TDD['HeI']/(TDD['HeI'] + TDD['HeII'] + TDD['HeIII'])

    T1heii = T1['HeII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
    T2heii = T2['HeII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
    T3heii = T3['HeII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
    T4heii = T4['HeII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
    T5heii = T5['HeII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
    T6heii = T6['HeII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
    T7heii = T7['HeII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
    T11heii= T11['HeII']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
    T22heii= T22['HeII']/(T22['HeI'] + T22['HeII'] + T22['HeIII'])
    T33heii= T33['HeII']/(T33['HeI'] + T33['HeII'] + T33['HeIII'])
    T44heii= T44['HeII']/(T44['HeI'] + T44['HeII'] + T44['HeIII'])
    T55heii= T55['HeII']/(T55['HeI'] + T55['HeII'] + T55['HeIII'])
    T66heii= T66['HeII']/(T66['HeI'] + T66['HeII'] + T66['HeIII'])
    T77heii= T77['HeII']/(T77['HeI'] + T77['HeII'] + T77['HeIII'])
    T88heii= T88['HeII']/(T88['HeI'] + T88['HeII'] + T88['HeIII'])
    T99heii= T99['HeII']/(T99['HeI'] + T99['HeII'] + T99['HeIII'])
    TAAheii= TAA['HeII']/(TAA['HeI'] + TAA['HeII'] + TAA['HeIII'])
    TBBheii= TBB['HeII']/(TBB['HeI'] + TBB['HeII'] + TBB['HeIII'])
    TCCheii= TCC['HeII']/(TCC['HeI'] + TCC['HeII'] + TCC['HeIII'])
    TDDheii= TDD['HeII']/(TDD['HeI'] + TDD['HeII'] + TDD['HeIII'])

    T1heiii = T1['HeIII']/(T1['HeI'] + T1['HeII'] + T1['HeIII'])
    T2heiii = T2['HeIII']/(T2['HeI'] + T2['HeII'] + T2['HeIII'])
    T3heiii = T3['HeIII']/(T3['HeI'] + T3['HeII'] + T3['HeIII'])
    T4heiii = T4['HeIII']/(T4['HeI'] + T4['HeII'] + T4['HeIII'])
    T5heiii = T5['HeIII']/(T5['HeI'] + T5['HeII'] + T5['HeIII'])
    T6heiii = T6['HeIII']/(T6['HeI'] + T6['HeII'] + T6['HeIII'])
    T7heiii = T7['HeIII']/(T7['HeI'] + T7['HeII'] + T7['HeIII'])
    T11heiii= T11['HeIII']/(T11['HeI'] + T11['HeII'] + T11['HeIII'])
    T22heiii= T22['HeIII']/(T22['HeI'] + T22['HeII'] + T22['HeIII'])
    T33heiii= T33['HeIII']/(T33['HeI'] + T33['HeII'] + T33['HeIII'])
    T44heiii= T44['HeIII']/(T44['HeI'] + T44['HeII'] + T44['HeIII'])
    T55heiii= T55['HeIII']/(T55['HeI'] + T55['HeII'] + T55['HeIII'])
    T66heiii= T66['HeIII']/(T66['HeI'] + T66['HeII'] + T66['HeIII'])
    T77heiii= T77['HeIII']/(T77['HeI'] + T77['HeII'] + T77['HeIII'])
    T88heiii= T88['HeIII']/(T88['HeI'] + T88['HeII'] + T88['HeIII'])
    T99heiii= T99['HeIII']/(T99['HeI'] + T99['HeII'] + T99['HeIII'])
    TAAheiii= TAA['HeIII']/(TAA['HeI'] + TAA['HeII'] + TAA['HeIII'])
    TBBheiii= TBB['HeIII']/(TBB['HeI'] + TBB['HeII'] + TBB['HeIII'])
    TCCheiii= TCC['HeIII']/(TCC['HeI'] + TCC['HeII'] + TCC['HeIII'])
    TDDheiii= TDD['HeIII']/(TDD['HeI'] + TDD['HeII'] + TDD['HeIII'])

    hi = [T1hi,T2hi,T3hi,T4hi,T5hi,T6hi,T7hi]
    h_i = [T11hi,T22hi,T33hi,T44hi,T55hi,T66hi,T77hi,T88hi,T99hi,TAAhi,TBBhi,TCChi,TDDhi]
    hii = [T11hii,T22hii,T33hii,T44hii,T55hii,T66hii,T77hii,T88hii,T99hii,TAAhii,TBBhii,TCChii,TDDhii]
    hei = [T11hei,T22hei,T33hei,T44hei,T55hei,T66hei,T77hei,T88hei,T99hei,TAAhei,TBBhei,TCChei,TDDhei]
    heii = [T11heii,T22heii,T33heii,T44heii,T55heii,T66heii,T77heii,T88heii,T99heii,TAAheii,TBBheii,TCCheii,TDDheii]
    heiii = [T11heiii,T22heiii,T33heiii,T44heiii,T55heiii,T66heiii,T77heiii,T88heiii,T99heiii,TAAheiii,TBBheiii,TCCheiii,TDDheiii]
    t = [T1['T'],T2['T'],T3['T'],T4['T'],T5['T'],T6['T'],T7['T']]
    t_ = [T11['T'],T22['T'],T33['T'],T44['T'],T55['T'],T66['T'],T77['T'],
        T88['T'],T99['T'],TAA['T'],TBB['T'],TCC['T'],TDD['T']]
    print(hi)

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

    #################### INTERPOLATE ####################
    new_t = np.arange(1000, 20500, 500)
    n_h_i = np.interp(new_t, t_, h_i)
    n_hii = np.interp(new_t, t_, hii)
    n_he_i = np.interp(new_t, t_, hei)
    n_heii = np.interp(new_t, t_, heii)
    n_heiii = np.interp(new_t, t_, heiii)


    #######################derivate#####################
    d_h_i = np.gradient(np.array(h_i))
    d_hii = np.gradient(np.array(hii))
    d_hei = np.gradient(np.array(hei))
    d_heii = np.gradient(np.array(heii))
    d_heiii = np.gradient(np.array(heiii))
    d_HI = np.gradient(np.array(HI))
    d_HII = np.gradient(np.array(HII))
    d_HeI = np.gradient(np.array(HeI))
    d_HeII = np.gradient(np.array(HeII))
    d_HeIII = np.gradient(np.array(HeIII))

    d = [x **2 for x in d_h_i]
    ############################PLOT############################
    fig3, ax3 = plt.subplots()

    ax3.plot(TT,hei,label="HeI, Tonalli",linestyle="dashed")
    ax3.plot(temperatures,HeI,label='HeI SAHA',)
    ax3.set_title('Helio')
    ax3.set_xlabel('Temperatura [K]')
    ax3.set_ylabel('%')
    ax3.legend()

    fig4, ax4 = plt.subplots()
    ax4.plot(TT,heii,linestyle="dashed",label="HeII, Tonalli",)
    ax4.plot(temperatures,HeII,label='HeII SAHA',)
    ax4.set_title('Helio')
    ax4.set_xlabel('Temperatura [K]')
    ax4.set_ylabel('%')
    ax4.legend()

    fig5, ax5 = plt.subplots()
    ax5.plot(TT,heiii,label="HeIII Tonalli",linestyle="dashed")
    ax5.plot(temperatures,HeIII,label='HeIII SAHA',)
    ax5.set_title('Helio')
    ax5.set_xlabel('Temperatura [K]')
    ax5.set_ylabel('%')
    ax5.legend()
    #plt.xscale('log')



    fig1, ax1 = plt.subplots()
    #plt.plot(t,hi,"-",label='HI')
    #print((t_),(hii))

    #plt.plot(new_t,n_h_i,linestyle="dotted",c='tab:blue',label="HI, NLTE")

    #ax1.plot(t_,d_hii,linestyle="dashed",c='tab:blue',label='HII, NLTE')
    #plt.plot(new_t,n_hii,linestyle="dashed",c='tab:blue',label="HII, NLTE")
    #plt.scatter(new_t,n_hii,marker="o",c='tab:blue',)
    #for i in range(len(b1__text)):
        #plt.text(t[i],hi[i],b1_text[i],fontsize=10)
    #     ax1.text(TT[i],h_i[i],"%.1f" % b1__text[i],fontsize=10,)
    ax1.plot(temperatures,HI,label='HI SAHA',color='tab:blue')
    ax1.plot(TT,h_i,label='HI, Tonalli',color='blue',linestyle="dashed")
    colors = ["blue","blue","blue","blue","blue","blue","green","red","red","red","red","red","red"]
    ax1.scatter(TT,h_i,marker="o", label='b1',c=colors)
    ax1.set_title('Hidrógeno')#Ecuacion de Saha')
    ax1.set_xlabel('Temperatura [K]')
    ax1.set_ylabel('%')
    ax1.legend()


    #fig2, ax2 = plt.subplots()
    ax1.plot(temperatures,HII,c='tab:orange',label="HII SAHA")
    ax1.plot(TT,hii,c='red',label='HII, Tonalli',linestyle="dashed")
    #plt.scatter(temperatures,HI,label='HI, NLTE',marker="o",c='tab:red',)
    #plt.xscale('log')
    ax1.set_title('Hidrógeno')#Ecuacion de Saha')
    ax1.set_xlabel('Temperatura [K]')
    ax1.set_ylabel('%')
    ax1.legend()




    #plt.plot(temperatures, n_e)
    plt.show()
