#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:36:37 2017

@author: sharleenprice
"""

def mytri(myrange):
    rows = list()
    lr = None # Last row

    for i in range(myrange+1):
        try:
            lr = [1] + [lr[i] + lr[i+1] for i in range(len(lr) - 1)] + [1]
        except TypeError:
            lr = [1]
        #rows.append(str(lr))
        rows.append(' '.join(str(v) for v in lr))
    return rows

rows = mytri(6)
l = len(rows[-1])
print ('\n'.join(v.center(l) for v in rows))