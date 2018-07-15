#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:24:04 2017

@author: sharleenprice
"""
import random
import math


rand_num=random.random()*10
ceil_rand = math.ceil(rand_num)
user_guess = 0
counter = 0

while counter < 5:
    user_guess = int(input("Enter your guess number: "))
    if abs(ceil_rand-user_guess)>5:
        print("Not even close")
        counter +=1
        continue
    elif abs(ceil_rand-user_guess)>=3 and abs(ceil_rand-5)<=5:
        print("Close")
        counter +=1
        continue
    elif abs(ceil_rand-user_guess)<3 and abs(ceil_rand-user_guess) != 0:
        print("Almost There")
        counter +=1
        continue
    else:
        print("You got it!")
        break
if(counter == 5):
    print("You have used up all 5 guesses, the correct answer was " 
      + str(ceil_rand))

