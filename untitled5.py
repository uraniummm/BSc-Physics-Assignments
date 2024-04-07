import numpy as np
from scipy import linalg as lg
from numpy.linalg import eig
import matplotlib.pyplot as plt
"""
Solve the s-wave radial Schrodinger equation for a particle 
of mass m:
For an harmonic oscillator potential
for the ground state energy (in MeV) of particle to an accuracy
 of three significant digits. 
Also, plot the corresponding wave function.
 Choose m = 940 MeV/c2, k = 100 MeV fm-2, b = 0, 10, 30 MeV fm-3
. In these units, cħ = 197.3 MeV fm. The ground state energy is 
expected to lie between 90 and 110 MeV for all three cases
"""
m=940 #given
h=197.3 #hcross
l=10
d=0.05 #range
p=np.arange(-l+d,l,d)
k=100 #given
n=len(p)
#constant
a=(m*(d**2))/h**2
#tridiagonal
z=np.zeros([n,n])
#potential
v=np.zeros([n])
for i in range(n):
 
    x=p[i]
    v[i]=(0.5)*k*(x**2)
    for j in range(n):
 
        if(i==j):
            z[i,j]=2*(1+a*v[i])
 
        elif(i==j-1):
            z[i,j]=-1
 
        elif(i==j+1):
            z[i,j]=-1
 
        else:
            z[i,j]=0
 
print(z)

values,vectors=np.linalg.eigh(z)
#print(values) #energy eigen value
E=values
E=np.multiply(E,(1/(2*a)))
print(E)
plt.plot(p,vectors[:,0]*vectors[:,0])
plt.plot(p,vectors[:,1]*vectors[:,1])
plt.plot(p,vectors[:,2]*vectors[:,2])
plt.title("wavefunction of harmonic oscillator")
plt.show()