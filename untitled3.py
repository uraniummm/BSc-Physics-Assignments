# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:38:20 2021

@author: hp
"""

# f(x)= (0.3*x**6)-(0.5*x**5)+(0.1*x**3)-(0.2*x)+5

import numpy as np
import matplotlib.pyplot as plt

f=lambda x:(0.3*x**6)-(0.5*x**5)+(0.1*x**3)-(0.2*x)+5

h=0.1


x=0.1


df1=(f(x+h)-f(x))/(h)
print("using forward difference method df1=",df1)

df2=(f(x)-f(x-h))/(h)
print("using backward difference method df2=",df2)

df3=(f(x+h)-f(x-h))/(2*h)
print("using central difference method df3=",df3)

dff=(f(x+h)-2*f(x)+f(x-h))/(h*h)
print("second order derivative dff1=",dff)