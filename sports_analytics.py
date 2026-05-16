# =====================================================
# NUMPY INTERVIEW PROJECT
# Sports Performance Analytics Engine
# End-to-End Learning Notebook
# Phase 1 + Phase 2 + Broadcasting Foundations
# =====================================================

import numpy as np


# =====================================================
# PART 1: BASIC NDARRAY FUNDAMENTALS
# =====================================================

print("\n========== BASIC ARRAY ==========\n")

a=[10,20,30,40]

b=np.array([10,20,30,40])

print("Python list type:")
print(type(a))

print("\nNumPy array type:")
print(type(b))

print("\nDatatype:")
print(b.dtype)

print("\nShape:")
print(b.shape)

print("\nDimensions:")
print(b.ndim)

print("\nTotal elements:")
print(b.size)

print("\nMemory in bytes:")
print(b.nbytes)



# =====================================================
# PART 2: SHAPE EXAMPLES
# =====================================================

print("\n========== SHAPE EXAMPLES ==========\n")

x=np.array([
    [10,20,30],
    [40,50,60]
])

print(x)

print("\nShape:")
print(x.shape)

print("\nSize:")
print(x.size)

print("\nDimensions:")
print(x.ndim)



# =====================================================
# PART 3: SPORTS ANALYTICS DATASET
# =====================================================

print("\n========== SPORTS DATA ==========\n")

scores=np.array([
    [45,67,23,89],
    [78,56,91,88],
    [34,55,61,72]
])

print(scores)

print("\nShape:")
print(scores.shape)

print("\nDimensions:")
print(scores.ndim)

print("\nSize:")
print(scores.size)



# =====================================================
# PART 4: INDEXING
# =====================================================

print("\n========== INDEXING ==========\n")

print("Second player:")
print(scores[1])

print("\nLast player:")
print(scores[-1])



# =====================================================
# PART 5: COLUMN SELECTION
# =====================================================

print("\n========== COLUMN SELECTION ==========\n")

print("Third column")
print(scores[:,2])



# =====================================================
# PART 6: SLICING
# =====================================================

print("\n========== SLICING ==========\n")

print("Rows 0-1 and cols 1-2")

print(scores[0:2,1:3])


print("\nFirst two rows")

print(scores[:2])


print("\nRows from index1 onward")
print(scores[1:,2:])



# =====================================================
# PART 7: NEGATIVE INDEXING
# =====================================================

print("\n========== NEGATIVE INDEXING ==========\n")

arr=np.array([10,20,30,40])

print(arr[-1])

print(arr[-2])



# =====================================================
# PART 8: REVERSING
# =====================================================

print("\n========== REVERSING ==========\n")

print(arr[::-1])



# =====================================================
# PART 9: BOOLEAN MASKING
# =====================================================

print("\n========== BOOLEAN MASKING ==========\n")

high_scores=scores>70

print(high_scores)

print("\nMask shape:")
print(high_scores.shape)



# =====================================================
# PART 10: FILTER VALUES
# =====================================================

print("\n========== FILTERED SCORES ==========\n")

filtered=scores[scores>70]

print(filtered)

print("\nShape:")
print(filtered.shape)



# =====================================================
# PART 11: FANCY INDEXING
# =====================================================

print("\n========== FANCY INDEXING ==========\n")

print("Rows 0 and 2")

selected=scores[[0,2]]

print(selected)


print("\nPairwise behavior")

pairwise=scores[[0,2],[1,3]]

print(pairwise)


print("\nCartesian product")

grid=scores[np.ix_([0,2],[1,3])]

print(grid)



# =====================================================
# PART 12: RESHAPE
# =====================================================

print("\n========== RESHAPING ==========\n")

arr=np.arange(12)

print("Original")

print(arr)

print("\nShape")
print(arr.shape)


reshape34=arr.reshape(3,4)

print("\n3x4")

print(reshape34)


reshape26=arr.reshape(2,6)

print("\n2x6")

print(reshape26)


print("\nAuto shape")

print(arr.reshape(3,-1))



# =====================================================
# PART 13: RESHAPE ERROR
# =====================================================

print("\n========== RESHAPE ERROR ==========\n")

try:

    arr.reshape(5,2)

except Exception as e:

    print(e)



# =====================================================
# PART 14: FLATTEN VS RAVEL
# =====================================================

print("\n========== FLATTEN VS RAVEL ==========\n")

matrix=np.array([
    [1,2,3],
    [4,5,6]
])

flat=matrix.flatten()

rav=matrix.ravel()

print("Flatten")

print(flat)

print("\nRavel")

print(rav)



print("\nModify flatten")

flat[0]=999

print(flat)

print("\nMatrix remains")

print(matrix)



print("\nModify ravel")

rav[1]=777

print(rav)

print("\nMatrix changes")

print(matrix)



# =====================================================
# PART 15: VIEWS VS COPIES
# =====================================================

print("\n========== VIEWS VS COPIES ==========\n")

a=np.array([1,2,3])

b=a

b[0]=999

print("a")

print(a)

print("b")

print(b)



print("\nReal copy")

c=a.copy()

c[1]=555

print("a")

print(a)

print("c")

print(c)



# =====================================================
# PART 16: SLICE VIEW BEHAVIOR
# =====================================================

print("\n========== SLICE VIEWS ==========\n")

x=np.array([
    [1,2],
    [3,4]
])

print("Original")

print(x)


y=x[:,0]

print("\nFirst column")

print(y)


y[0]=999

print("\nModified view")

print(y)

print("\nOriginal changed")

print(x)



z=x[:,1]

z[1]=777

print("\nSecond slice")

print(z)

print("\nOriginal changed")

print(x)



# =====================================================
# PART 17: BROADCASTING
# =====================================================

print("\n========== BROADCASTING ==========\n")

a=np.array([1,2,3])

print(a+10)

print(a*5)

print(a-1)



# =====================================================
# PART 18: 2D BROADCASTING
# =====================================================

print("\n========== 2D BROADCASTING ==========\n")

matrix=np.array([
    [1,2,3],
    [4,5,6]
])


bonus=np.array([
    [10],
    [20]
])


print(matrix)

print("\nBonus")

print(bonus)

print("\nResult")

print(matrix+bonus)



# =====================================================
# PART 19: NEW AXIS
# =====================================================

print("\n========== NEW AXIS ==========\n")

b=np.array([10,20])

print("Original shape")

print(b.shape)

column=b[:,None]

print("\nConverted")

print(column)

print("\nShape")

print(column.shape)

# =====================================================
# PART 20: VECTORIZATION VS PYTHON LOOPS
# =====================================================

import time

print("\n========== VECTORIZATION ==========\n")

large=np.arange(1000000)


start=time.time()

result=[]

for x in large:

    result.append(x+5)

end=time.time()

print("Python loop time:")

print(end-start)



start=time.time()

new=large+5

end=time.time()

print("\nNumPy vectorized time:")

print(end-start)