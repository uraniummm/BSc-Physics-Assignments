import numpy as np 
import matplotlib.pyplot as plt
from scipy.constants import k,c,e
import sympy as sp
E=np.linspace(-1,1,1000)
# print(k)
u=0
a=[-1,0,1]

T=np.arange(100,1000,200)
def F(a,T):
    g=(np.exp(((E-u)*e)/(k*T)))+a
    return 1/g
for i in a:
    for j in T:
        plt.plot(E,F(i,j),label="T="+str(j)+"K")
        plt.legend(loc='best')
    plt.ylabel("f(E) -->")
    plt.xlabel("Energy(ev) -->")

    if i==-1 :
        plt.title("Bose-Einstein Distribution with u=0")
        plt.ylim(-10,10)
        plt.xlim(-.15,.15)
    elif i==0:
        plt.title("Maxwell-Boltzmann Distribution with u=0")
        plt.ylim(0,3)
        plt.xlim(-.5,.5)
    else:
        plt.title("Fermi-Dirac Distribution with u=0")
    plt.show()