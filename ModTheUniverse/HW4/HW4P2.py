#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:27:21 2018

@author: sharleenprice
"""
import homework4 as hw4
import numpy as np
import matplotlib.pyplot as plt
import math


mass_plot =[]
r_plot =[]
Fe = hw4.Planet_Model(8300,0.00345,0.528)
for x in np.arange(11,14.3,0.2):
    y_0=np.array([10**x,0])
    
    dr= 6371
    r = 6371
    earth_r=6371000
    earth_m = 5.972*10**24
    while True:
            p=y_0[0]
            m=y_0[1]
            y=hw4.RK4(Fe.derivatives,y_0,r,dr)
            r=r+dr
            y_0=y

            if (p+10*Fe.dPdr(p,r,m)*dr) <=0:
                dr=1000
        
            if (p+2*Fe.dPdr(p,r,m)*dr < 0):
                mass_plot.append(math.log(m/earth_m))
                r_plot.append(math.log(r/earth_r))
                break
  
          
plt.plot(r_plot, mass_plot)
plt.xlabel("Log of Radius Ratios (Radius/Earth Radius)")
plt.ylabel("Log of Mass Ratios (Mass/Earth Mass)")
plt.title("Fe Mass vs Radius")
            


