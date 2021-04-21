# -*- coding: utf-8 -*
"""
Created on Fri Mar 13 18:24:52 2020

@author: plouk
"""

import numpy as np 
from numpy.linalg import multi_dot, norm


A = np.zeros([1,])
B = np.zeros([1,2])
C = np.zeros([2,1])
A = A.reshape(1,1)

a = np.array([1, 2, 3])         # a.shape = (3,)
b = np.array([[1], [2], [3]])   # b.shape = (3, 1)
c = np.array( [ [1, 2, 3] ] )       # c.shape = (1, 3)

b.reshape(3) # array([1, 2, 3]); doesn't affect b
b = b.reshape(3) # array is changed to array([1, 2, 3])


b = np.array([1, 2, 3], copy=True)
d = b  # d is a pointer to b
"""e = np.copy(b)"""

b = 2*b 
print(d)


alpha = np.array([[1], [2]])
beta = np.array([[3, 4]])

c = np.array( [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] ] ) 
alpha.dot( beta )
x= np.dot( alpha, beta )
y = np.array( [ [1, 2], [6, 7] ] ) 
np.dot( beta, alpha )[0,0]
np.dot( alpha, beta, c)
multi_dot( [alpha, beta, c] )
alpha.dot( beta ).dot(c)


C = np.zeros([3,4], dtype = int)
c = np.ones([3,4])


c = np.array( [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] ] ) 
d = np.zeros_like( c, dtype = 'float64' )
e = np.ones_like( c )

#========= norms for vectors =============================
# we said that the vector-element absolute sum must be below or equal to one

a = np.array([[0], [-1], [1]])
norm(a, 2)
norm(a, 1)
norm(a, np.inf)