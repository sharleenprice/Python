#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:27:16 2017

@author: sharleenprice
"""

fruits_to_color= {"banana":"yellow", "cherry":"red", "blueberries":"blue", "apple":"red", "lemon":"yellow"}
color_to_fruit ={}
for fruit, color in fruits_to_color.items():
    fruit_list=[]
    if color not in color_to_fruit:
        color_to_fruit[color] = []
    color_to_fruit[color].append(fruit)
    fruit_list.append(fruit)
print(color_to_fruit, fruit_list)
