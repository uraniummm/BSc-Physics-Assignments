
# Program for plotting Specific Heat of Solids

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import R,h,pi,k,c
from scipy.integrate import quad
import warnings
warnings.filterwarnings("ignore") #This is just for ignoring the warnings

# Taking Diamond as our solid

plt.subplot(2,2,1)

#-----Dulong-Petit's Model-------

T=np.linspace(0,5000,1000)
def Cv(T):
    Cv=3*R*T**0
    return Cv
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat (J/(mol-K))")
plt.plot(T,Cv(T),label="Dulong-Petit's Model")
plt.title("Dulong-Petit's Model",fontweight='bold')

plt.subplot(2,2,2)

#---------Einstein Model-------

Te=1320 #Einstein Temperature for Diamond

def Cve(T):
    a=3*R*((np.exp(Te/(T)))*(Te/(T))**2)
    b=(np.exp(Te/T)-1)**2
    return a/b
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat (J/(mol-K))")
plt.plot(T,Cve(T),color="orange",label="Einstein Model")
plt.title("Einstein Model",fontweight='bold')

plt.subplot(2,2,3)

#-----------Debye Model----------------

Td=2250 #Debye Temperature for Diamond

def f(y):
    f=y**4*np.exp(y)/(np.exp(y)-1)**2
    return f
Cvd=[0]*len(T)
for i in range(len(T)):
    res,err=quad(f,0,Td/T[i])
    Cvd[i]=res*9*R*(T[i]/Td)**3
    plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat (J/(mol-K))")
plt.plot(T,Cvd,color="green",label="Debye Model")
plt.title("Debye Model",fontweight='bold')

plt.subplot(2,2,4)

#Comparison
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat (J/(mol-K))")
plt.plot(T,Cv(T),label="Dulong-Petit's Model")
plt.plot(T,Cve(T),label="Einstein Model")
plt.plot(T,Cvd,label="Debye Model")
plt.title("Comparison of different model",fontweight='bold')
plt.tight_layout()
plt.legend()
plt.show()
