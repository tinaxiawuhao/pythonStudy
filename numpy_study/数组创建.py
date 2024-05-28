import numpy as np

a = np.array([2, 3, 4])
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

# a = np.array(1, 2, 3, 4) #创建错误
a = np.array([1, 2, 3, 4])

print(np.array([(1.5, 2, 3), (4, 5, 6)]))

print(np.array([[1, 2], [3, 4]], dtype=complex))
print("=============")
print(np.zeros((3, 4)))

print(np.ones((2, 3, 4), dtype=np.int16))
print("=============")

print(np.empty((2,3)))
print("=============")
print(np.arange(10, 30, 5))
print(np.arange(0, 2, 0.3))

print("=============")
from numpy import pi
# 当arange与浮点参数一起使用时，由于浮点精度有限，通常无法预测获得的元素数量。
# 出于这个原因，通常最好使用linspace接收我们想要的元素数量作为参数的函数，而不是步骤
print(np.linspace(0, 2, 9))                  # 9 numbers from 0 to 2
x = np.linspace(0, 2 * pi, 10)        # useful to evaluate function at lots of points
print(x)
f = np.sin(x)
print(f)
