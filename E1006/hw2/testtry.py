#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 00:10:25 2017

@author: sharleenprice
"""

def triangle(rows):

    for rownum in range (rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration )   / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)
        somelist = [5]
    print(somelist)