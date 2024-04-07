# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:08:08 2021

@author: hp
"""

# df= (f(x+h)-f(x-h))/(2*h)
#dff=(f(x+h)-2*f(x)+f(x-h))/(h*h)
# f(x)= 0.5*x**5-0.2*x**3+0.1*x-0.2

import numpy as np
import matplotlib.pyplot as plt

f=lambda x:0.5*x**5-0.2*x**3+0.1*x-0.2

####### 1st part of the problem : At x=0.1, find first and second derivatives of the above function with the help of any one of the  finite differences method and compare solution at h = 0.1, 0.01, and 0.001.

h=0.1
#h1=0.01
#h2=0.001
x=np.linspace(-1,1)
x1=0.1
#central differentiation

# print("First derivatives using different values of h are : -")

# df1=(f(x1+h)-f(x1-h))/(2*h)
# print("df1=",df1)

# df2=(f(x1+h1)-f(x1-h1))/(2*h1)
# print("df2=",df2)                         
                         
# df3=(f(x1+h2)-f(x1-h2))/(2*h2)
# print("df3=",df3)

print("Second derivatives using different values of h are : -")

dff1=(f(x1+h)-2*f(x1)+f(x1-h))/(h*h)
print("dff1=",dff1)

# dff2=(f(x1+h1)-2*f(x1)+f(x1-h1))/(h1*h1)
# print("dff2=",dff2)

# dff3=(f(x1+h2)-2*f(x1)+f(x1-h2))/(h2*h2)
# print("dff3=",dff3)



####### 2nd part of the problem:Find first and second derivative  of the above function over domain [-1,1] by using central finite differences then plot the graph of function and its first and second derivatives at h =0.1

# plt.figure(1)
#First derivatives

# dy1=(f(x+h)-f(x-h))/(2*h)
# plt.plot(x,dy1)


#Second Derivatives

# dy2=(f(x+h)-2*f(x)+f(x-h))/(h*h)
# plt.plot(x,dy2)

#plot
# plt.legend(["dy1","dy2"])



####### 3rd part of the problem : Plot the  first derivative of the above function over [-1,1] by using forward, backward and central finite differences. Compare the plots with theoretical one at h = 0.01.

# plt.figure(2)
#central differentiation

# y1=(f(x+h1)-f(x-h1))/(2*h1)
# plt.plot(x,y1)

#forward difference

# y2= (f(x+h1)-f(x))/h1
# plt.plot(x,y2)

#backward difference
# y3=(f(x)-f(x-h1))/h1
# plt.plot(x,y3)

# plt.legend(["y1","y2","y3"])
# plt.show()