#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:50:15 2017

@author: sharleenprice spp2122
"""

def piggify(word):
   vowels= "aeiou"
   char = 0
   new_word = ""
   length = len(word)
   if (word[0] in vowels):
       new_word = word + "yay"
       return new_word
   else:
       while ((word[char] not in vowels) and char!=length):
           word+= word[char]
           new_word = word[(char + 1):]
           char +=1
       return (new_word+"ay")   


vars = True
while(vars):
    userword= input("Enter the word you would like translated or enter '.' to quit ")
    if(userword == "."):
        vars = False
    else:
        print(piggify(userword))
