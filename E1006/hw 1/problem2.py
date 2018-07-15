#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:03:36 2017

@author: sharleenprice
"""
import math

current_pop = 307357870

input_years = int(input("Please enter an amount of years "))

#convert years to seconds
seconds = input_years*31536000

#used floor because you can't have half a death
births = math.floor(seconds/7)
deaths = math.floor(seconds/13)
immigrants = math.floor(seconds/35)

#add incoming subtract deaths to current population to get 
#new total
total_people = current_pop + births + immigrants - deaths

print("The current population is " + str(current_pop) 
+ " in " + str(input_years)+ " years the population will be " 
+ str(total_people))
