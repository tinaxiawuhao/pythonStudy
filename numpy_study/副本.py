import numpy as np

a = np.array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11]])
b = a            # no new object is created
print(b is a)

c = a.view()
print(c is a)
print(c.base is a)         # c is a view of the data owned by a
print(c.flags.owndata)
c = c.reshape((2, 6))  # a's shape doesn't change
print(a.shape)
c[0, 4] = 1234         # a's data changes
print(a)   

print("==================")
d = a.copy()  # a new array object with new data is created
print(d is a)
print(d.base is a)  # d doesn't share anything with a
d[0, 0] = 9999
print(d)
