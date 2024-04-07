
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k,e


T = np.arange(0.1,2000,10)
E = 0.01 #Energy Difference
nl=[0,1,2] #Energy level
N = int(input('Enter the number of particles: '))
k = k/e


#Creating Finite Difference Function
#F'(x)= {F(x+h)-F(x)}/{h}
def D(x,F):
    h=0.1
    return (F(x+h)-F(x))/h


#Defining Partition Function
def Z(T,E):
    z=0
    for i in range(len(nl)):
        z+=np.exp(-i*E/(k*T))
    return z**N


#Defining Helmholtz Energy Function
def F(T,E):
    return -k*T*np.log(Z(T,E))


#Average Energy
def U(T,E):
    u = k*T**2*D(T,lambda T: np.log(Z(T,E)))
    return u

#Entropy
def S(T,E):
    s = -D(T,lambda T: F(T,E))
    return s

#Specific Heat At Constant Volume
def C_v(T,E):
    c_v = D(T,lambda T: U(T,E))
    return c_v

#Plotting Each Functions

#Partition Function
plt.figure(1)
plt.xlabel('T')
plt.ylabel('Z(T,E)')
plt.title('Plot of Partition Function vs T')
plt.plot(T, Z(T,E))

#Helmholtz Energy Function
plt.figure(2)
plt.xlabel('T')
plt.ylabel('F(T,E)')
plt.title('Plot of Helmholtz Energy Function vs T')
plt.plot(T, F(T,E))

#Average Energy Function
plt.figure(3)
plt.xlabel('T')
plt.ylabel('U(T,E)')
plt.title('Plot of Average Energy Function vs T')
plt.plot(T, U(T,E))

#Entropy Function
plt.figure(4)
plt.xlabel('T')
plt.ylabel('S(T,E)')
plt.title('Plot of Entropy Function vs T')
plt.plot(T, S(T,E))

#Specific Heat at Constant Volume Function
plt.figure(5)
plt.xlabel('T')
plt.ylabel('C_v(T,E)')
plt.title('Plot of Specific Heat at Constant Volume Function vs T')
plt.plot(T, C_v(T,E))
plt.show()
