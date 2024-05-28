import numpy as np

rg = np.random.default_rng(1)  # create instance of default random number generator

a = np.floor(10 * rg.random((3, 4)))
print(a)
print("=========1=============")
print(a.shape)
print("=========2=============")
print(a.ravel())  # returns the array, flattened
print("=========3=============")
print(a.reshape(6, 2))  # returns the array with a modified shape
print("=========4=============")
print(a.T)  # returns the array, transposed
print("=========5=============")
print(a.T.shape)
print("=========6=============")
print(a)
print("=========7=============")
# resize方法修改数组本身
a.resize((2, 6))
print(a)
print("=========8=============")
print(a.reshape(3, -1))
print("=========9=============")

a = np.floor(10 * rg.random((2, 2)))
print(a)
print("=========10=============")

b = np.floor(10 * rg.random((2, 2)))
print(b)
print("=========11=============")
# column_stack函数将一维数组作为列堆叠到二维数组中。它等效于hstack仅用于 2D 数组
print(np.vstack((a, b)))
print("=========12=============")
print(np.hstack((a, b)))
print("=========13=============")

from numpy import newaxis

a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b)))  # returns a 2D array
print("=========14=============")
print(np.hstack((a, b)))       # the result is different
print("=========15=============")
print(a[:, newaxis])  # view `a` as a 2D column vector
print("=========16=============")
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print("=========17=============")
print(np.hstack((a[:, newaxis], b[:, newaxis])))  # the result is the same
print("=========18=============")


# row_stack函数等效vstack于任何输入数组。实际上，row_stack是vstack的别名
print(np.column_stack is np.hstack)
print(np.row_stack is np.vstack)


a = np.floor(10 * rg.random((2, 12)))
print(a)
# Split `a` into 3
print(np.hsplit(a, 3))
# Split `a` after the third and the fourth column
print(np.hsplit(a, (3, 4)))