#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:49:31 2017

@author: sharleenprice
"""

counter = 0
while True:
    print(counter)
    if counter >=100:
        print(counter)
        break
    if counter % 2 == 0:
        print(counter)
        counter+=1
        continue
    counter = counter * 2
    print(counter)

print(counter)
    
    
