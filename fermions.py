
#Plotting dN/dE vs E for Relativistic/Non-relativistic Fermions

import numpy as np
from scipy.constants import h,c,m_e,k,pi,e
import matplotlib.pyplot as plt

#dN/dE for non-relativistic fermions

plt.subplot(1,2,1)
s=0.5 #Spin
u=1 #Chemical Potential
V=1 #Volume
Cn=(2*s+1)*2*pi*V*(2*m_e)**(3/2)/h**3
E=np.linspace(0,2,1000) #Energy in eV
T=[100,1000]
g=[0]*len(E)
n=[0]*len(E)
f=[0]*len(E)
for j in range(len(T)):
    b=1/(k*T[j])
    for i in range(len(E)):
        g[i]=Cn*E[i]**(1/2)
        n[i]=1/(np.exp((E[i]-u)*b*e)+1)
        f[i]=g[i]*n[i]
    plt.plot(E,f,label=str(T[j])+" K")
plt.xlabel("Energy (eV)")
plt.ylabel("dN/dE")
plt.title("Non-Relativistic Fermions (s=0.5, u=1eV)",fontweight='bold')
plt.legend()

plt.subplot(1,2,2)

#dN/dE for relativistic fermions

s=0.5 #Spin
u=1 #Chemical Potential
V=1 #Volume
Cr=2*s*4*pi*V/(h*c)**3
E=np.linspace(0,2,1000) #Energy in MeV
T=[1e8,1e9]
g=[0]*len(E)
n=[0]*len(E)
f=[0]*len(E)
for j in range(len(T)):
    b=1/(k*T[j])
    for i in range(len(E)):
        g[i]=Cr*E[i]**2
        n[i]=1/(np.exp((E[i]-u)*b*e*10**6)+1)
        f[i]=g[i]*n[i]
    plt.plot(E,f,label=str(format(T[j],"0.1"))+" K")
plt.xlabel("Energy (MeV)")
plt.ylabel("dN/dE")
plt.title("Relativistic Fermions (s=0.5, u=1MeV)",fontweight='bold')
plt.legend()    
plt.show()
