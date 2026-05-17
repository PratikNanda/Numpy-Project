import numpy as np

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