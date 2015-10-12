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
'''
T = [0]*(N+1)
T[N]=1.0/N
for i in range(N-1,0,-1):
    T[i] = T[i+1]+(1.0/i)   
print(T)
'''
T = [0]*N

for i in range (1,N):
    T[i]= T[i-1]+1.0/i

#print(T)
    
def P(k,n):
    return (T[n-1]-T[k-1])*k/n
    
    
'''
def P(k,n):
    t = 0
    for i in range(k,n):
        t+=(1.0/i) 
    return (t*k)/n
'''
   
k=1
nk_table = [0]*(N+1)
#print(nk_table)

for n in range(1,N+1):
    while(P(k+1,n)>P(k,n)):
        k = k+1
    nk_table[n]=k
    #nk_table[n][1]=P(k,n)
    
print(nk_table)
