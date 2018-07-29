#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:35:39 2018

@author: sharleenprice
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np


"""Spiral"""

#spiral = fits.getdata("spiral.fits")
#plt.imshow(spiral)

        #Brightest Pixel 
#maxvalS = np.max(spiral)
#y = np.where(spiral == maxvalS)
#plt.plot(y[1],y[0],marker = "o", markersize = 3, color="red")


        #Weighted Mean

#ivals, jvals, normalizes = 0,0,0
#
#nxs, nys = np.shape(spiral)
#
#for i in range(nxs):
#    for j in range(nys):
#        ivals+=i*spiral[i,j]
#        jvals+=i*spiral[i,j]
#        normalizes+=spiral[i,j]
#ivals = int(ivals/normalizes)
#jvals = int(jvals/normalizes)
#
#plt.plot(ivals,jvals, marker = "o", markersize = 3, color="red")


""" Elliptical"""

elliptical = fits.getdata("elliptical.fits")
plt.imshow(elliptical)


        #Brightest Pixel

#maxvalE = np.max(elliptical)
#x = np.where(elliptical == maxvalE)
#plt.plot(x[0],x[1],marker = "o", markersize = 3, color="red")


        #Weighted Mean

ival, jval, normalize = 0,0,0

nx, ny = np.shape(elliptical)
center = [nx/2,ny/2]


for i in range(nx):
    for j in range(ny):
        
        ival+=i*elliptical[i,j]
        jval+=i*elliptical[i,j]
        normalize+=elliptical[i,j]
        r=np.sqrt(((i-center[0])**2)+((j-center[1])**2))


ival = int(ival/normalize)
jval = int(jval/normalize)

plt.plot(ival,jval, marker = "o", markersize = 3, color="red")



#Dont Comment
plt.colorbar()
plt.clim(vmax = 30)







