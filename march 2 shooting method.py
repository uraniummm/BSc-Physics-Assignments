# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:13:12 2021

@author: hp
"""
# Sidhanth Gupta
#y"+y=0
#y(0)=1 y(pi/2)=1
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def f(u,x):
    return(u[1],-u[0])
#first guess at y'(0)=0
u0=[1,0]
xs=np.linspace(0,np.pi/2,100)

ps=odeint(f,u0,xs)
ys=ps[:,0]
y=ps[:,1]
print(ys[-1])
plt.plot(xs,ys,label="first guess")


#second guess at y'(0)=-2
u1=[1,-2]
xs=np.linspace(0,np.pi/2,100)

ps1=odeint(f,u1,xs)
ys1=ps1[:,0]
y1=ps1[:,1]
print(ys1[-1])
plt.plot(xs,ys1,label="second guess")

g3=y1[0]+(1-ys1[-1])*(y[0]-y1[0])/(ys[-1]-ys1[-1])

print("g3:",g3)

u2=[1,g3]
ps2=odeint(f,u2,xs)
y2=ps2[:,0]
print("y2[-1]:",y2[-1])
t=np.linspace(0,np.pi/2,100)
plt.plot(t,y2,label="final guess")
plt.plot(np.pi/2,1,"ro")
plt.show()
