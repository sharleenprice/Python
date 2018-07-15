#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:18:33 2017

@author: sharleenprice
"""

counter = 0
while(counter<100):
    print(counter)
    if counter % 2 == 0:
        print(counter)
        counter += 1
    else: 
        counter = counter * 2
        print(counter)

print(counter)