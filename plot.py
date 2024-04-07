from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite as h

from scipy.integrate import dblquad

#P=fx

# m=0 
# n=0 
# hm=h(m)
# hn=h(n)
# hm1=h(m+1)
# print(hm)


def j(x,y):
    return(1+ (2)*np.exp(-(x**2 + y**2)))


def integ(x,y):
    return(x*(np.exp(-2*(x**2 + y**2)))*(x - 2*x)*(j(x, y)**(-3/2)))




def dp_dx(P,z):
    i,err=dblquad(integ,-np.inf,np.inf,-np.inf,np.inf)
    return(P[1],((-1/P[0])*P[1]**2)+(1/P[0]**3)+ (28/(np.pi*P[0]**2))*(i/((0.5)*2)) )

P0=[1,0]
a=0
b=10

z=np.linspace(0,5,100)

fx=odeint(dp_dx, P0, z)

sol=fx[:,0]

plt.plot(z,sol)
plt.show()