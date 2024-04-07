import numpy as np
import matplotlib.pyplot as plt

N=input("Enter no. of coins : ")
print(np.math.factorial)
wk=[0]*(N+1)
N1=[0]*(N+1)
N2=[0]*(N+1)

for i in range(len(N1)):
    N1[i]=i
    N2=len(N2)-i-1

print("N1:",N1)
print("N2:",N2)

for i in range(len(N1)):
    wk[i]=np.math.factorial(N)/(np.math.factorial(N1[i])*np.math.factorial(N2[i]))

print("Thermodynamic probabilities:",wk)

plt.plot(N1,wk)
plt.show()
