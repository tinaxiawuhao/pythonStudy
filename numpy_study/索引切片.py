import numpy as np

a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])
a[:7:2] = 1000
print(a)
print(a[::-1])  # reversed a
for i in a:
    print(i**(1 / 3.))
    
def f(x, y):
     return 10 * x + y
print("====================")
b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
print("====================")
print(b[2, 3])
print("====================")
print(b[0:5, 1])  # each row in the second column of b
print("====================")
print(b[:, 1])    # equivalent to the previous example
print("====================")
print(b[1:3, :])  # each column in the second and third row of b
print("====================")

c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100, 101, 102],
                [110, 112, 113]]])
print(c.shape)
print(c[1, ...])  # same as c[1, :, :] or c[1]
print(c[..., 2])  # same as c[:, :, 2]
print("====================")

for row in b:
    print(row)
print("====================")
for element in b.flat:
    print(element)
    
print("====================")    
palette = np.array([[0, 0, 0],         # black
                     [255, 0, 0],       # red
                     [0, 255, 0],       # green
                     [0, 0, 255],       # blue
                     [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                   [0, 3, 4, 0]])
print(palette[image])  # the (2, 4, 3) color image

print("====================") 
time = np.linspace(20, 145, 5)  # time scale
data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
print(time)
print(data)
print("====================")
ind = data.argmax(axis=0)
print(ind)
print("====================")
# times corresponding to the maxima
# time_max = data[ind]
data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]...
# print(time_max)
print(data_max)
print("====================")
print(np.all(data_max == data.max(axis=0)))