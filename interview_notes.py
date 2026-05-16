# =====================================================
# NUMPY INTERVIEW CHEAT SHEET
# =====================================================

print("""

WHY NUMPY IS FAST
-----------------

• contiguous memory
• vectorized operations
• compiled C implementation
• avoids Python loop overhead


ARRAY PROPERTIES
----------------

shape
→ size along axes

size
→ total elements

ndim
→ number of dimensions

dtype
→ datatype

nbytes
→ memory occupied


AXIS
-----

axis0
↓ rows

axis1
→ columns


SLICING
--------

start included
stop excluded


NEGATIVE INDEXING
-----------------

-1 last
-2 second last

arr[::-1]
reverses


BOOLEAN MASKING
---------------

mask preserves shape

filter creates new array


FANCY INDEXING
--------------

[0,2]
shopping list


scores[[0,2],[1,3]]

acts like zip()


np.ix_()

creates cartesian products


RESHAPE
--------

rows × cols
=
total elements


reshape does not create
or destroy data


-1 auto-calculates dimension


FLATTEN VS RAVEL
----------------

flatten()
copy


ravel()
view (when possible)


VIEWS VS COPIES
---------------

slice
→ window


copy
→ photocopy


BROADCASTING
------------

compare RIGHT → LEFT

dimensions compatible if:

equal

or

one is 1


NEW AXIS
--------

[:,None]

adds dimension

(2,) → (2,1)

""")