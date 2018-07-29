#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:13:04 2018

@author: sharleenprice spp2122
"""

import homework4 as hw4
import numpy as np
import matplotlib.pyplot as plt
import math
mass_plot =[]
r_plot =[]
mass2_plot =[]
r2_plot =[]
mass_plot3 =[]
r_plot3 =[]
earth_r=6371000
earth_m = 5.972*10**24

""" Fe """
Fe = hw4.Planet_Model(8300,0.00345,0.528)
for l in np.arange(11,14.3,0.2):
    y_03=np.array([10**l,0])
    
    dr= 6371
    r = 6371
    
    while True:
            p=y_03[0]
            m=y_03[1]
            y=hw4.RK4(Fe.derivatives,y_03,r,dr)
            r=r+dr
            y_03=y
            

            if (p+10*Fe.dPdr(p,r,m)*dr) <=0:
                dr=1000
        
            if (p+2*Fe.dPdr(p,r,m)*dr < 0):
                mass_plot3.append(math.log(m/earth_m))
                r_plot3.append(math.log(r/earth_r))
                break
  
         
plt.plot(r_plot3, mass_plot3, label="Fe")
plt.xlabel("Log of Radius Ratio (Radius/Earth Radius)")
plt.ylabel("Log of Mass Ratio (Mass/Earth Mass)")
plt.title("Mass vs Radius")
                        
                        
""" H20 """
H20 = hw4.Planet_Model(1460,0.00311,0.513)
for x in np.arange(10,13.15,0.1):
    y_0=np.array([10**x,0])
    
    dr= 6371
    r = 6371
    earth_r=6371000
    earth_m = 5.972*10**24
    while True:
        p=y_0[0]
        m=y_0[1]
        y=hw4.RK4(H20.derivatives,y_0,r,dr)
        r=r+dr
        y_0=y

        if (p+10*H20.dPdr(p,r,m)*dr) <=0:
            dr=1000
    
        if (p+2*H20.dPdr(p,r,m)*dr < 0):
            mass_plot.append(math.log((m/earth_m)))
            r_plot.append(math.log(r/earth_r))
            
            break

plt.plot(r_plot, mass_plot, label="H2O")

""" MgSiO3 """

MgSiO3= hw4.Planet_Model(4100,0.00161,0.541)
for z in np.arange(10.6,13.7,0.2):
    y_02=np.array([10**z,0])
    
    dr= 6371
    r = 6371

    while True:
            
            p=y_02[0]
            m=y_02[1]
            y=hw4.RK4(MgSiO3.derivatives,y_02,r,dr)
            r=r+dr
            y_02=y
            
    
            if (p+10*MgSiO3.dPdr(p,r,m)*dr) <=0:
                dr=1000
        
            if (p+2*MgSiO3.dPdr(p,r,m)*dr < 0):
               
                mass2_plot.append(math.log(m/earth_m))
                r2_plot.append(math.log(r/earth_r))
                break
            
plt.plot(r2_plot, mass2_plot, label="MgSiO3")
  

         
"""Kepler-102 f"""
plt.errorbar(math.log(0.88), math.log(0.62), math.log(3.30),marker='o', markersize=3, color="red")

"""KOI-1612.01"""
plt.errorbar(math.log(0.82), math.log(0.48), math.log(3.20),marker='o', markersize=3, color="red")

"""Kepler-37 b"""
plt.errorbar(math.log(0.32), math.log(2.78), math.log(3.70),marker='o', markersize=3, color="red", label="Exoplanets")

""" Mercury """
plt.plot(math.log(0.383/2), math.log(0.0553), marker='o', markersize=3, color="blue", label="Terrestrial Planets")

""" Venus """
plt.plot(math.log(0.949/2), math.log(0.815), marker='o', markersize=3, color="blue" )

""" Earth """
plt.plot(math.log(1), math.log(1), marker='o', markersize=3, color="blue")

""" Mars """
plt.plot(math.log(0.532/2), math.log(0.107), marker='o', markersize=3, color="blue")
plt.legend(loc = "lower right")



