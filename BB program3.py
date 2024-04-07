
#Program:3

#Comparison of plots of Planck’s Law at different temperatures w.r.t. wavelength
#Comparison of plots of Rayleigh Jean’s Law at different temperatures w.r.t. wavelength

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c


plt.figure(1)
w=np.linspace(0.005e-6,9e-6,1000)
T=[1000,2000,3000]
for i in range(3):
    rj=8*pi*k*T[i]/w**4
    plt.plot(w,rj,label="T="+str(T[i])+"K")
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Density (J/m^3)")
plt.ylim(0,10**4.2)
plt.title("Plots of Rayleigh-Jean's law at different temperatures wrt wavelength")
plt.legend()

plt.figure(2)
w=np.linspace(0.005e-6,6e-6,1000)
T=[2500,3000,3500]
for i in range(3):
    pl=(8*pi*h*c)/(w**5*(np.exp((h*c)/(w*k*T[i]))-1))
    plt.plot(w,pl,label="T="+str(T[i])+"K")
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Density (J/m^3)")
plt.legend()
plt.title("Plots of Planck's law at different temperatures wrt wavelength")
plt.show()
