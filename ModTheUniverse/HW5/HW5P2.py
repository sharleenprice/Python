#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:11:42 2018

@author: sharleenprice
"""
from astropy.io import fits
import math
import matplotlib.pyplot as plt
import numpy as np


galaxy = input("Enter Data File Name: ")
galaxy_data = fits.getdata(galaxy)


nx, ny = np.shape(galaxy_data)
center = [nx/2,ny/2]

total = 0
count = 0
radius = []
average = []

s_0=galaxy_data[int(nx/2),int(ny/2)]
rand_bright=s_0*(1/math.e)
r_0=23
for inc in np.arange(0,int(nx/2),5):

    for i in range((nx)):
        for j in range((ny)):
            r=np.sqrt(((i-center[0])**2)+((j-center[1])**2))  
            if (r >= inc and r<= 2+inc ):
                total += galaxy_data[i,j]
                count+=1
    radius.append(((inc)+(2+inc))/2)        
    average.append(total/count)
   
flux = [] 
for i in radius:
    flux.append(s_0*math.exp(-i/r_0))

plt.plot(radius,flux, color="red", label = "Exponential")
plt.plot(radius,average, label = "Average")

plt.title("Average Brightness vs Radius")
plt.ylabel("Average Brightness")
plt.xlabel("Radius")
plt.legend()
       
            
            

