#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:56:52 2018

@author: sharleenprice
"""

import math
import numpy as np

def unobscuredFlux(p,abs_z):
    z= abs(abs_z)
    lambda_e=0
    unobs_flux = 0
    
    if 1+p<z:
        lambda_e = 0
    elif abs(1-p)<z and 1+p>=z:
        k_1= math.acos((1-(p**2)+(z**2))/(2*z)) 
        k_0= math.acos(((p**2)+(z**2)-1)/(2*p*z))
        lambda_e = (1/math.pi)*(((p**2)*k_0)+k_1-math.sqrt((4*(z**2)-(1+(z**2)-(p**2))**2)/4))
    elif z <=1-p:
        lambda_e=p**2
    elif z <= p-1:
        lambda_e = 1
    
    unobs_flux = 1-lambda_e
    
    return unobs_flux
        
def LoopThroughFlux(p,start,stop,interval):
    all_range = np.arange(start,stop,interval)
    for i in all_range:
        print (unobscuredFlux(p,i))
    