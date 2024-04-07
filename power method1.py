import numpy as np

def normalize(x):
    fac = abs(x).max() # fac is the factorized value on each step which will become
                       #  largest eigen value  
    x_n = x / x.max()  # x_n will be the vector for next step
    return fac, x_n    

# Dominant eigen vector 
x = np.array([1, 1, 0])
# A matrix
a = np.array([[1, -1, 0], 
              [-1, 2, -1],
              [0, -1, 1]])

for i in range(5):
    x = np.dot(a, x)
    lambda_1, x = normalize(x)   # lambda1.v1= A.x(k-1)
    
print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)
