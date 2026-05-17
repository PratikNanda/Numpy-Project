import numpy as np
import time

# ndarray basics
b=np.array([10,20,30,40])
print(b.shape)
print(b.size)
print(b.ndim)
print(b.dtype)
print(b.nbytes)

# sports dataset
scores=np.array([
    [45,67,23,89],
    [78,56,91,88],
    [34,55,61,72]
])

print(scores[1])
print(scores[-1])
print(scores[:,2])
print(scores[0:2,1:3])
print(scores[1:,2:])

# reverse
arr=np.array([10,20,30,40])
print(arr[::-1])

# masking
high=scores>70
print(high)
print(scores[scores>70])

# fancy indexing
print(scores[[0,2]])
print(scores[[0,2],[1,3]])
print(scores[np.ix_([0,2],[1,3])])

# reshape
arr=np.arange(12)
print(arr.reshape(3,4))
print(arr.reshape(2,6))
print(arr.reshape(3,-1))

# flatten vs ravel
matrix=np.array([
[1,2,3],
[4,5,6]
])

flat=matrix.flatten()
print(flat)
rav=matrix.ravel()
print(rav)

flat[0]=999
print(flat)
rav[1]=777
print(rav)

print(matrix)

# references
a=np.array([1,2,3])
b=a
b[0]=999

c=a.copy()
c[1]=555

print(a)
print(c)

# slice views
x=np.array([
[1,2],
[3,4]
])

y=x[:,0]
y[0]=999

print(x)

# broadcasting
arr=np.array([1,2,3])
print(arr+10)

matrix=np.array([
[1,2,3],
[4,5,6]
])

bonus=np.array([
[10],
[20]
])

print(matrix+bonus)

# new axis
b=np.array([10,20])
print(b[:,None])

# aggregation
scores=np.array([
[45,67,23],
[78,56,91]
])

print(scores.sum())
print(scores.sum(axis=0))
print(scores.sum(axis=1))
print(scores.mean(axis=0))
print(scores.max(axis=1))

# matrix multiply
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])

print(a*b)
print(a@b)

# performance
large=np.arange(1000000)

start=time.time()
res=[]
for x in large:
    res.append(x+5)
print(time.time()-start)

start=time.time()
large+5
print(time.time()-start)
