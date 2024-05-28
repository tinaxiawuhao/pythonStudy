import numpy as np
from numpy import pi

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
print("=======================")
c = a - b
print(c)
print("=======================")
print(b**2)
print("=======================")
print(10 * np.sin(a))
print("=======================")
print(a < 35)
print("=======================")
A = np.array([[1, 1],
               [0, 1]])
B = np.array([[2, 0],
               [3, 4]])
print(A * B)    # elementwise product
print("=======================")
print(A @ B)     # matrix product
print("=======================")
print(A.dot(B))  # another matrix product
print("=======================")
rg = np.random.default_rng(1)  # create instance of default random number generator
print(rg)
print("=======================")
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)
print("=======================")
b += a
print(b)
print("=======================")
# a += b  # b is not automatically converted to integer type

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)
c = a + b
print(c)
print(c.dtype.name)
d = np.exp(c * 1j)
print(d)
print(d.dtype.name)
print("=======================")

a = rg.random((2, 3))
print(type(a))
print(a.sum())
print(a.min())
print(a.max())
print("=======================")

b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0))     # sum of each column
print(b.min(axis=1))     # min of each row
print(b.cumsum(axis=1))  # cumulative sum along each row
print("=======================")