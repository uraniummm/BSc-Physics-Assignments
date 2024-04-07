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


def j(fx,x,y):
    return(1+ (2)*np.exp(-(x**2 + y**2))/fx)


def integ(fx,x,y):
    res,err=dblquad(lambda x,y :x*(np.exp(-2*(x**2 + y**2)))*(x - 2*x)*(j(fx,x, y)**(-3/2)),
                    -np.inf,np.inf,-np.inf,np.inf)
    return res




def dp_dx(P,z):
    f1x,df1x=P
    df2x=((-1/f1x)*df1x**2)+(1/f1x**3)+ (28/(np.pi*f1x**2))*(integ(f1x,0,0)/((0.5)*2))
    return(df1x, df2x)

P0=[1,0]
a=0
b=10

z=np.linspace(0,5,100)

fx=odeint(dp_dx, P0, z)

sol=fx[:,0]

plt.plot(z,sol)
plt.show()