import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
# 数组的维度
print(a.shape)
# 数组的轴数（维度）
print(a.ndim)
# 元素类型的对象
print(a.dtype.name)
# 数组每个元素的大小
print(a.itemsize)
# 数组元素长度
print(a.size)
print(type(a))