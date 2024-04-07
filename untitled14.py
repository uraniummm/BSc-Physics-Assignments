
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite as h

from scipy.integrate import dblquad

def j(x,y):
    return(1+ (2)*np.exp(-(x**2 + y**2)))


def integ1(x,y):
    return(x*(np.exp(-2*(x**2 + y**2)))*(x - 2*x)*(j(x, y)**(-3/2)))

def integ2(x,y):
    return(y*(np.exp(-2*(x**2 + y**2)))*(y - 2*y)*(j(x, y)**(-3/2)))

def system(variables, t):
    fx, fy, df1x, df1y  = variables
    i1,err1=dblquad(integ1,-np.inf,np.inf,-np.inf,np.inf)
    i2,err2=dblquad(integ2,-np.inf,np.inf,-np.inf,np.inf)
    df2x = -((df1x**2)/fx) + (1/fx**3) + (28/(np.pi*fy*fx**2))*(i1) 
    df2y = -((df1y**2)/fy) + (1/fy**3) + (28/(np.pi*fx*fy**2))*(i2)
    return [df1x, df1y, df2x, df2y]

# Set initial conditions
initial_conditions = [1,1,0,0]

# Define time points
t = np.linspace(0, 10, 100)

# Solve the equations
solution = odeint(system, initial_conditions, t)

# Plot the results
plt.plot(t, solution[:, 0])
plt.plot(t, solution[:, 1])
plt.plot(t, solution[:, 2])
plt.plot(t, solution[:, 3])


plt.legend()
plt.show()
