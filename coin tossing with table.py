import  numpy as np
import matplotlib.pyplot as plt



def fact(N):
	p=1
	for i in range(1,N+1):
		p=p*i
	return p

N=int(input("\n Enter no. of coin:"))

M=np.ones((N,2**N))
m=2**N
for i in range(N):
    p=2**(N-1-i)
    a=0
    
    for j in range(m):
        if a%2==0:
            M[i][p*a:p*(a+1)]*=0
            a+=1
        else:
            a+=1
                
Matrix=np.transpose(M)
Var=np.sum(Matrix,axis=1)
Matrix1=np.where(Matrix==0,"H","T")
print(Matrix1)


wk=[0]*(N+1)
N1=[0]*(N+1)
N2=[0]*(N+1)

for i in range(len(N1)):
    N1[i]=i
    N2[i]=len(N2)-i-1
    
print("N1",N1)
print("N2",N2)

for i in range(len(N1)):
    wk[i]=fact(N)/(fact(N1[i])*fact(N2[i]))
    
print("Thermodynamic probabilities:",wk)    

plt.plot(N1,wk)
plt.show()
