#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:33:42 2017

@author: sharleenprice
"""

user_input = int(input("Please enter a number "))
sum = 0
temp = 1

while temp <= user_input:
    for x in range(0,1):
        sum += temp
        temp += 1
    print(sum)    

    
    
        
    
