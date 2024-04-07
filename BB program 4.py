
#Program:4

#Comparison of plots of Planck’s Law at different temperatures w.r.t. frequency
#Comparison of plots of Rayleigh Jean’s Law at different temperatures w.r.t. frequency

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c

plt.figure(1)
f=np.linspace(1e-5,2e14,1000)
T=[1000,2000,3000]
for i in range(3):
    rj=8*pi*k*T[i]*f**2/c**3
    plt.plot(f,rj,label="T="+str(T[i])+"K")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy Density (J/m^3)")
plt.ylim(0,1.5e-16)
plt.title("Plots of Rayleigh Jean's law at different temperatures wrt frequency")
plt.legend()

plt.figure(2)
f=np.linspace(1e-5,8e14,1000)
T=[2500,3000,3500]
for i in range(3):
    pl=(8*pi*h*f**3)/(c**3*(np.exp((h*f)/(k*T[i]))-1))
    plt.plot(f,pl,label="T="+str(T[i])+"K")
plt.xlabel("Frequency")
plt.ylabel("Energy Density")
plt.legend()
plt.title("Plots of Planck's law at different temperatures wrt frequency")
plt.show()
