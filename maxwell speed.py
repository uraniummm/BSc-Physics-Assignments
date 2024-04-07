
#Calculation of different speeds 

import numpy as np
from scipy.constants import pi,k,u
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import *
import scipy as sp
from scipy.misc import derivative

m=2*u #mass of hydrogen gas

#Defining iteration for Trapezoidal method
def trap(f,a,b,n):
    I1=0
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    for k in range(1,n):
        I1+=2*f(x[k])
    I2=f(x[0])+f(x[n])
    I=h*(I1+I2)/2
    return I

T=900 #temperature

#Defining the function needed to be plotted
v=np.linspace(0,6000,100)
def f(v,T):
    r=m/(2*k*T)
    a=4*pi*(v**2)
    b=(r/pi)**(3/2)
    c=np.exp(-r*(v**2))
    return a*b*c

#Most Probable Speed
v=symbols('v',real=True)
r=m/(2*k*T)
a=4*pi*v**2
b=(r/pi)**(3/2)
c=exp(-r*v**2)
fn=a*b*c

dfdv=diff(fn,v)
cp= solve(dfdv,v)
print("Most probable speed of Hydrogen gas is:",round(cp[2],3)) #we are getting three critical points but first is negative second is zero and third is the required one

v=cp[2]
r=m/(2*k*T)
a=4*pi*v**2
b=(r/pi)**(3/2)
c=exp(-r*v**2)
fn=a*b*c
plt.scatter(v,fn,color="b",label="Most Probable Speed")

#Average Speed
T=900
def avg(v):
    r=m/(2*k*T)
    a=4*pi*v**2
    b=(r/pi)**(3/2)
    c=np.exp(-r*v**2)
    return v*a*b*c
res,err=quad(avg,0,6000)
print("Average speed of Hydrogen gas (using inbuilt function) is:",np.round(res,3))

v=np.linspace(0,6000,100)
i=trap(avg,0,6000,100)
print("Average speed of Hydrogen gas (using Trapezoidal Method) is:",round(i,3))

v=res
plt.scatter(v,f(v,T),color="r",label="Average Speed")

#RMS Speed
T=900
def rms(v):
    r=m/(2*k*T)
    a=4*pi*v**2
    b=(r/pi)**(3/2)
    c=np.exp(-r*v**2)
    return v**2*a*b*c
res,err=quad(rms,0,6000)
print("RMS speed of Hydrogen gas (using inbuilt function) is:",np.round((res)**(1/2),3))

v=np.linspace(0,6000,100)
i=trap(rms,0,6000,100)
i=i**(1/2)
print("RMS speed of Hydrogen gas (using Trapezoidal Method) is:",round(i,3))

v=res**(1/2)
plt.scatter(v,f(v,T),color="m",label="RMS Speed")

#Plotting function
v=np.linspace(0,6000,100)
plt.plot(v,f(v,T),label=str(T)+"K",color='orange')

plt.xlabel("Speed")
plt.ylabel("Particle Distribution")
plt.legend()
plt.title("Maxwell Speed Distribution",fontweight="bold")
plt.show()


