import numpy as np

# =====================================================
# PART 1: Basic ndarray Fundamentals
# =====================================================

print("\n========== BASIC ARRAY ==========\n")

a = [10,20,30,40]

b = np.array([10,20,30,40])

print("Python List Type:")
print(type(a))

print("\nNumPy Array Type:")
print(type(b))

print("\nDatatype:")
print(b.dtype)

print("\nShape:")
print(b.shape)

print("\nDimensions:")
print(b.ndim)

print("\nTotal Elements:")
print(b.size)

print("\nMemory in bytes:")
print(b.nbytes)


# Interview Notes:
#
# shape  -> size along each axis
# size   -> total elements
# ndim   -> number of dimensions
# dtype  -> datatype
# nbytes -> memory usage


# =====================================================
# PART 2: Understanding Shape
# =====================================================

print("\n========== SHAPE EXAMPLES ==========\n")

x=np.array([
    [10,20,30],
    [40,50,60]
])

print(x)

print("\nShape:")
print(x.shape)

print("Size:")
print(x.size)

print("Dimensions:")
print(x.ndim)

# Shape = rows, columns

# (2,3)

# axis 0 length = 2
# axis 1 length = 3

