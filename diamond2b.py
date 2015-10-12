# -*- coding: utf-8 -*-

N = 20
K = [0]*N 
#N = input("Enter the value of N: ")

T = [0]*N

for i in range (1,N):
    T[i]= T[i-1]+1.0/i

#print(T)
    
def P(k,n):
    return (T[n-1]-T[k-1])*k/n

k=1
nk_table = [0]*(N+1)

#print(nk_table)

for n in range(1,N+1):
    while(P(k+1,n)>P(k,n)):
        k = k+1
    nk_table[n]=(k,P(k,n))
    #nk_table[n][1]=P(k,n)
nk_table.pop(0)

for index, S in enumerate(nk_table, start=1): 
    print "n=",index, " k=", S[0], " P:", S[1] 
    