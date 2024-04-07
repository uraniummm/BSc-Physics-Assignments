# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:00:32 2021

@author: hp
"""

import numpy as np 
from scipy.signal import square

import matplotlib.pyplot as  plt

from scipy.integrate import simps 
from scipy.integrate import quad

L=4 #Periodicity of the periodic freq- no ofe n Sint
freq=4 #no of waves in time period L
dutycycle=0.5

samples=1000 
terms=100

#generation of square wave 
x=np.linspace(0,L,samples)
y=square(2.0*np.pi*x*freq/L,duty=dutycycle)

#Calculation of Fourier Coefficients
a0=2/L*simps(y,x)
an=lambda n:2.0/L*simps(y*np.cos(2.*np.pi*x/L),x)
bn=lambda n:2.0/L*simps(y*np.sin(2.*np.pi*n*x/L),x)

#Sum of the series
s=a0/2+sum([an(k)*np.cos(2*np.pi*k*x/L)+bn(k)*np.sin(2*np.pi*k*x/L) for k in range(1,terms+1)])

#plotting
plt.plot(x,s,label="Fourier Series")
plt.plot(x,y,label="Original Square Wave")
plt.xlabel("$x$")
plt.ylabel("y=f(x)")
plt.legend(loc='best',prop={'size':10})
plt.title("Square wave signal analysis by fourier series")
plt.savefig("fs_square.png")
plt.show()
