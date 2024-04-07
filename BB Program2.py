
#Program:2

#Comparing plots of Planck's Law and Rayleigh Jean's Law at the same temperature w.r.t. wavelength

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c

w=np.linspace(0.005e-6,9e-6,1000)

T=2500

rj=8*pi*k*T/w**4

pl=(8*pi*h*c)/(w**5*(np.exp((h*c)/(w*k*T))-1))

plt.plot(w,rj,label="Rayleigh-Jean's Law")
plt.ylim(0,10**4.3)
plt.plot(w,pl,label="Planck's Law")
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Density (J/m^3)")
plt.title("Comparison of Planck's law and Rayleigh Jean's law wrt wavelength")
plt.legend()
plt.show()
