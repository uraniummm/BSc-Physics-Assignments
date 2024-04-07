
#Plotting of Speed distribution at different temperatures
import numpy as np
from scipy.constants import pi,k,u
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import *
import scipy as sp
from scipy.misc import derivative

m=2*u #mass of hydrogen gas

#Disrtibution Function
def f(v,T):
    r=m/(2*k*T)
    a=4*pi*(v**2)
    b=(r/pi)**(3/2)
    c=np.exp(-r*(v**2))
    return a*b*c

v=np.linspace(0,8000,100)

T=[500,600,700,800,900,1000]  #Different temperatures
for i in range(len(T)):
    plt.plot(v,f(v,T[i]),label=str(T[i])+"K")
plt.xlabel("Speed (v)")
plt.ylabel("Probability Distribution [f(v)]")
plt.title("Maxwell Speed Distribution",fontweight="heavy")
plt.legend()
plt.show()
