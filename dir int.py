#(x+3)*np.exp(-((x-mu)**2.0)/(2.0*sig**2.0))/np.sqrt(2.0*np.pi)/sig
# function with x+3 that approaches to 5

import numpy as np
import scipy.integrate as sci

def gau(x,mu,sig):
    return (x+3)*np.exp(-((x-mu)**2.0)/(2.0*sig**2.0))/np.sqrt(2.0*np.pi)/sig

low = -np.inf ;up =np.inf;

mu1 = 2.0; sig1 = 0.88;

I_numerical, error = sci.quad(gau ,low , up, args=(mu1,sig1))

print(I_numerical)