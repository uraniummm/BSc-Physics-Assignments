import numpy as np
import matplotlib.pyplot as plt

def gau(x,mu,sig):
    return np.exp(-((x-mu)**2.0)/(2.0*sig**2.0))/(np.sqrt(2.0*np.pi))/sig

mu1= 0;sig1 = 0.05
mu2 = 0 ; sig2 = 0.35
mu3 = 4 ; sig3 = 0.55
mu4 = 7 ; sig4 = 0.95

x=np.linspace(-15,15, 500)

fig, ax =plt.subplots(2,2)
ax[0,0].plot(x,gau(x,mu1,sig1),color='r')
ax[0,1].plot(x,gau(x,mu2,sig2),color='b')
ax[1,0].plot(x,gau(x,mu3,sig3),color='y')
ax[1,1].plot(x,gau(x,mu4,sig4),color='g')
plt.show()