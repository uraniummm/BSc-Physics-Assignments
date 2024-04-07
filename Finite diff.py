# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:02:16 2021

@author: hp
"""

# df= (f(x+h)-f(x-h))/(2*h)

# f(x)= 0.1*x**5-0.2*x**3+0.1*x-0.2

import numpy as np
import matplotlib.pyplot as plt

f=lambda x:0.1*x**5-0.2*x**3+0.1*x-0.2

h=0.1
x=np.linspace(-1,1)

#central differentiation

dff1=(f(x+h)-f(x-h))/(2*h)

#plot
plt.plot(x,dff1)

#forward difference

dff2= (f(x+h)-f(x))/h
plt.plot(x,dff2)

#backward difference
dff3=(f(x)-f(x-h))/h
plt.plot(x,dff3)


#theoretical

g=lambda x:0.5*x**4-0.6*x**2+0.1
plt.plot(x,g(x))
plt.legend(["dff1","dff2","dff3","dff4"])

plt.show()
