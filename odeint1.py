# y"=(-g/l)sin(y)
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dP_dx(P,x):
    return(P[1],(-g/l)*np.sin(P[0]))

P0=[1,0]
g=9.8
l=10
a=0
b=100
xs=np.arange(a,b,0.01)

ps=odeint(dP_dx,P0,xs)
ys=ps[:,1]
cs=ps[:,0]
#plt.plot(xs,ys)
#plt.plot(xs,cs)
plt.plot(ys,cs)