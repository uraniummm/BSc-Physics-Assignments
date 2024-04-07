# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:57:39 2021

@author: hp
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
#dy/dx=3y-x
#y(0)=0
#x=0to3

def f(y,x):
    return(3*y-x)

xs=np.linspace(0,3,100)
p0=0
ps=odeint(f,p0,xs)

print("y:",ps)
plt.plot(ps,xs)
plt.xlabel("x axis")
plt.ylabel("Y axis")
plt.show()