#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:20:46 2017

@author: sharleenprice
"""

f = open("hello.txt",'r')

lines = len(f.readlines())
print(lines)
