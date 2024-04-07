# made by Nikita Rana

#Question 3 :Verify Dirac Delta Function

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import legendre
from scipy.integrate import quad
from scipy.integrate import simps

print("Question 3: Dirac Delta Function\n")

#Defining limits:

a=-np.inf
b=np.inf

#To use Gauss Hermite method, we will rearrange the integral.
# x=(y*sigma*np.sqrt(2))+2
# therefore dx=dy*sigma*np.sqrt(2)

def f(y):
	return (y*sig*np.sqrt(2)+5)/np.sqrt(np.pi)


#Using three point formula:

#Weight
w1=0.295408
w2=1.181635
w3=0.295408
#Abscissae
x1=-1.224744
x2=0
x3=1.224744

#For sigma =1
print("For sigma = 1 ")
sig=1
y1=w1*f(x1)
y2=w2*f(x2)
y3=w3*f(x3)

print("Result using Gauss Hermite 3-point rule:",(y1+y2+y3))

#-------------Simpsons Method-----------
x=np.linspace(-100,100,10000) #Since simps can't accept infinity as limits therefore I have used 100.
y1=simps(np.exp(-(x-2)**2/(2*sig**2))*(x+3),x)
y=(1/np.sqrt(2*np.pi*sig**2))*y1
print("Result using simpson:",y,"\n")


#For sigma=0.1
print("For sigma=0.1")
sig=0.1
y1=w1*f(x1)
y2=w2*f(x2)
y3=w3*f(x3)

print("Result using Gauss Hermite 3-point rule:",(y1+y2+y3))


y1=simps(np.exp(-(x-2)**2/(2*sig**2))*(x+3),x)
y=(1/np.sqrt(2*np.pi*sig**2))*y1
print("Result using simps:",y,"\n")


#For sigma=0.01
print("For sigma=0.01")
sig=0.01
y1=w1*f(x1)
y2=w2*f(x2)
y3=w3*f(x3)

print("Result using Gauss Hermite 3-point rule:",(y1+y2+y3))


y1=simps(np.exp(-(x-2)**2/(2*sig**2))*(x+3),x)
y=(1/np.sqrt(2*np.pi*sig**2))*y1
print("Result using simps:",y)