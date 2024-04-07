#   Name : Sidhanth Gupta
# Roll no: 19/17075

#Question : Verification of Orthogonality of Legendre Polynomials.

#-----------importing library-----------
import numpy as np
#-----------Defining limits-----------
a = -1
b = 1
#-----------for different legendre polynomial-----------
#-----------defining function : Pn(u)*Pm(u)-----------
def f(u):
    P1 = u                    # first legendre polynomial
    P2 = (1/2)*(3*(u**2) - 1) # second legendre polynomial
    return (P1*P2)

#-----------integration using gauss quadrature-----------

#-----------using 3 point formula-----------

# Weight Functions
w1 = 5/9 
w2 = 8/9 
w3 = 5/9

u1 = np.sqrt(3/5)
u2 = 0
u3 = -np.sqrt(3/5)

#  Abscisae
x1 = ((b-a)/2)*u1 + (b+a)/2
x2 = ((b-a)/2)*u2 + (b+a)/2
x3 = ((b-a)/2)*u3 + (b+a)/2


y = (b-a)/2*(w1*f(x1) + w2*f(x2) + w3*f(x3))
print("Integral result for different legendre polynomials i.e. n is not equal to m : ",y)
print(" ")


#------------for same legendre polnomial-----------
def g(u):
    g1 = u # first legendre polynomial
    return (g1*g1)
#-----------using 3 point formula-----------
y1 = (b-a)/2*(w1*g(x1) + w2*g(x2) + w3*g(x3))
print("Integral result for same legendre polynomials i.e. n is equal to m : ",y1)
print(" ")

#--------verification using formula-----------
n = 1
y2 = (2)/(2*n + 1)
print(" verfication using orthogonality formula:",y2)
