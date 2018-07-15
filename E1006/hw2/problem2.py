#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:38:31 2017

@author: sharleenprice spp2122

worst case find() makes (len(s)+2)*(len(substring+)+1) comparisons
find_multi() makes about the same amount of comparisons

"""

def find(s,substring):
    word = ""
    for c in range(0,len(s)):
        if(s[c]==substring[0]):
            
            if(len(s)-c>=len(substring)):
                for x in range(0,len(substring)):
                    word += s[c+x]
                    
                if (word == substring):
                    return(c)
                    break
                else:
                    word = ""
        else:
            continue
    return -1
            


def find_multi(s, substring):
    
    index_list = []
    for c in range(0,len(s)):
        if(s[c]==substring[0]):
            word = ""
            if(len(s)-c>=len(substring)):
                for x in range(0,len(substring)):
                    word += s[c+x]
                if (word == substring):
                    index_list.append(c)
                    continue
                else:
                    word = ""
           
    return index_list









