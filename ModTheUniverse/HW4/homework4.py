#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:27:52 2018

@author: sharleenprice spp2122
"""

import numpy as np
import matplotlib.pyplot as plt
G = 6.67408*10**-11


class Planet_Model(object):
    
    def __init__(self, rho0,c,n):
        self.rho0 = rho0
        self.c = c
        self.n = n
      
    def density(self, P):
        density = self.rho0 +self.c*P**self.n
        return density
        
    def dPdr(self,P,r,m):
        dpdr = -1*G*self.density(P)*m/r**2
        return dpdr

    def dmdr(self,P,r):
        dmdr = 4*np.pi*self.density(P)*r**2
        return dmdr

    def derivatives(self,y,r):
        p=y[0]
        m=y[1]
        dp_dr=self.dPdr(p,r,m)
        dm_dr=self.dmdr(p,r)
        return(np.array([dp_dr,dm_dr]))
    
def RK4(f,y,r,dr):
    k1=f(y,r)*dr
    k2=f(y+k1/2,r+dr/2)*dr
    k3=f(y+k2/2,r+dr/2)*dr
    k4=f(y+k3,r+dr)*dr
    y = y+1/6*(k1+(2*k2)+(2*k3)+k4)
    return y


y_0=np.array([10**12,0])
Fe = Planet_Model(8300,0.00345,0.528)
dr= 6371
r = 6371
rfinal=10000
rho_plot =[]
r_plot =[]
earth_r=6371000
earth_m = 5.972*10**24

if __name__ == "__main__":

    while True:
        
        p=y_0[0]
        m=y_0[1]
        y=RK4(Fe.derivatives,y_0,r,dr)
        r=r+dr
        y_0=y
        
       
        rho_plot.append(Fe.density(p))
        r_plot.append(r)
        
       
        if (p+10*Fe.dPdr(p,r,m)*dr) <=0:
            dr=1000
    
        if (p+2*Fe.dPdr(p,r,m)*dr < 0):
            print("radius ",r/earth_r)
            print("mass ", m/earth_m)
            break
        
        plt.plot(r_plot, rho_plot)
        plt.xlabel("Radius")
        plt.ylabel("Density")
        plt.title("Fe Density vs Radius")
        
    

    
    
