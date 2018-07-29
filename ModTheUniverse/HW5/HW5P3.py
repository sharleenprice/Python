#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 21:36:11 2018

@author: sharleenprice
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
#import scipy.stats as stats
galaxy = input("Enter Data File Name: ")
galaxy_data = fits.getdata(galaxy)

nx = 30
ny = 30

flux = []

for i in range(nx):
        for j in range(ny):
            flux.append(galaxy_data[i,j])


plt.hist(flux)

"""Uncomment for Gaussian"""
#s = np.random.normal(0.3, 0.03, 1000)
#plt.hist(s)
"""Uncomment for Poisson"""
p = np.random.poisson(0.3, 900)
plt.hist(p)

plt.title("Distribution of Brightness Values")
plt.ylabel("Count")
plt.xlabel("Brightness")
