import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Plotting the Scattered graph
x=[-3,-2,-1,0,1,2,3] #Data points for X-axis
y=[7.5,3.0,0.5,1.0,3.0,6.0,14.0] #Data points for Y-axis
plt.plot(x,y,"o",label="Scattered")
#plt.show()

#Finding coefficients using Formula
p=sum(x) #Summation x
q=sum(np.square(x)) #Summation x^2
r=sum(np.power(x,3)) #Summation x^3
s=sum(np.power(x,4)) #Summation x^4
t=sum(y) #Summation y
u=sum(np.multiply(np.square(x),y)) #Summation x^2*y
v=sum(np.multiply(x,y)) #Summation x*y
n=len(x)
A=[[n,p,q],[p,q,r],[q,r,s]]
B=[[t],[v],[u]]
X=np.linalg.solve(A,B)
print("X:",X)
c=[[0],[0],[0]]  
for i in range(3):
    c[i]=X[2-i]
print("C:",c)
A=np.transpose(c)
print("A:",A)
y=np.poly1d(A.flatten())
print("A:",A.flatten())
print("Equation for Quadratic Line using formula:",y)
Y=[y(x) for x in x]

#Plotting using Formula
plt.plot(x,Y,"--",label="Using derived formula")
plt.xlim([-4,4]) #This Limit is changing the graph
plt.ylim([0,14])
plt.legend()
plt.title("Quadratic Line fitting using formula")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
