#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:38:12 2017

@author: sharleenprice
"""

f= open("students.txt" , "r")
years=[]
for lines in f:
    a=f.read()
    a.strip()
    a.split(",")
    years.append([a[1],a[0]])
years.sort()
print (years)