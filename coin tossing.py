import numpy as np
import matplotlib.pyplot as plt

N=int(input("Enter no. of coins : "))

wk=[0]*(N+1)
N1=[0]*(N+1)
N2=[0]*(N+1)

for i in range(len(N1)):
    N1[i]=i
    N2=len(N2)-i-1

print("N1:",N1)
print("N2:",N2)

for i in range(len(N1)):
    wk[i]=np.fact(N)/(np.fact(N1[i])*np.fact(N2[i]))

print("Thermodynamic probabilities:",wk)

plt.plot(N1,wk)
plt.show()
