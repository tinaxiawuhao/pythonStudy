import numpy as np

a = np.arange(6)                    # 1d array
print(a)
print("=================")
b = np.arange(12).reshape(4, 3)     # 2d array
print(b)
print("=================")
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)
print("=================")
print(np.arange(10000))
print("=================")
print(np.arange(10000).reshape(100, 100))