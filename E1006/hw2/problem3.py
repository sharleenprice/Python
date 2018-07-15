#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:37:14 2017

@author: sharleenprice spp21222
"""
a_list= []
x = 1
height = int(input("what height woud you like your pascals triangle to be? "))
for row in range(height):
    var = 1
    if (row <6):
        a_list = [" "*((height+1)-x), var, " "]
        x+=1
        for pos in range(row):
            var=var*(row-pos)/(pos+1)
            a_list.append(int(var))
            a_list.append(" ")
    elif(row>=6):
        a_list = [" "*((height)-x), var, " "]
        x+=1
        for pos in range(row):
            var=var*(row-pos)/(pos+1)
            a_list.append(int(var))
            a_list.append(" ")
    
    formmated_a_list =("".join(str(x) for x in a_list))
    print(formmated_a_list)
