#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:26:15 2018

@author: sharleenprice
"""

import math 
import numpy as np

#p=0.2
#z=0.9

def delta(p,z,r):
    delta=0
    if r>= z+p or r<=z-p:
        delta = 0
    elif r+z <= p:
        delta = 1
    else:
        delta = ((math.pi)**-1)*np.arccos(((z**2)-(p**2)+r**2)/(2*r*z))
     
    return delta
    
def limbDarkening(r):
     m= (1-r**2)**(1/2)
     return (1-(1-m**(3/2)))
    

def top(p,z,r):
    top_func = limbDarkening(r)*(1-delta(p,z,r))*2*r
    return top_func

def bottom(p,z,r):
    bottom_func = limbDarkening(r)*2*r
    return bottom_func

    
def F(p,z,N):
    #N=[10,10**2,10**3,10**4,10**5]
    top_f = 0
    bottom_f=0
    #N_np = np.array(N)
    
    i=N
    top_f=simpson(top,0,1,i,p,z)
    bottom_f = simpson(bottom,0,1,i,p,z)
    f=top_f/bottom_f
    #    error=abs(0.9684170049114548 - f)/0.9684170049114548
    
    return (f)
        #print(f)
        #print("error is: ", error)
        #print()
        
    
def simpson(f,a,b,N,p,z):
    delta_x = (b-a)/N
    n=N-2
    odds=0
    evens= 0
    #sum_odds = 0
    for i in range(0,int(n)):
        #r1=(a+i*delta_x+a+(i+1)*delta_x)/2
        r1=(a+i*delta_x+(delta_x/2))
        odds+=(2/3)*f(p,z,r1)
        #odds=odds*(2/3)
    for j in range(1,int(n-1)):
        r2=a+j*delta_x
        evens+=(1/3)*f(p,z,r2)
        #evens = evens*(1/3)
        
    sum_all = (f(p,z,a)/6 +f(p,z,b)/6 + evens + odds)*delta_x
    
    return sum_all   
    
def LoopFlux(p,start,stop,interval,N):
    fe=[]
    all_range = np.arange(start,stop,interval) #values of z
    for i in all_range:
        fe.append(F(p,abs(i),N)) #values of f(p,z)
    fe_np=np.array(fe)
    return(fe_np,all_range)
        
    
    
    
    
    
    