import numpy as np

# 1D array from list
a = np.array([1, 2, 3])
# 2D array from nested lists
b = np.array([[1, 2], [3, 4]])

print(a)
print(b)

# Evenly spaced values
c = np.arange(0, 20, 10)        # [0,2,4,6,8]
# Equally spaced over interval
d = np.linspace(0, 2, 5)       # [0.,0.25,0.5,0.75,1.]
# All zeros or ones
z = np.zeros((3,4))
o = np.ones((2,3))
# Constant fill
f = np.full((3,4), 3)
# Identity matrix
i = np.eye(5)

print(i)

arr = np.random.rand(3,4)
print(arr.shape)    # dimensions (3,4)
print(arr.ndim)     # number of axes: 2
print(arr.size)     # total elements: 12
print(arr.dtype)    # data type, e.g. float64


a = np.array([10, 20, 30, 40])
print(a[1])        # 20
print(a[-1])       # 40


m = np.arange(16).reshape(4,4)
# rows 1–2, cols 2–3
sub = m[1:3, 2:4]
print(sub)

x = np.array([5,10,15,20])
mask = x > 10
print(x[mask])             # [15,20]
# fancy indexing    
inds = [0,3]
print(x[inds])             # [5,20]



arr = np.arange(1,10).reshape(3,3)
print(arr.sum())           # total sum
print(arr.mean(axis=0))    # mean per column
print(arr.max(axis=1))     # max per row
print(arr.std())           # standard deviation


a = np.arange(12)
b = a.reshape(3,4)         # change shape
flat = b.flatten()         # 1D copy
t = b.T                     # transpose (4×3)
# add/remove dimensions
c = np.expand_dims(a, axis=1)   # shape (12,1)
d = np.squeeze(c)                # back to (12,)


a = np.arange(3)           # [0,1,2]
b = np.array([[10],[20],[30]])
# a (1×3) broadcast to (3×3) then add
c = a + b                  # [[10,11,12],[20,21,22],[30,31,32]]

