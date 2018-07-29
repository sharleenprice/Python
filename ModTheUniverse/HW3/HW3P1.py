#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:54:04 2018

@author: sharleenprice
"""

#import kplr
import numpy as np
import matplotlib.pyplot as plt
from Problem4PS1 import LoopThroughFlux2
from HW2P2 import LoopFlux

"""
Problem 1
"""

time, flux, flux_err = np.loadtxt("KOI97.01_1.out", unpack=True)

plt.errorbar(time,flux, yerr=flux_err, fmt=".",color="b")
plt.xlabel("Time")
plt.ylabel("Flux")
plt.title("Kepler's Plot")

"""
Problem 2 part a
"""
ex_index=[]
for i in range(0,len(flux)):
    ex_index.append(i)
all_index=np.array(ex_index) #creates array of all indexes
    
index1= np.where((time>124.2) & (time<124.8)) #index of first eclipse
index2= np.where((time>128.5) & (time<129)) #index of second eclipse
ec_time=time[index1] #time of first eclipse
z_ec = (ec_time-124.5)/0.1 # z of first eclipse


ex_eclipse1=np.delete(all_index,index1)#creates array without first eclipse
ex_eclipses=np.delete(ex_eclipse1,index2)#creates array without either eclipse

mean=np.nanmean(flux[ex_eclipses]) #mean of unobscured flux
ratio=flux[index1]/mean #ratio of obscured vs unobscured flux

fe_flux,z=LoopThroughFlux2(0.085,-1.7,1.7,0.15) #flux and z from problemset 1

                          
fig = plt.figure()
ax=plt.subplot(111)


kplr_data=ax.plot(z_ec,ratio, label="Kepler Data")#blue kplr data plot
ratio_data=ax.plot(z,fe_flux, label="Pset 1")#yellow problem set 1 plot


"""
Problem 2 part b
"""
fflux,zfl=LoopFlux(.065,-2,2,.1,10**4)
r_data=ax.plot(zfl,fflux, label="Pset 2") #green plot using simpsons method


plt.xlabel("Z(t)")
plt.ylabel("Flux Ratio")
plt.title("Eclipse 1")
ax.legend()
plt.show()























        






