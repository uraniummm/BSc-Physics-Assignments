## Name : Nikita rana
## Roll no : 19/17076

import numpy as np
from scipy.constants import pi
from scipy.constants import h
from scipy.constants import m_e
from scipy.constants import e
from scipy import *
from scipy import integrate
from pylab import *
from matplotlib import pyplot as plt
def Numerov(f, x0, dx, dh):
    x = zeros(len(f))
    x[0] = x0
    x[1] = x0 + dh*dx
    
    h2 = dh**2
    h12 = h2/12
    
    w0 = x0*(1 - h12*f[0])
    w1 = x[1]*(1-h12*f[1])
    xi = x[1]
    fi = f[1]
    for i in range(2,len(f)):
        w2 = 2*w1-w0+h2*fi*xi
        fi = f[i]
        xi = w2/(1-h12*fi)
        x[i] = xi
        w0 = w1
        w1 = w2
        return x
        
def fschrod(En,l, R):
    return 1*(l+1)/R**2-2/R-En

Rl = linspace(1e-7,50.1000)
l= 0

En = -1
f = fschrod(En,l,Rl[::-1])
ur = Numerov(f,0.0,1e-7,Rl[1]-Rl[0])[::-1]
norm = integrate.simps(ur**2,x=Rl)
ur *= 1/sqrt(abs(norm))
plt.plot(f,ur)
plt.show()