#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:46:54 2018

@author: sharleenprice
"""

import math
import numpy as np
#import kplr
import matplotlib.pyplot as plt
import scipy 


p=0.0775
tau=0.1
t_0=124.5

"""Problem 1"""

time, flux, flux_err = np.loadtxt("KOI97.01_1.out", unpack=True)

index1= list(np.where((time>124) & (time<125))) #eclipse 
          
ec_time=list(time[index1])
ec_flux = list(flux[index1])
ec_error = list(flux_err[index1])
eclipse_time=time[index1]

unobscured_flux = list(flux[index1])

for i in range (5): 
    exclude_flux = []
    flux_mean = np.mean(unobscured_flux) #mean unobscured flux
    flux_std = np.std(unobscured_flux)
    for j in range(len(unobscured_flux)):
        if (abs(unobscured_flux[j]-flux_mean)/flux_std > 2):
            exclude_flux.append(j)  #index of eclipse
 
    unobscured_flux = np.delete(unobscured_flux,exclude_flux) #remove eclipse
    



ec_flux= ec_flux/flux_mean #normalized unobscured flux
ec_error= ec_error/flux_mean #normalized unobscured error




import my_transit

def I(r):
    '''A Limb-darkening function'''
    mu = (1 - (r**2))**(0.5)
    return 1 - (1 - (mu**(0.5)))

def func1(r, p, z):
    return I(r) * (1 - my_transit.delta(p,r,abs(z))) * 2 * r

def func2(r, p, z):
    return I(r) * 2 * r

    
def F(p,z):
    top_f, error1 = scipy.integrate.quad(func1,0,1,args=(p,z))
    bottom_f, error2 = scipy.integrate.quad(func2,0,1,args=(p,z))
    f=top_f/bottom_f

    return f

flux_ratio = []
for i in eclipse_time:        
    z=(i-t_0)/tau
    flux_ratio.append(F(p,z))
    
"""Problem 2"""
#plt.plot(eclipse_time, flux_ratio) #f(p,z) model
#plt.errorbar(eclipse_time, ec_flux, ec_error) #fit

chi2=sum(((ec_flux-flux_ratio)/ec_error)**2)
N= len(ec_flux)
M=3
dof=N-M
p_value=scipy.special.gammaincc(dof/2,chi2/2)
print("p value: ", p_value)



"""Problem 3"""
lowest = 100000
lowest_ratio = []
all_chisq = []
all_tao = []
for j in np.arange(0.08,0.13,0.001):
    fluxratio2 = []
    for i in eclipse_time:        
        z=(i-t_0)/j
        fluxratio2.append(F(p,z))
    chisq=sum(((ec_flux-fluxratio2)/ec_error)**2)
    all_chisq.append(chisq)
    all_tao.append(j)
    if(lowest>chisq):
        lowest=chisq
        lowest_tau = j
        lowest_ratio = fluxratio2

print("Minimum chisq: ", lowest)
print("Corresponding tau: ", lowest_tau)
p_value2=scipy.special.gammaincc(dof/2,lowest/2)
print("Corresponding p value: ", p_value2)

plt.plot(all_tao, all_chisq)

sigma = lowest+1
#plt.plot(all_tao,sigma)
#plt.axhline(y=sigma, linestyle = "-")
sigma_tao=[]
for i in range(len(lowest_ratio)):
    if lowest_ratio[i]==sigma:
        sigma_tao=all_tao[i]

print(sigma_tao)