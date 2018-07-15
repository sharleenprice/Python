#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:07:44 2017

@author: spp2122 Sharleen Price
"""
import math

userSeconds = int(input("Please enter an amount of seconds "))

#calculate hours in input time
hours = (userSeconds/86400)*24
floor_hours = str(math.floor(hours))
if int(floor_hours) == 1:
    total_hours = (floor_hours + " hour")
else:
    total_hours = (floor_hours + " hours")
    
#calculate minutes in input time
minutes=(hours%1)*60
floor_minutes = str(math.floor(minutes))
if (int(floor_minutes) == 1):
    total_minutes = (floor_minutes + " minute")
else:
    total_minutes = (floor_minutes + " minutes")

#calculate seconds in input time
seconds= (minutes%1)*60
floor_seconds = str(math.floor(seconds))
ceiling_seconds = str(math.ceil(seconds)) 
   
if (int(floor_seconds)==1 or int(ceiling_seconds)==1):
    total_seconds = ("1 second")    
elif (seconds%1<.5):
    total_seconds = (floor_seconds + " seconds") 
elif (seconds%1>=.5):
    total_seconds = (ceiling_seconds + " seconds")
       
print(total_hours + ", "+ total_minutes + ", and " +total_seconds)
