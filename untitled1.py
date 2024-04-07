''' Nikita Rana , 19/17076

A particle of mass m is projected with initial velocity u at an angle
theta with horizontal. Use Lagrangian equation to describe the motion 
 of the projectile.'''
 
import numpy as np
from numpy.ma.core import arctan
from numpy.testing._private.utils import _Dummy
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# INBUILT INT(ODE INT)


Ux=2
Uy=2

g=9.81


def Funx(x,t):
    x1,Ux=y
    dxdt=[Ux,0]
    return(dxdt)

def Funy(y,t,g,_Dummy):
    y1,Uy=y
    dydt=[Uy,-g]
    return dydt


t=np.arange(0,10,0.01)


initial=[0,Ux]
y=[0,Uy]

G=odeint(Funx,initial,t)
H=odeint(Funy,y,t,args=(g,_Dummy))


k=0
for i in H[:,0]:
    k+=1
    if i<0:
        H=H[:k,0]
        G=G[:k,0]
        break
plt.grid(True)
plt.title('Trajectory for the projectile motion ',size=20)
plt.xlabel("Range")
plt.ylabel("Height")
plt.plot(G,H)
plt.show()

print('Theta(in degree) =',180*arctan(Uy/Ux)/np.pi)
print("Maximum height in meters",H.max())
print("Maximum Range in meters",G.max())
