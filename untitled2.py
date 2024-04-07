# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:31:27 2021

@author: hp
"""
# y'+y=0
import numpy as np
import matplotlib.pyplot as plt
n=100
h=((np.pi/2)-0)/n

A=np.zeros((n+1,n+1))

A[0,0]=1
A[n,n]=1


for i in range(1,n):
    A[i,i+1]=1
    A[i,i]=-2+(h**h)
    A[i,i-1]=1

print(A)

b=np.zeros(n+1)

b[0]=1
b[-1]=1 

print(b)

y=np.linalg.solve(A,b)
t=np.linspace(0,np.pi/2,n+1)
plt.plot(t,y)
plt.plot()
print(y)   