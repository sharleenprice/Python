#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:15:09 2018

@author: sharleenprice
"""

import random
#import math

p=0.2
z=0.9
N=[10,10**2,10**3,10**4,10**5]

for a in N:
    N1=0
    N2=0
    for i in range(0,a):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if ((x**2)+(y**2))<1:
            N1+=1
        if (((x-z)**2)+(y**2)<(p**2)):
            N2+=1
    f=(N1-N2)/N1
    error=abs(0.9684170049114548 - f)/0.9684170049114548
    print("F(p,z) is: ",f)
    print("error is: ", error)
    print()



