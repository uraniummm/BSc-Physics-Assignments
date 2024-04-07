
# Solving ode using odeint function
# y"+y'+2y=x+sinx

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dP_dx(P,x):
    return(P[1],-P[1]-2*P[0]+x+np.sin(x))

P0=[1,0]
a=0
b=10
xs=np.arange(a,b,0.01)
Ps=odeint(dP_dx,P0,xs)

ys=Ps[:,0]
print("ys=",ys)

Zs=Ps[:,1]
print("Zs",Zs)
plt.plot(xs,ys)
plt.plot(xs,Zs)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('using inbuilt')
