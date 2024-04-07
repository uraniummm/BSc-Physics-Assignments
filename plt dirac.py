# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:55:26 2021

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

def gau(x,mu,sig):
    return np.exp(-((x-mu)**2.0)/(2.0*sig**2.0))/(np.sqrt(2.0*np.pi))/sig

mu1= 0;sig1 = 0.05555
mu2 = 0 ; sig2 = 0.9999999

x=np.linspace(-10,10, 500)

plt.figure()
plt.plot(x,gau(x,mu1,sig1))
plt.plot(x,gau(x,mu2,sig2))
plt.xlabel("x")
plt.ylabel(r"$\mathcal{N}(\mu,sigma)$")
plt.show()