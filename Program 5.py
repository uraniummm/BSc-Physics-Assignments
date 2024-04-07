#--Submitted by : Nikita Rana

#Integrating 2x/(1+x^4) from limits 1 to 2 using Gauss Quadrature and compare with exact solution.
#Exact solution: tan^–1 (4) – (π/4)

import numpy as np
import math


#Defining the function f(x):[2x/(1+ x^4 ):
def f(x):
	return (2*x/(1+x**4))

#Defining limits:
a=1
b=2

#Using one point formula i.e. n=1:

#Weight Functions
w1=2
#Abscissae 
u1=0

#Converting limits from a and b to -1 and 1
t1=((b-a)*u1+b+a)/2

y=(b-a)/2*(w1*f(t1))
print("Result using n=1 point formula:",y)

#Using two point formula i.e. n=2:

#Weight Functions
w1=1
w2=1
#Abscissae
u1=-1/np.sqrt(3)
u2=1/np.sqrt(3)

t1=((b-a)*u1+b+a)/2
y1=(b-a)/2*(w1*f(t1))

t2=((b-a)*u2+b+a)/2
y2=(b-a)/2*(w2*f(t2))

print("Result using n=2 point formula:",y1+y2)

#Using three point formula i.e. n=3:

#Weight Functions
w1=5/9
w2=8/9
w3=5/9
#Abscissae
u1=-np.sqrt(3/5)
u2=0
u3=np.sqrt(3/5)

t1=((b-a)*u1+b+a)/2
y1=(b-a)/2*(w1*f(t1))

t2=((b-a)*u2+b+a)/2
y2=(b-a)/2*(w2*f(t2))

t3=((b-a)*u3+b+a)/2
y3=(b-a)/2*(w3*f(t3))

print("Result using n=3 point formula:",y1+y2+y3)


#Exact answer:
exact=math.atan(4)-np.pi/4
print("Exact Solution for comparison :",exact)

