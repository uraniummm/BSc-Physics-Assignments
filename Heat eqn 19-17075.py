#       Name : Nikita Rana
#     Roll No: 19/17076



#--------------Heat equation------------
#------------U_t = D*U_xx ------------
#------------U(x,0) =2*np.sin((x*np.pi)/2)-np.sin(np.pi*x)+4*np.sin(2*np.pi*x)------------
#u(0,t)=0  u(l,t)=0   l=2
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


#------------selecting grid points------------
M = 80
N = 90

#------------interval of x------------
x0 = 0
xL = 2
#------------step size in x------------
dx = (xL - x0)/(M-1)

#------------interval of time------------
t0 = 0
tf = 0.2
#------------step size of time------------
dt = (tf - t0)/(N-1)

#------------constants used in equation------------
D = 1

r = (dt*D)/(dx**2)


x = np.linspace(x0, xL, M)
t = np.linspace(t0, tf, N)

#------------intializing matrix.......

U = np.zeros((M,N))

#------------initial conditions......

U[:,0] = 2*np.sin((x*np.pi)/2)-np.sin(np.pi*x)+4*np.sin(2*np.pi*x)
U[0,:]= 0
U[-1,:] = 0

#------------double loop for discrete equation........

for j in range(0, N-1):
    for i in range(1,M-1):
        U[i, j+1] = r*U[i-1, j] + (1 - 2*r)*U[i, j] + r*U[i+1, j]

#------------forming meshgrid.........

T, X = np.meshgrid(t, x)

#.......plotting.......
fig = plt.figure()
ax=fig.gca(projection = '3d')
surf = ax.plot_surface(X, T, U, cmap=cm.coolwarm,linewidth=0, antialiased = False)
ax.set_xlabel('space')
ax.set_ylabel('Time')
ax.set_zlabel('U')
ax.view_init(elev=33,azim=36)
plt.tight_layout()
plt.show()


