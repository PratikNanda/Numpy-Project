import numpy as np

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