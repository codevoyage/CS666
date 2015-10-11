# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:48:12 2015

@author: s7mahaja
"""
#import numpy as np

n = 9
success = [0]*(n+1)

#print success

def find_success(k):
    if k>1:
        find_success(k-1)
        success[k] =((success[k-1] - 1.0/n)/(k-1))*k
    elif k==1:
        harmonic = [1.0/x for x in range(1,n)]
        success[k] = sum(harmonic)/n
        

find_success(n)
print "Max value of success ", max(success), "k: ", success.index(max(success))


        