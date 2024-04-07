#   Name : Sidhanth Gupta
# Roll no: 19/17075

#Question 2: Integrate I=1/(x**2+2) from 0 to infinity using Gauss Laguerre method.

#---------Importing libraries---------
import numpy as np
import math
from scipy.integrate import quad
#-----Defining limits-------
a=0
b=np.inf

# As to use the Gauss Laguerre method, we need to multiply and divide the integrand with exp(x).

def f(x):
	return (np.exp(x)/(x**2+2))

#---------Using the three point formula-----------

#Weight 
w1=0.711093
w2=0.278517
w3=0.010389

#Abscissae
x1=0.415774
x2=2.294280
x3=6.289945

I=w1*f(x1)+w2*f(x2)+w3*f(x3)

print("Result using Gauss Laguerre three point rule:",I)


#Defining function for verification
def g(x):
	return (1/(x**2+2))

result,err=quad(g,a,b)

print("Result using inbuilt quad function:",result)
