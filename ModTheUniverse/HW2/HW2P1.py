#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:17:15 2018

@author: sharleenprice
"""
import math 
import numpy as np

p=0.2
z=0.9

def delta(p,r,z):
    delta=0
    if r>= z+p or r<=z-p:
        delta = 0
    elif r+z <= p:
        delta = 1
    else:
        delta = ((math.pi)**-1)*np.arccos(((z**2)-(p**2)+r**2)/(2*r*z))
     
    return delta
    
def limbDarkening(r):
    return 1
    

def top(r):
    top_func = limbDarkening()*(1-delta(0.2,r,0.9))*2*r
    return top_func

def bottom(r):
    bottom_func = limbDarkening()*2*r
    return bottom_func

def integrator(f,a,b,N):
    delta_x = (b-a)/N
    r_sum = 0        
    for c in range(0,N):
        r = a+ c*delta_x
        r_sum += f(r)*delta_x
    
    return r_sum
    
def F(p,z):
    N=[10,10**2,10**3,10**4,10**5]
    top_f = 0
    bottom_f=0
    for i in N:
        top_f=integrator(top,0,1,i)
        bottom_f = integrator(bottom,0,1,i)
        f=top_f/bottom_f
        error=abs(0.9684170049114548 - f)/0.9684170049114548
        print(f)
        print("error is: ", error)
        print()
        


    
    
    
    
    
    
    
    