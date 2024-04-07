# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:19:21 2021

@author: hp
"""

# d^2 y/dx^2 = -2dy/dx -2y + cos(2x)
#
#du[1]/dx=-2*u[1]-2*u[0]+cos(2x)
#u[1],du[1]/dx
# y=u[0]  ,  dy/dx=u[1]
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def f(u,x):
    return(u[1],-2*u[1]-2*u[0]+np.cos(2*x))

#y(0)=0    y'(n)=0
u0=[0,0]

xs=np.linspace(0,10,100)

ps=odeint(f,u0,xs)
ys=ps[:,0]
zs=ps[:,1]
plt.plot(xs,ys)
plt.plot(xs,zs)
#plt.plot(xs,ps)
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.grid()
plt.show()