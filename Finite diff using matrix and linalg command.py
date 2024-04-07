# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:56:27 2021

@author: hp
"""

#finite  difference using matrix by ajay mishra  sir

# y"=-g
import numpy as np
import matplotlib.pyplot as plt
n=10
h=(5-0)/n

A=np.zeros((n+1,n+1))

A[0,0]=1
A[n,n]=1


for i in range(1,n):
    A[i,i+1]=1
    A[i,i]=-2
    A[i,i-1]=1

print(A)

b=np.zeros(n+1)

b[1:-1]=(-9.8)*h**2

b[-1]=50 

print(b)

y=np.linalg.solve(A,b)
x=np.linspace(0,5,n+1)
print("y:",y)   
plt.plot(x,y)
plt.show()