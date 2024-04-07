#Program:5

#Evaluation of Stefan’s Constant using a numerical method of your choice and comparing the result of integration obtained by using an inbuilt function in python.

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c,sigma
from scipy.integrate import quad
from scipy.integrate import simps

T=1500
def pl(w):
    pl=(8*pi*h*c)/(w**5*(np.exp((h*c)/(w*k*T))-1))
    return pl

res,err=quad(pl,0,40e-6) #for giving different value when we put upper limit as infinity

sig=res*c/(4*T**4)
print("Value of Stefan's Constant in Python database: ",np.round(sigma,12))
print("Calculated value using inbuilt integration 'quad': ",np.round(sig,12))

#Calculation using trapezium method

def f(x):
    return (8*pi*h*c)/(x**5*(np.exp((h*c)/(x*k*T))-1))
def trap(f,a,b,n):
    I1=0
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    for k in range(1,n):
        I1+=2*f(x[k])
    I2=f(x[0])+f(x[n])
    I=h*(I1+I2)/2
    return I
i=trap(f,1e-8,40e-6,500) #setting the lower limit using trial and error.
stef=i*c/(4*T**4)
print("Calculated value using Trapezium method: ",np.round(stef,12))


