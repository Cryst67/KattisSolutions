from math import factorial as f
n,a=int(input()),0
for i in range(1,n+1):a+=f(n)//f(n-i)
print('JUST RUN!!'if a>1e9 else a)