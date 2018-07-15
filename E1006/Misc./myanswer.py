#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:52:06 2017

@author: sharleenprice
"""

counter = 0
while counter<100:
     print(counter)
     while counter%2 == 0:
         print(counter)
         counter+=1

     counter = counter *2 
     print(counter)
     
     
     
print(counter)