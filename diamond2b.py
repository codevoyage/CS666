# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:41:51 2015

@author: s7mahaja
"""
'''
first write the algorithm, the complexity analysis is later
'''

N = 20
K = [0]*N 
#N = input("Enter the value of N: ")
'''
I=0
for i in range(1,N):
    I+=1.0/i

for k in range(1,N):
    I[k] = sum([1/x])
'''


def P(k,n):
    t = 0
    for i in range(k,n):
        t+=(1.0/i) 
    return (t*k)/n

   
k=1
nk_table = [0]*(N+1)


for n in range(1,N+1):
    while(P(k+1,n)>P(k,n)):
        k = k+1
    nk_table[n]=k

print(nk_table)
