

# y"+4y=0
# y(0)=-2
#y(pi/4)=10

import numpy as np
import matplotlib.pyplot as plt
n=100
a=0 
b=np.pi/4
h=(b-a)/n

A=np.zeros((n+1,n+1))

A[0,0]=1
A[n,n]=1


for i in range(1,n):
    A[i,i+1]=1
    A[i,i]=4*(h*h)-2
    A[i,i-1]=1

print("A:",A)

B=np.zeros(n+1)
B[0]=-2
B[1:-1]=0

B[-1]=10

print(B)

y=np.linalg.solve(A,B)
x=np.linspace(a,b,n+1)
print("y:",y)   
plt.plot(x,y)
plt.show()