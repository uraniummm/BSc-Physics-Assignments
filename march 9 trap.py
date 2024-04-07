# ----By : Sidhanth Gupta------
# ---- Roll No. : 19/17075-------

import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return 1/(1+x)

a=0
b=1
exact=np.log(2)

# -----------trapezoidal method-------------- 
# n=2
# h=(b-a)/n
# s=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s=s+y[i]
        
# I=(h/2)*(f(a)+2*s+f(b)) 
# print("By trapezoidal rule for n=2:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)

          
# n=4
# h=(b-a)/n
# s=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s=s+y[i]
    
# I=(h/2)*(f(a)+2*s+f(b)) 
# print("By trapezoidal rule for n=4:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)



# n=8
# h=(b-a)/n
# s=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
    # x[i]=x[0]+i*h
    # y[i]=f(x[i])
    # s=s+y[i]
    
# I=(h/2)*(f(a)+2*s+f(b)) 
# print("By trapezoidal rule for n=8:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)

#-----------simpson's 1/3 rule--------

# n=2
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])

# for i in range(1,n,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s1=s1+y[i]  #s1= y1+y3+y5+....y(n-1)

# for i in range(2,n-1,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s2=s2+y[i]  #s2= y2+y4+y6+.....y(n-2)
    
# I= (h/3)*(f(a)+ (4*s1) + (2*s2)+f(b)) 
# print("By simpsons 1/3 rule for n=2:",I)
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)


# n=4
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])

# for i in range(1,n,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s1=s1+y[i]  #s1= y1+y3+y5+....y(n-1)

# for i in range(2,n-1,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s2=s2+y[i]  #s2= y2+y4+y6+.....y(n-2)
    
# I= (h/3)*(f(a)+ (4*s1) + (2*s2)+f(b)) 
# print("By simpsons 1/3 rule for n=4:",I)
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)
   


# n=8
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])

# for i in range(1,n,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s1=s1+y[i]  #s1= y1+y3+y5+....y(n-1)

# for i in range(2,n-1,2):
#     x[i]=x[0]+i*h
#     y[i]=f(x[i])
#     s2=s2+y[i]  #s2= y2+y4+y6+.....y(n-2)
    
# I= (h/3)*(f(a)+ (4*s1) + (2*s2)+f(b)) 
# print("By simpsons 1/3 rule for n=8:",I)
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)




#-----------simpson's 3/8 rule---------


# n=2
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
#    x[i]=x[0]+i*h
#    if(i%3==0):
#        y[i]=f(x[i])
#        s1=s1+y[i]
#    else:
#      y[i]=f(x[i])
#      s2=s2+y[i]
              
        
# I=((3*h)/8)*(f(a) + 2*s1 + 3*s2 + f(b)) 
# print("By Simpson's 3/8 for n=2:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)


# n=4
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
#     x[i]=x[0]+i*h
#     if(i%3==0):
#         y[i]=f(x[i])
#         s1=s1+y[i]
#     else:
#       y[i]=f(x[i])
#       s2=s2+y[i]
              
        
# I=((3*h)/8)*(f(a) + 2*s1 + 3*s2 + f(b)) 
# print("By Simpson's 3/8 for n=4:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)


# n=8
# h=(b-a)/n
# s1=0
# s2=0
# x=np.linspace(a,b,n)
# x[0]=0
# y=np.linspace(a,b,n)
# y[0]=f(x[0])
# for i in range(1,n):
#    x[i]=x[0]+i*h
#    if(i%3==0):
#        y[i]=f(x[i])
#        s1=s1+y[i]
#    else:
#      y[i]=f(x[i])
#      s2=s2+y[i]
              
        
# I=((3*h)/8)*(f(a) + 2*s1 + 3*s2 + f(b)) 
# print("By Simpson's 3/8 for n=8:",I)  
# error=abs((I-np.log(2)))
# print("Exact value:",exact)
# print("Absolute Error: ",error)