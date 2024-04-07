# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:30:29 2021

@author: hp
"""

import matplotlib.pyplot as plt
import numpy as np
N0=input("Enter Initial no. of items:")
N0=int(N0)
t0=0

th=input("Enter Half Life:")
th=int(th)
k=(np.log(2))/th

print("Decay constant:",k)

tfinal=input("Enter t final:")
tfinal=int(tfinal)

dt=0.1

t=np.arange(t0,tfinal,dt)

Nexact=N0*np.exp(-k*t)

print("No. of atoms remaining:",Nexact[-1])

plt.plot(t,Nexact)


length_t=len(t)
Nf=np.zeros(length_t)
Nf[0]=N0

for i in range(length_t-1):
    Nf[i+1]=Nf[i]-k*dt*Nf[i]

plt.plot(t,Nf)    
    
plt.show()
