
#Program:6

#Evaluation of Wein’s Constant and verification of Wein’s Law (by drawing a table).

import numpy as np
import matplotlib.pyplot as plt
from scipy. constants import h,pi,k,c
from tabulate import tabulate

w=np.linspace(0.005e-6,8e-6,1000)
emax=[0,0,0,0]
T=[1500,1750,2000,2250]
def pl(w,T):
    pl=(8*pi*h*c)/(w**5*(np.exp((h*c)/(w*k*T))-1))
    return pl
    
for i in range(4):
    plt.plot(w,pl(w,T[i]),label="T="+str(T[i])+"K")

p=[0]*len(w)


for j in range(4):
    for i in range(len(w)):
        p[i]=(8*pi*h*c)/(w[i]**5*(np.exp((h*c)/(w[i]*k*T[j]))-1))
        emax[j]=np.max(p)

#print(emax) #Maximum value of energy for different temperature
lmax=[0]*4
for j in range(4):
    for i in range(1,len(w)):
        p[i]=(8*pi*h*c)/(w[i]**5*(np.exp((h*c)/(w[i]*k*T[j]))-1))
        if p[i]>=p[i-1]:
            lmax[j]=i
#print(lmax) #Value in the array for which lambda is maximum for different temperature

wmax=[0]*4
for i in range(4):
    wmax[i]=w[lmax[i]]

#print(wmax) #Corresponding lambda to maximum value of energy



#table=[['W_peak','Temp','Wein Constant'],[1,2,1],[1,3,5]]

print("W_peak","     ","Temperature","     ","Wein Constant")
for i in range(4):
    print(np.round(wmax[i],10),"        ",T[i],"        ",np.round(wmax[i]*T[i],6))
    #plt.plot(wmax[i],emax[i],'ko')
plt.scatter(wmax,emax,color='k',marker='x')
plt.plot(wmax,emax,color='k')
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Density (J/m^3)")
plt.legend()
plt.title("Plots of Planck's law at different temperatures wrt wavelength")
plt.show()
