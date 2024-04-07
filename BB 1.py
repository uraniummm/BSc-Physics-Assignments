
#Program:1

#Comparing plots of Planck's Law and Rayleigh Jean's Law at the same temperature w.r.t. frequency.

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c

f=np.linspace(1e-5,8e14,1000)

T=2500

rj=8*pi*k*T*f**2/c**3

pl=(8*pi*h*f**3)/(c**3*(np.exp((h*f)/(k*T))-1))

plt.plot(f,rj,label="Rayleigh-Jean's Law")
plt.ylim(0,1.5e-16)
plt.plot(f,pl,label="Planck's Law")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy Density (J/m^3)")
plt.title("Comparison of Planck's law and Rayleigh-Jean's law w.r.t. frequency")
plt.legend()
plt.show()
